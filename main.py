from typing import List

# Skeleton code for even_list
def even_list(int_list: List[int]) -> List[int]:
    """
    Determines if a number is even and return an even list.
    Args:
        int_list: A list of integer.
    Returns:
        A list of even integers.
    """
    even_list = []
    for num in int_list:
        if num % 2 == 0:
            even_list.append(num)
    
    return even_list

# Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    """
    Computes the sum of the squares of all even numbers in a list.
    Args:
        even_int_list: A list of even integers.
    Returns:
        The sum of the squares of all even numbers in the list.
    """
    # TODO: Implement sum_of_squares_of_even
    pass
