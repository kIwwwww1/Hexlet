import sys

from loguru import logger


class InterceptLogger:
    @staticmethod
    def setup():
        logger.remove()
        logger.add(
            sys.stdout,
            colorize=True,
            format="<level>{level: <8}</level> <green>{time:HH:mm:ss}</green> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>",
            level="DEBUG"
        )

        return logger

log = InterceptLogger.setup()
