import logging

# Настройка логгера
logging.basicConfig(filename='logfile.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

def log_variables_and_exceptions():
    try:
        # Логирование переменных
        a = 10
        b = 'Hello, world!'
        logging.debug(f'Значение переменной 1: {a}')
        logging.debug(f'Значение переменной 2: {b}')
        
        # Имитация исключения
        result = a / 0  # Деление на ноль для вызова ZeroDivisionError
    except Exception as e:
        # Логирование исключений
        logging.error(f'Произошло исключение: {e}', exc_info=True)

# Вызов функции для логирования
log_variables_and_exceptions()