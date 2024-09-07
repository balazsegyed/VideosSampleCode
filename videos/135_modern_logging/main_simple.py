import atexit
import json
import logging.config
import logging.handlers
import pathlib

# This logger works under python 3.10+
logger = logging.getLogger(__name__)  # __name__ is a common choice


def setup_logging():
    config_file = pathlib.Path("logging_configs/standard_file.json")
    # config_file = pathlib.Path("logging_configs/json_file.json")
    with open(config_file) as f_in:
        config = json.load(f_in)

    logging.config.dictConfig(config)


def main():
    setup_logging()
    logging.basicConfig(level="INFO")
    logger.debug("debug message", extra={"x": "hello"})
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("exception message")


if __name__ == "__main__":
    main()
