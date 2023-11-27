# SPDX-FileCopyrightText: 2023 Mewbot Developers <mewbot@quicksilver.london>
#
# SPDX-License-Identifier: BSD-2-Clause

"""
Provides bindings to allow mewbot to communicate with reddit.
"""

from mewbot.io.client_for_reddit.io_configs.reddit_bot_oauth_io import (
    RedditBotOauthIOConfig,
)
from mewbot.io.client_for_reddit.io_configs.reddit_bot_password_io import (
    RedditBotPasswordIOConfig,
)
from mewbot.io.client_for_reddit.io_configs.reddit_self_io import RedditSelfIOConfig

__version__ = "0.0.2"

__all__ = ["RedditSelfIOConfig", "RedditBotPasswordIOConfig", "RedditBotOauthIOConfig"]
