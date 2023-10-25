#!/usr/bin/env python3

"""
Contains means of connecting to reddit - either via a bot account or your own.
"""

# Note - validation checks for plugins which make sure no forbidden files are overwritten
# when the plugin installs

from __future__ import annotations

from typing import List, Optional, Sequence, Union

import abc
import logging

import asyncpraw  # type: ignore
from mewbot.api.v1 import Input, IOConfig, Output

from .inputs.redditors import RedditRedditorInput
from .inputs.subreddit import RedditSubredditInput
from .outputs import RedditOutput


class RedditIOConfigBase(IOConfig):
    """
    Base class for all the forms of the mewbot reddit client.

    There are two types of bots which are supported by this client.
     - bots - acknowledged by reddit as such - need two sets of credentials
     - self-bots - bots which use your account directly - need one set of credentials

     Bots need a set of bot credentials and your credentials.
     Two ways of getting these credentials into the system are provided
      - oauth flow - where you'll be prompted to enter credentials in a pop up browser instance
        (not suited for headless operation)
      - password flow - where you just enter your credentials in plain text
      (note - unless you do additional work, password flow _may also_ require opening a browser
      window - especially if you have 2fa enabled).

    Self bots just need your credentials.
    The same two types of flow should be available for giving them.

    Note - due to implementation complications, there can only be one instance of praw active at a
    time.
    Asyncpraw is just an asynchronous wrapper around praw.
    As such, we need to pass the underlying object around.
    """

    _subreddit_input: Optional[RedditSubredditInput] = None
    _redditor_input: Optional[RedditRedditorInput] = None
    _output: Optional[RedditOutput] = None

    praw_reddit: asyncpraw.reddit

    _subreddits: list[str]
    _redditors: list[str]

    @property
    def subreddits(self) -> list[str]:
        """
        Return the subreddits being watched by the bot.

        :return:
        """
        return self._subreddits

    @subreddits.setter
    def subreddits(self, new_subreddits: list[str]) -> None:
        """
        Update the monitored subreddits.

        :param new_subreddits:
        :return:
        """
        if not isinstance(new_subreddits, list):
            raise AttributeError("Please provide a list of sites.")

        self._subreddits = new_subreddits

        if self._subreddit_input is not None:
            self._subreddit_input.subreddits = new_subreddits

    @property
    def redditors(self) -> List[str]:
        """
        Return the redditors being watched by the bot.

        :return:
        """
        return self._redditors

    @redditors.setter
    def redditors(self, new_redditors: List[str]) -> None:
        """
        Update the monitored redditors.

        :param new_redditors:
        :return:
        """
        if not isinstance(new_redditors, list):
            raise AttributeError("Please provide a list of sites.")

        self._redditors = new_redditors

        if self._redditor_input is not None:
            self._redditor_input.subreddits = new_redditors

    @staticmethod
    def enable_praw_logging() -> None:
        """
        Install log handlers for praw.

        :return:
        """
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        for logger_name in ("asyncpraw", "asyncprawcore"):
            logger = logging.getLogger(logger_name)
            logger.setLevel(logging.DEBUG)
            logger.addHandler(handler)

    def get_inputs(self) -> Sequence[Input]:
        """
        Return the inputs offered by the class.

        In this case , there are two
         - RedditSubredditInput - for watching subreddits
         - RedditUserInput - for watching users
        :return:
        """
        # Setup and store a praw_reddit instance
        # self.enable_praw_logging()
        self.complete_authorization_flow()

        inputs: List[Union[RedditSubredditInput, RedditRedditorInput]] = []
        if not self._subreddit_input:
            self._subreddit_input = RedditSubredditInput(
                praw_reddit=self.praw_reddit,
                subreddits=self._subreddits,
            )
            inputs.append(self._subreddit_input)
        if not self._redditor_input:
            self._redditor_input = RedditRedditorInput(
                praw_reddit=self.praw_reddit,
                redditors=self._redditors,
                reddit_state=self._subreddit_input.reddit_state,
            )
            inputs.append(self._redditor_input)

        return inputs

    @abc.abstractmethod
    def get_outputs(self) -> Sequence[Output]:
        """
        Return the reddit outputs - in this case probably an empty list.

        :return:
        """

    @abc.abstractmethod
    def complete_authorization_flow(self) -> None:
        """
        Login to reddit using bot credentials.

        Should be overridden for the particular way you're authenticating to reddit.
        :return:
        """
