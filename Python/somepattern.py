#!/usr/bin/env python3

class Test:

    __attrs = {"someshit": 1}

    def __init__(self) -> None:
        self.__dict__ = self.__attrs


print(Test().__dict__ is Test().__dict__)
