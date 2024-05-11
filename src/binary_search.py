from typing import List, Union

def binary_search(input_list: List[int], target: int) -> Union[int, None]:
    low = 0
    high = len(input_list) - 1
    while high >= low:
        mid = (high + low) // 2
        guess = input_list[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None

ORDERED_LIST = [1, 3, 4, 5, 7, 8]
TEST_ELEMENTS = [1, 2, 5, 9]

for element in TEST_ELEMENTS:
    position = binary_search(ORDERED_LIST, element)
    if position is not None:
        print(f'{element} is at position {position} in the list')
    else:
        print(f'{element} is not in the list')