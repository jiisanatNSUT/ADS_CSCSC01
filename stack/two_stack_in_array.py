"""ADS_CSCSC01\two_stack_in_array.py
Lab-1: 

1.1.Implement two stacks in an Array
"""

from typing import Union, List


class TwoStacks:

    def __init__(self, n: int) -> None:
        self.size: int = n
        self.list: List[int] = [None]*n
        self.top_left: int = -1
        self.top_right: int = self.size


    def push_left(self, x: int) -> None:

        if self.top_left < self.top_right - 1:
            self.top_left = self.top_left + 1
            self.list[self.top_left] = x

        else:
            print("Stack Overflow")
            exit(1)


    def push_right(self, x: int) -> None:

        if self.top_left < self.top_right - 1:
            self.top_right = self.top_right - 1
            self.list[self.top_right] = x

        else:
            print("Stack Overflow")
            exit(1)


    def pop_left(self) -> Union[int, None]:

        if self.top_left >= 0:
            x = self.list[self.top_left]
            self.top_left -= 1
            return x

        else:
            print("Stack Underflow")
            exit(1)


    def pop_right(self) -> Union[int, None]:

        if self.top_right < self.size:
            x = self.list[self.top_right]
            self.top_right += 1
            return x

        else:
            print("Stack Underflow")
            exit(1)


    def print_list(self) -> List[Union[int, None]]:

        return self.list


if __name__ == '__main__':
    two_stack = TwoStacks(5)
    two_stack.push_left(8)
    two_stack.push_right(11)
    two_stack.push_right(12)
    two_stack.push_right(6)

    print(two_stack.print_list())

    print(f"Pop for left stack: {two_stack.pop_left()}")
    print(f"Pop for right stack: {two_stack.pop_right()}")
