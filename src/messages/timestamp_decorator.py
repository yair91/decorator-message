from datetime import datetime
from typing import Callable

from .message import Message
from .message_decorator import MessageDecorator


class TimestampDecorator(MessageDecorator):
    def __init__(self, wrapped: Message, clock: Callable[[], datetime] = datetime.now):
        super().__init__(wrapped)
        self.clock = clock

    def render(self) -> str:
        stamp = self.clock().strftime("%Y-%m-%d %H:%M")
        return f"[{stamp}] {self.wrapped.render()}"
