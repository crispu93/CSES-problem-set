def read_input() -> int:
    """Does what it says
    """
    number = int(input().strip())
    return number


def trailing_zeros(input_number: int) -> int:
    """Computes the trailing zeroes the factorial of input_number
    """
    # Counts the number of times 5 is a factor
    power_of_five = 5
    number_of_fives = 0
    while power_of_five <= input_number:
        number_of_fives += input_number // power_of_five
        power_of_five *= 5
    return number_of_fives


def main() -> None:
    """Prints the number of trailing zeros in the the inputs number factorial
    """
    input_number = read_input()
    result = trailing_zeros(input_number)
    print(result)


if __name__ == '__main__':
    main()
