"""
Classes for sending outputs back to reddit.
"""

from __future__ import annotations

from typing import Set, Type

from mewbot.api.v1 import Output, OutputEvent


class RedditOutput(Output):
    """
    Talk back to reddit.
    """

    @staticmethod
    def consumes_outputs() -> Set[Type[OutputEvent]]:
        """
        This is a placeholder - this Output does not consume anything.

        :return:
        """
        return set()

    async def output(self, event: OutputEvent) -> bool:
        """
        Does the work of transmitting the event to the world.

        :param event:
        :return:
        """
        raise NotImplementedError(
            f"Output not current supported {event} will not be transmitted!"
        )
