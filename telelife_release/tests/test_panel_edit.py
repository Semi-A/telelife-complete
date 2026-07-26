from __future__ import annotations
from unittest.mock import AsyncMock, patch
import pytest
from telegram.error import BadRequest
from apps.telelife_bot.handlers.common import send_panel

@pytest.mark.asyncio
async def test_identical_edit_is_a_successful_noop() -> None:
    message = AsyncMock()
    message.edit_text.side_effect = BadRequest("Message is not modified: same content")
    with patch("apps.telelife_bot.handlers.common.schedule_cleanup") as cleanup:
        await send_panel(AsyncMock(), message, "same", None, "profile", edit=True)
    cleanup.assert_called_once()

@pytest.mark.asyncio
async def test_other_bad_request_is_not_hidden() -> None:
    message = AsyncMock()
    message.edit_text.side_effect = BadRequest("Message to edit not found")
    with pytest.raises(BadRequest, match="not found"):
        await send_panel(AsyncMock(), message, "text", None, "profile", edit=True)