#!/usr/bin/env python3

"""
For reddit bots which acquire user credentials via an oauth authentication flow.
"""

from typing import Sequence

import asyncpraw  # type: ignore
from mewbot.api.v1 import Output

from ..io_configs import RedditIOConfigBase
from .credentials import RedditBotCredentials


class RedditBotOauthIOConfig(RedditIOConfigBase):
    """
    Client connected to reddit using a bot style credentials.

    Normally, you will be prompted to log into reddit using the redirect_uri.
    (Log in as a normal bot seems to require both user and bot credentials.
    This is for where you
     - want to provide the bot credentials programmatically
     - want to provide the user credentials via an auth flow)
    """

    # Should pass regex base checks
    # From the praw docs -
    # https://asyncpraw.readthedocs.io/en/stable/getting_started/authentication.html
    bot_credentials: RedditBotCredentials = RedditBotCredentials(
        client_id="SI8pN3DSbt0zor",
        client_secret="xaxkj7HNh8kwg8e5t4m6KvSrbTI",
        redirect_uri="http://localhost:8080",
        user_agent="testscript by u/fakebot3",
    )

    @property
    def client_id(self) -> str:
        """
        Get the id of your bot within reddit.

        :return:
        """
        return self.bot_credentials.client_id

    @client_id.setter
    def client_id(self, value: str) -> None:
        """
        Set the id of your bot - only valid before connection.

        :param value:
        :return:
        """
        self.bot_credentials.client_id = value

    @property
    def client_secret(self) -> str:
        """
        Get the client secret used to connect to reddit.

        :return:
        """
        return self.bot_credentials.client_secret

    @client_secret.setter
    def client_secret(self, value: str) -> None:
        """
        Set the client secret used to connected to reddit - only valid before connection.

        :param value:
        :return:
        """
        self.bot_credentials.client_secret = value

    @property
    def user_agent(self) -> str:
        """
        Get the user_agent used to connect to reddit.

        :return:
        """
        return self.bot_credentials.user_agent

    @user_agent.setter
    def user_agent(self, value: str) -> None:
        """
        Set the user agent you're using to connect to reddit - only valid before connection.

        This just changes the user agent stored in the local credentials.
        Not sure if you can change the user agent for reddit after connect.
        :param value:
        :return:
        """
        self.bot_credentials.user_agent = value

    def complete_authorization_flow(self) -> None:
        """
        Login to reddit using bot credentials.

        No further authorization flow should be required.
        :return:
        """
        reddit = asyncpraw.Reddit(
            client_id=self.bot_credentials.client_id,
            client_secret=self.bot_credentials.client_secret,
            redirect_uri=self.bot_credentials.redirect_uri,
            user_agent=self.bot_credentials.user_agent,
        )

        print(reddit.auth.url(scopes=["identity"], state="...", duration="permanent"))

        self.praw_reddit = reddit

    def get_outputs(self) -> Sequence[Output]:
        """
        At the moment, this class does not support outputs.

        :return:
        """
        return []
