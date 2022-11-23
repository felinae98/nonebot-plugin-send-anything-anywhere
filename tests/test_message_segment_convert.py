import typing
from typing import Type

import pytest
from nonebug import App

if typing.TYPE_CHECKING:
    from nonebot_plugin_send_anything_anywhere.utils import (
        SupportedAdapters,
        MessageSegmentFactory,
    )


@pytest.fixture
def dummy_factory(app: App):
    from nonebot_plugin_send_anything_anywhere.utils import MessageSegmentFactory

    class Test(MessageSegmentFactory):
        text: str

        def __init__(self, text: str) -> None:
            self.text = text
            super().__init__()

    return Test


@pytest.fixture
def onebot_v11(app: App):
    from nonebot_plugin_send_anything_anywhere.utils import SupportedAdapters

    return SupportedAdapters.onebot_v11


async def test_sync_without_bot(
    dummy_factory: "Type[MessageSegmentFactory]", onebot_v11: "SupportedAdapters"
):
    from nonebot.adapters.onebot.v11.message import MessageSegment

    from nonebot_plugin_send_anything_anywhere.utils import register_ms_adapter

    @register_ms_adapter(onebot_v11, dummy_factory)
    def _text(t):
        return MessageSegment.text("314159")


async def test_sync_with_bot(
    dummy_factory: "Type[MessageSegmentFactory]", onebot_v11: "SupportedAdapters"
):
    from nonebot.adapters.onebot.v11.message import MessageSegment

    from nonebot_plugin_send_anything_anywhere.utils import register_ms_adapter

    @register_ms_adapter(onebot_v11, dummy_factory)
    def _text(t, bot):
        return MessageSegment.text("314159")


async def test_async_without_bot(
    dummy_factory: "Type[MessageSegmentFactory]", onebot_v11: "SupportedAdapters"
):
    from nonebot.adapters.onebot.v11.message import MessageSegment

    from nonebot_plugin_send_anything_anywhere.utils import register_ms_adapter

    @register_ms_adapter(onebot_v11, dummy_factory)
    async def _text(t):
        return MessageSegment.text("314159")


async def test_async_with_bot(
    dummy_factory: "Type[MessageSegmentFactory]", onebot_v11: "SupportedAdapters"
):
    from nonebot.adapters.onebot.v11.message import MessageSegment

    from nonebot_plugin_send_anything_anywhere.utils import register_ms_adapter

    @register_ms_adapter(onebot_v11, dummy_factory)
    async def _text(t, bot):
        return MessageSegment.text("314159")
