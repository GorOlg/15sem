"""Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
   операцией, даже ошибочной
✔ Любое действие выводит сумму денег"""

import decimal
import logging

py_logger = logging.getLogger(__name__)
py_logger.setLevel(logging.INFO)

# настройка обработчика и форматировщика в соответствии с нашими нуждами
py_handler = logging.FileHandler(f"my_journal.log", mode='w', encoding='utf-8')
py_formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

# добавление форматировщика к обработчику
py_handler.setFormatter(py_formatter)
# добавление обработчика к логгеру
py_logger.addHandler(py_handler)

py_logger.info(f"Тестирование пользовательского регистратора для модуля {__name__}!!!")

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(0.015)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(0.03)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(0.1)
RICHNESS_SUM = decimal.Decimal(5_000_000)

bank_account = decimal.Decimal(0)
count = 0


def deposit(amount):
    """Пополнение счета"""
    global bank_account, count
    if amount % MULTIPLICITY != 0:
        py_logger.warning(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
        return f'Сумма должна быть кратной {MULTIPLICITY} у.е.'
    else:
        count += 1
        if count % COUNTER4PERCENTAGES == 0:
            bank_account += amount * PERCENT_DEPOSIT
            py_logger.info(f'Начислен бонус в 3% - {(amount * PERCENT_DEPOSIT):.2f} Баланс равен {bank_account:.2f}')
            print(f'Начислен бонус в 3% - {(amount * PERCENT_DEPOSIT):.2f}')
        bank_account += amount
        if bank_account > RICHNESS_SUM:
            percent = bank_account * RICHNESS_PERCENT
            bank_account -= percent
            py_logger.info(f'Снят налог на богатство 10% - {percent:.2f} Баланс равен {bank_account:.2f}')
            print(f'Снят налог на богатство 10% - {percent:.2f}')
        py_logger.info(f'Пополнение карты на {amount:.2f}у.е. Баланс равен {bank_account:.2f}')
        return f'Пополнение карты на {amount:.2f}у.е.'


def withdraw(amount):
    """Снятие денег"""
    global bank_account, count
    if amount % MULTIPLICITY != 0:
        py_logger.warning(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
        return f'Сумма должна быть кратной {MULTIPLICITY} у.е.'
    else:
        count += 1
        if count % COUNTER4PERCENTAGES == 0:
            bank_account += amount * PERCENT_DEPOSIT
            py_logger.info(f'Начислен бонус в 3% - {(amount * PERCENT_DEPOSIT):.2f} Баланс равен {bank_account:.2f}')
            print(f'Начислен бонус в 3% - {(amount * PERCENT_DEPOSIT):.2f}')
        if amount * PERCENT_REMOVAL < MIN_REMOVAL:
            percent = MIN_REMOVAL
        elif amount * PERCENT_REMOVAL > MAX_REMOVAL:
            percent = MAX_REMOVAL
        else:
            percent = PERCENT_REMOVAL * amount
        if bank_account >= amount + percent:
            bank_account = bank_account - amount - percent
            py_logger.info(f'Снятие с карты {amount}у.е. Процент за снятие {percent:.2f}у.е.'
                           f'Баланс равен {bank_account:.2f}')
            return f'Снятие с карты {amount} у.е. Процент за снятие {percent:.2f} у.е.'
        else:
            py_logger.warning(f'Недостаточно средств. Сумма с комиссией {amount + percent:.2f}у.е.'
                              f'На карте {bank_account:.2f}у.е')
            return f'Недостаточно средств. Сумма с комиссией {amount + percent:.2f} у.е.На карте {bank_account:.2f} у.е'


def main():
    """Ввод данных"""
    global bank_account
    while True:
        print(f'На вашем счету {bank_account:.2f} у.е.')
        print('Введите от 1 до 3')
        print('1 - Пополнить счет')
        print('2 - Снять со счета')
        print('3 - выйти')
        match input():
            case '1':
                print(deposit(int(input('Введите сумму пополнения счёта:\n'))))
            case '2':
                print(withdraw(int(input('Сколько Вы хотите снять?:\n'))))
            case '3':
                break
            case _:
                py_logger.warning('Введено не верное значение!')
                print('Введено не верное значение!')


if __name__ == '__main__':
    try:
        main()
    except SyntaxError as er:
        py_logger.critical(f'Синтаксическая ошибка {er}')
        print(er)