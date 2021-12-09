from typing import List, Dict


def read_inputs() -> List[str]:
    """Does what it says
    """
    letters: str = input()
    return letters


def palindrome_reorder(letters: List[str]) -> None:
    """Reorders a list of letters (if possible) in order to convert
    it into a palindrome

    Args:
        letters: unordered letters
    """
    dict_letters: Dict[str, int] = {}

    # Compute frequencies of each letter
    for c in letters:
        if c in dict_letters.keys():
            dict_letters[c] += 1
        else:
            dict_letters[c] = 1

    # Check all frequencies are even or just one of them is odd
    find_odd = False
    odd_letter: str = "" 
    odd_value: int = 1
    for k, v in dict_letters.items():
        if v % 2 == 1:
            if find_odd is True:
                print("NO SOLUTION")
                return
            else:
                find_odd = True
                odd_letter = k
                odd_value = v

    # Build the string
    palindrome: List[str] = []
    for key, value in dict_letters.items():
        if key == odd_letter:
            continue
        else:
            palindrome.append((value // 2) * (key))

    string_palindrome = palindrome[:]
    palindrome.reverse()
    string_palindrome = string_palindrome + [odd_letter*odd_value] + palindrome
    print(''.join(string_palindrome))


def main() -> None:
    """Read a list of letters and print a palindrome if possible
    """
    letters: List[str] = read_inputs()
    palindrome_reorder(letters)


if __name__ == '__main__':
    main()
