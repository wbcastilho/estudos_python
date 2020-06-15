# Logging
import logging

logging.basicConfig(
    filename='info.log',
    level=logging.DEBUG,
    format='%(levelname)s %(asctime)s: %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)

logger = logging.StreamHandler()
logging.getLogger('').addHandler(logger)

logging.debug('Isso é uma mensagem nível debug')
logging.info('Isso é uma mensagem nível info')
logging.warning('Isso é uma mensagem nível warning')
logging.error('Isso é uma mensagem nível error')
logging.critical('Isso é uma mensagem nível critical')
