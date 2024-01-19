import random

def generate_and_sum_random_list(length):
    """
    Generates a list of random integers and returns their sum.

    Parameters:
    - length (int): The length of the random list.

    Returns:
    - int: The sum of the random list.
    """
    random_list = [random.randint(1, 100) for _ in range(length)]
    list_sum = sum(random_list)
    return list_sum

# Example usage
random_list_length = 5
result = generate_and_sum_random_list(random_list_length)
print(f"Random list sum: {result}")
