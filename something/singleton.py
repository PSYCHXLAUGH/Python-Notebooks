#!/usr/bin/env python3

# an implementation of a class that, when instantiated, will have the same address in memory

from typing import Any

class NoSingleton: # for example
    pass

class Singleton:

    _instance: object = None # check

    def __new__(cls, *args, **kwargs) -> object:
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance


    def method(self) -> None:
        pass



print(Singleton() is Singleton()) # True
print(NoSingleton() is NoSingleton()) # False
