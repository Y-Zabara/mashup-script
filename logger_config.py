import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("app.log", mode='a', encoding='utf-8')
    ]
)

logger = logging.getLogger("my_project")
