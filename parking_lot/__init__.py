from enum import Enum


class PaymentStatus(Enum):
    COMPLETED = 1
    FAILED = 2
    PENDING = 3
    UNPAID = 4
    REFUNDED = 5


class AccountStatus(Enum):
    ACTIVE = 1
    CLOSED = 2
    CANCELED = 3
    BLACKLISTED = 4
    NONE = 5


class Person:
    def __int__(self, name, address, phone, email):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__email = email





if __name__ == '__main__':
    print("Sharan")
