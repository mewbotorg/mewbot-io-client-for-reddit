"""
Tests loading an example reddit config.
"""

# pylint: disable=duplicate-code
# Repetition for emphasis is occasionally desirable in tests

from __future__ import annotations

import pytest
import yaml

from mewbot.core import ConfigBlock
from mewbot.loader import load_component
from mewbot.test import BaseTestClassWithConfig

from mewbot.io.client_for_reddit import RedditBotPasswordIOConfig

CONFIG_YAML = "examples/trivial_reddit_bot.yaml"
CONFIG_YAML_NAME = "trivial_reddit_bot.yaml"


class TestLoader:
    """
    Base test loader class - contains core methods to load and run examples for testing purposes.
    """

    @staticmethod
    def test_empty_config() -> None:
        """
        Tests trying to load a bad config block - an empty one.

        :return:
        """
        # Build a bad config and give it to the bot
        this_config = ConfigBlock()  # type: ignore
        with pytest.raises(ValueError):  # @UndefinedVariable
            _ = load_component(this_config)

    @staticmethod
    def test_bad_config() -> None:
        """
        Tests trying to load a config block with an invalid kind set.

        :return:
        """
        # Build a bad config and give it to the bot
        this_config = ConfigBlock()  # type: ignore
        this_config["kind"] = "NULL"
        with pytest.raises(ValueError):  # @UndefinedVariable
            _ = load_component(this_config)


class TestLoaderConfigureBot(BaseTestClassWithConfig[RedditBotPasswordIOConfig]):
    """
    Tests loading an example reddit based bot.
    """

    config_file: str

    def test_config_type(self) -> None:
        """
        Tests that the RedditPasswordIOConfig has the correct api after load.

        :return:
        """
        config_path = self.get_example_path(
            CONFIG_YAML_NAME, file_path=__file__, folder_prefix="reddit_"
        )

        with open(config_path, "r", encoding="utf-8") as config_file:
            config = list(yaml.load_all(config_file, Loader=yaml.CSafeLoader))

        assert len(config) > 1
        assert any(
            obj for obj in config if obj["implementation"] == "mewbot.api.v1.Behaviour"
        )
