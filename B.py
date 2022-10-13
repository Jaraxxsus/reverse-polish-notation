from typing import Union, Tuple


class Stack:
    def __init__(self):
        self.items =  []

    def is_math_operator(self, symbol: str) -> bool:
        if symbol == "+" or symbol == "-" or symbol == "*" or symbol == "/":
            return  True
        return False

    def _get_operands(self) -> Tuple:
        x: int = self.items.pop()
        y: int = self.items.pop()
        return x,y

    def calc(self, symbol: str) -> int:
        if symbol == "+":
            x,y = self._get_operands()
            return x + y
        if symbol == "-":
            x, y = self._get_operands()
            return y - x
        if symbol == "*":
            x, y = self._get_operands()
            return x * y
        if symbol == "/":
            x, y = self._get_operands()
            return y // x

    def push(self, symbol: Union[str, int]) -> None:
        if self.is_math_operator(symbol):
            self.items.append(self.calc(symbol))
        else:
            self.items.append(symbol)

    def answer(self):
        if len(self.items) > 1:
            return self.items.pop()
        return self.items[0]


if __name__ == "__main__":
    s = Stack()
    data: list = input().split()
    for i in data:
        if not s.is_math_operator(i):
            s.push(int(i))
        else:
            s.push(i)
    print(s.answer())