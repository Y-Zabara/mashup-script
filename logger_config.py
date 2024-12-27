import logging
import config

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(config.LOG_FILE, mode='a', encoding='utf-8')
    ]
)

logger = logging.getLogger("my_project")
