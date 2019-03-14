import logging
Log_FORMAT='%(asctime)s-------%(levelname)s________%(message)s'
DATE_FORMAT='%m/%d/%Y %H:%M:%S:%p'
logging.basicConfig(filename='my_log',level=logging.DEBUG,format=Log_FORMAT,datefmt=DATE_FORMAT)
logging.debug(' This is a debug log.')
logging.info('this is a info log')
logging.warning('This is a warning log')
logging.error('This is a error log')
logging.critical('This is a critical log')

logging.log(logging.DEBUG,'this is a debug log')
logging.log(logging.INFO,'this is a info log')
logging.log(logging.WARNING,'this is a warning log')
logging.log(logging.ERROR,'this is a error log')
logging.log(logging.CRITICAL,'this is a critical log')
