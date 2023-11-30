# SPDX-FileCopyrightText: 2023 Mewbot Developers <mewbot@quicksilver.london>
#
# SPDX-License-Identifier: BSD-2-Clause

"""
Methods to support examples for mewbot_io_client_for_reddit.
"""


from typing import Any, AsyncIterable, Dict, Set, Type

from mewbot.api.v1 import Action, Trigger
from mewbot.core import InputEvent, OutputEvent

from mewbot.io.client_for_reddit.events import RedditInputEvent


class RedditInputTrigger(Trigger):
    """
    Nothing fancy - just fires whenever there is a RedditInputEvent.
    """

    @staticmethod
    def consumes_inputs() -> Set[Type[InputEvent]]:
        """
        Responds to every RedditInputEvent.

        :return:
        """
        return {RedditInputEvent}

    def matches(self, event: InputEvent) -> bool:
        """
        If the event is a RedditInputEvent it triggers - otherwise it will not.

        :param event:
        :return:
        """
        if not isinstance(event, RedditInputEvent):
            return False

        return True


class RedditPrintAction(Action):
    """
    Print every RedditInputEvent.
    """

    @staticmethod
    def consumes_inputs() -> Set[Type[InputEvent]]:
        """
        Can consume all inputs.
        """
        return {InputEvent}

    @staticmethod
    def produces_outputs() -> Set[Type[OutputEvent]]:
        """
        Produces no outputs.
        """
        return set()

    async def act(self, event: InputEvent, state: Dict[str, Any]) -> AsyncIterable[None]:
        """
        Acts on events pulled from the queue.

        Consumes RSSInputEvents and prints some of their properties.
        """
        if not isinstance(event, RedditInputEvent):
            print(f"Unexpected event {event}")
            return

        reddit_output_str = []
        reddit_output_str.append(f"New event ... event - \n{event}")

        print("\n".join(reddit_output_str))
        yield None
