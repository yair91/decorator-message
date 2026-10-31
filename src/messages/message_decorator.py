from .message import Message


class MessageDecorator(Message):
    def __init__(self, wrapped: Message):
        self.wrapped = wrapped

    def render(self) -> str:
        return self.wrapped.render()
