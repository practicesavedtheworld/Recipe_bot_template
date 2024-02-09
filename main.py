import asyncio
import logging
import pathlib

from bot.handlers.handlers import router
from bot.loader import bot, dp
from utils.logger import create_logger

entrypoint_logger = create_logger(
    loger_name="entrypoint logger",
    logger_level=logging.DEBUG,
    file_info=pathlib.Path(__file__).name,
)


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    entrypoint_logger.debug("Starting bot...")
    asyncio.run(main())
    entrypoint_logger.debug("Bot stopped")
