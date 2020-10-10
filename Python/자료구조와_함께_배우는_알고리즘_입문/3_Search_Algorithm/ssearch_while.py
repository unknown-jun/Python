# linear search algorithm using with while loop

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """a"""
    i = 0

    while True:
        if i == len(a):
            return -1    # Return -1, because fail to search
        if a[i] == key:
            return i     # Search succeeded and returned the index of the currently scanned array
        i += 1

if __name__ == '__main__':
    num = int(input('Enter the number of element: '))    # Entered the num value
    x = [None] * num                                     # Creating the array that the number of element is 'num'

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('Enter the value that you want to search: '))  # Received a key 'ky' to search for

    idx = seq_search(x, ky)                                       # Search element same as 'ky' within 'x'

    if idx == -1:
        print("The element doesn't exist in the list")
    else:
        print(f'The searching value is in x[{idx}]')