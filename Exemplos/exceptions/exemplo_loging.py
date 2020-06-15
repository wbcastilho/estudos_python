import logging

logging.basicConfig(
    filename='info.log',
    level=logging.DEBUG,
    format='%(levelname)s %(asctime)s: %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)

logger = logging.StreamHandler()
logging.getLogger('').addHandler(logger)

try:
    ano_atual = int(input('Qual é o ano atual?'))
except ValueError:
    logging.warning('Você deve digitar um número.')

try:
    print(5/0)
except ZeroDivisionError:
    logging.warning('Não é possível divir por 0.')

try:
    print(5/0)
except:
    logging.warning('Ocorreu um erro')
finally:
    logging.info('Usuário x realizou cálculos nos sistema.')