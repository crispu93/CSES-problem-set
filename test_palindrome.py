def solution(inputString):
    """Check if the input string is palindrome
    """
    isPalindrome = True
    for i in range(len(inputString)//2):
        if inputString[i] != inputString[len(inputString) - i - 1]:
            isPalindrome = False
            break
    return isPalindrome
