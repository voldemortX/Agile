import logging
import logging.handlers
from concurrent_log_handler import ConcurrentRotatingFileHandler

log_path = "./log"


def init_logger(app):
    # 128MB "multi-processable" log file(info)
    access = ConcurrentRotatingFileHandler(log_path+"/access.log", "a", 128*1024*1024, 7, encoding="utf-8")
    access.setLevel(logging.INFO)
    access.suffix = "%Y-%m-%d.log"
    access.setFormatter(logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(funcName)s: %(message)s'
    ))

    # 128MB "multi-processable" log file(error)
    error = ConcurrentRotatingFileHandler(log_path + "/error.log", "a", 128 * 1024 * 1024, 7, encoding="utf-8")
    error.setLevel(logging.ERROR)
    error.suffix = "%Y-%m-%d.log"
    error.setFormatter(logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(funcName)s: %(message)s'
    ))

    app.logger.addHandler(access)
    app.logger.addHandler(error)
    app.logger.setLevel(logging.INFO)
