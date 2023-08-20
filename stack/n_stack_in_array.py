"""ADS_CSCSC01/n_stack_in_array.py
Lab-1:

1.2. Implement N stacks in an Array
"""

from typing import List, Union

class NStacks:

    def __init__(self, num_stacks: int, total_size: int) -> None:

        self.num_stacks: int = num_stacks
        self.total_size: int = total_size
        self.stack_data: List[int] = [None] * total_size
        self.stack_sizes: List[int] = [0] * num_stacks
        self.stack_pointer: List[int] = [-1] * num_stacks
        self.segment_size: int = total_size // num_stacks


    def is_full(self, stack_num: int) -> bool:
        return self.stack_sizes[stack_num] == self.segment_size


    def is_empty(self, stack_num: int) -> bool:
        return self.stack_sizes[stack_num] == 0


    def push(self, stack_num: int, value: int) -> Union[None, Exception]:

        if self.is_full(stack_num):
            raise Exception(f"Stack {stack_num} is full...")

        self.stack_pointer[stack_num] += 1
        self.stack_sizes[stack_num] += 1
        index = self.stack_pointer[stack_num] + stack_num * self.segment_size
        self.stack_data[index] = value


    def pop(self, stack_num: int) -> Union[int, Exception]:

        if self.is_empty(stack_num):
            raise Exception(f"Stack {stack_num} is empty...")

        index = self.stack_pointer[stack_num] + stack_num * self.segment_size
        value = self.stack_data[index]
        self.stack_pointer[stack_num] -= 1
        self.stack_sizes[stack_num] -= 1
        return value


    def peek(self, stack_num: int) -> Union[int, Exception]:

        if self.is_empty(stack_num):
            raise Exception(f"Stack {stack_num} is empty...")

        index = self.stack_pointer[stack_num] + stack_num * self.segment_size
        return self.stack_data[index]


    def print_list(self) -> List[Union[None, int]]:

        return self.stack_data


if __name__ == '__main__':
    num_stacks = 3
    total_size = 9
    n_stacks = NStacks(num_stacks, total_size)

    n_stacks.push(0, 10)
    n_stacks.push(0, 20)
    n_stacks.push(1, 30)
    n_stacks.push(2, 40)

    print("n_stacks.peek(0): ", n_stacks.peek(0))
    print("n_stacks.peek(1): ", n_stacks.peek(1))
    print("n_stacks.peek(2): ", n_stacks.peek(2))

    print("Our Array is: ", n_stacks.print_list())

    print(n_stacks.pop(0))
    print(n_stacks.pop(1))
    print(n_stacks.pop(2))