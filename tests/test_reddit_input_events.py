"""
Tests loading an example reddit config.
"""

# pylint: disable=duplicate-code
# Repetition for emphasis is occasionally desirable in tests

from __future__ import annotations

import pytest
from mewbot.core import ConfigBlock
from mewbot.loader import load_component


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


# class TestLoaderConfigureBot(BaseTestClassWithConfig[RedditPasswordIOConfig]):
#     """
#     Tests loading an example reddit based bot.
#     """
#
#     config_file: str
#
#     def test_config_type(self) -> None:
#         """
#         Tests that the RedditPasswordIOConfig has the correct api after load.
#
#         :return:
#         """
#         config_path = self.get_example_path(
#             CONFIG_YAML_NAME, file_path=__file__, folder_prefix="reddit_"
#         )
#
#         with open(config_path, "r", encoding="utf-8") as config_file:
#             config = list(yaml.load_all(config_file, Loader=yaml.CSafeLoader))
#
#         assert len(config) > 1
#         assert any(
#             obj for obj in config if obj["implementation"] == "mewbot.api.v1.Behaviour"
#         )
#
#     def test_working(self) -> None:
#         """
#         Tests we can load the bot from the given yaml.
#
#         :return:
#         """
#         config_path = self.get_example_path(
#             CONFIG_YAML_NAME, file_path=__file__, folder_prefix="reddit_"
#         )
#
#         with open(config_path, "r", encoding="utf-8") as config_file:
#             bot = configure_bot("bot", config_file)
#
#         assert isinstance(bot, Bot)


# # Tester for mewbot.loader.load_component
# class TestLoaderRSSInput(BaseTestClassWithConfig[RedditPasswordIO]):
#     config_file: str = CONFIG_YAML
#     implementation: Type[RedditPasswordIO] = RedditPasswordIO
#
#     # Test this working
#     def test_working(self) -> None:
#         component = load_component(self.config)
#         assert isinstance(component, IOConfig)
#
#     # Test that the loading is accurate
#     def test_loading_component_type(self) -> None:
#         assert isinstance(self.component, RedditPasswordIO)
#
#     def test_loading_component_config(self) -> None:
#         assert self.component.host == "localhost"
#         assert self.component.port == 12345
#
#     def test_loading_component_values(self) -> None:
#         # Protected access overridden here to inspect variables ONLY
#         assert self.component._host == "localhost"  # pylint: disable="protected-access"
#         assert self.component._port == 12345  # pylint: disable="protected-access"
#
#     # Tests that expose errors
#     def test_erroring_kind(self) -> None:
#         # Change the kind of this config, to break it
#         this_config = copy.deepcopy(self.config)
#         this_config["kind"] = "NULL"
#         with pytest.raises(ValueError):  # @UndefinedVariable
#             _ = load_component(this_config)
#
#
# # Test for mewbot.loader.load_behaviour
# class TestLoaderBehaviourHttpPost(BaseTestClassWithConfig[Behaviour]):
#     config_file: str = CONFIG_YAML
#     implementation: Type[Behaviour] = Behaviour
#
#     # Test this working
#     def test_config_type(self) -> None:
#         assert "triggers" in self.config
#         assert "conditions" in self.config
#         assert "actions" in self.config
#
#     # Test this working
#     def test_working(self) -> None:
#         component = load_behaviour(self.config)  # type: ignore
#         assert isinstance(component, Behaviour)
