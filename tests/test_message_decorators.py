from datetime import datetime

from messages.plain_message import PlainMessage
from messages.timestamp_decorator import TimestampDecorator
from messages.urgent_decorator import UrgentDecorator


def fixed_clock():
    return datetime(2026, 10, 30, 9, 15)


def test_stacked_decorators_wrap_in_order():
    message = PlainMessage("Deploy complete")

    timestamp_outside = TimestampDecorator(UrgentDecorator(message), clock=fixed_clock)
    urgent_outside = UrgentDecorator(TimestampDecorator(message, clock=fixed_clock))

    assert timestamp_outside.render() == "[2026-10-30 09:15] [URGENT] Deploy complete"
    assert urgent_outside.render() == "[URGENT] [2026-10-30 09:15] Deploy complete"
