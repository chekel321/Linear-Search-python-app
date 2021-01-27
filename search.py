"""
File: search.py
Defines function for linearSearch.
Best-case:
Worst-case:
Average-case:
"""

def linearSearch(target, lyst):
    """Returns the position of the target item if found, or -1 otherwise."""
    index = 0
    while index < len(lyst):
        if target == lyst[index]:
            return index
        index += 1

    return -1

   
def main():
    """Tests with three lists."""
    print(linearSearch(3, [3, 5, 7, 9, 10]))
    print(linearSearch(3, [0, 1, 2]))
    # Will stop at second position.
    print(linearSearch(3, [0, 2, 4, 6]))
   
if __name__ == "__main__":
    main()
