#!/usr/bin/env python3

"""
IOConfig for a bot which acquires its user credentials via plain text stored passwords.
"""

from typing import Sequence

import logging

import asyncpraw  # type: ignore
from mewbot.api.v1 import Output

from ..io_configs import RedditIOConfigBase
from .credentials import RedditPasswordCredentials


class RedditPasswordIOConfig(RedditIOConfigBase):
    """
    Provide both bot and user credentials in plain text.

    Reddit needs two types of credentials for a bot to log in
     - bot credentials
     - user credentials

    This IOConfig allows you to provide both in plain text.
    If you do not want to provide user credential (in plain text in a YAML file) then use
    the RedditBotIO config - where a browser will be opened and you will be prompted to
    authenticate into reddit.
    """

    # Credentials to store all the info needed to log into reddit
    hybrid_credentials: RedditPasswordCredentials = RedditPasswordCredentials(
        username="Probably not an actual username",
        password="Not a real password",
        client_id="SI8pN3DSbt0zor",
        client_secret="xaxkj7HNh8kwg8e5t4m6KvSrbTI",
        redirect_uri="http://localhost:8080",
        user_agent="testscript by some guy",
    )

    _subreddits: list[str]

    _logger: logging.Logger

    @property
    def display_name(self) -> str:
        """
        The name of this IOConfig - for display and printing purposes.

        :return:
        """
        return str(type(self).__name__)

    def __init__(self) -> None:
        super().__init__()

        self._logger = logging.getLogger(__name__ + ":" + type(self).__name__)

    # This mode requires quite a lot of info from the user
    @property
    def client_id(self) -> str:
        """
        Get the id of your bot within reddit.

        :return:
        """
        return self.hybrid_credentials.client_id

    @client_id.setter
    def client_id(self, value: str) -> None:
        """
        Set the id of your bot - must happen before connection.

        :param value:
        :return:
        """
        self.hybrid_credentials.client_id = value

    @property
    def client_secret(self) -> str:
        """
        Get the client secret.

        :return:
        """
        return self.hybrid_credentials.client_secret

    @client_secret.setter
    def client_secret(self, value: str) -> None:
        """
        Set the client secret - must happen before connection.

        :param value:
        :return:
        """
        self.hybrid_credentials.client_secret = value

    @property
    def user_agent(self) -> str:
        """
        Get the user_agent used to connect to reddit.

        :return:
        """
        return self.hybrid_credentials.user_agent

    @user_agent.setter
    def user_agent(self, value: str) -> None:
        """
        Set the user agent you're using to connect to reddit - must happen before connection.

        :param value:
        :return:
        """
        self.hybrid_credentials.user_agent = value

    @property
    def username(self) -> str:
        """
        Get the username being used to connected to reddit.

        :return:
        """
        return self.hybrid_credentials.username

    @username.setter
    def username(self, value: str) -> None:
        """
        Set the value of the username used to connect to reddit - must happen before connection.

        :param value:
        :return:
        """
        self.hybrid_credentials.username = value

    @property
    def password(self) -> str:
        """
        Get the password you used to connect to reddit.

        :return:
        """
        return self.hybrid_credentials.password

    @password.setter
    def password(self, value: str) -> None:
        """
        Set the password used to connect to reddit - must happen before connection.

        :param value:
        :return:
        """
        self.hybrid_credentials.password = value

    def complete_authorization_flow(self) -> None:
        """
        Login to reddit using bot credentials - with pre-added password.

        :return:
        """
        reddit = asyncpraw.Reddit(
            username=self.hybrid_credentials.username,
            password=self.hybrid_credentials.password,
            client_id=self.hybrid_credentials.client_id,
            client_secret=self.hybrid_credentials.client_secret,
            # Must be set. Will be used if you have 2fa on your persoanl account
            redirect_uri=self.hybrid_credentials.redirect_uri,
            user_agent=self.hybrid_credentials.user_agent,
        )

        self.praw_reddit = reddit

    def get_outputs(self) -> Sequence[Output]:
        """
        Return the reddit outputs - in this case just an empty list.

        :return:
        """
        return []
