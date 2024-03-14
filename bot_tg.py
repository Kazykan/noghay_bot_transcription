import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, BotCommand
from aiogram.utils.markdown import hbold
from aiogram.fsm.storage.memory import MemoryStorage

from bot.handlers import common, translit_handler, info
from conf import TELEGRAM_TOKEN

logger = logging.getLogger(__name__)


async def set_commands(bot: Bot):
    """Кнопки меню постоянные"""
    commands = [
        BotCommand(command="/start", description="Start"),
        BotCommand(command="info", description="Описание бота (Bot açıklaması)"),
    ]
    await bot.set_my_commands(commands)


my_bot = Bot(token=TELEGRAM_TOKEN, parse_mode="HTML")


async def main(bot):

    logging.basicConfig(
        level=logging.WARNING,
        format="%(filename)s[LINE:%(lineno)d]# %(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")

    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(common.router)
    dp.include_router(info.router)
    dp.include_router(translit_handler.router)

    await set_commands(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    try:
        asyncio.run(main(bot=my_bot))
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")