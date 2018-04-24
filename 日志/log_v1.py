import logging

#日志格式
LOG_FORMAT = "%(asctime)s:%(levelname)s:%(message)s"

#配置日志
logging.basicConfig(filename='test.log', level=logging.DEBUG, filemode='w', format=LOG_FORMAT)

#写日志
logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")

logging.log(logging.DEBUG, 'This is a error log.')
logging.log(logging.INFO, 'This is a error log.')
logging.log(logging.WARNING, 'This is a error log.')
logging.log(logging.ERROR, 'This is a error log.')
logging.log(logging.CRITICAL, 'This is a error log.')