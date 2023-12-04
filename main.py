import asyncio
import logging
import sys

import bot_start
from handlers import inline, keyboard, echo, notes
from loader import dp, bot


async def main() -> None:
    dp.include_routers(
        bot_start.start_router,
        inline.inline_router,
        keyboard.kb_router,
        notes.notes_router,
        echo.echo_router,
    )
    await dp.start_polling(bot)

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())