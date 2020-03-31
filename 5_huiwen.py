def isPalindrome(self, x: int) -> bool:
    if '-' in str(x):
        return False
    else:
        if str(x)[::-1] == str(x):
            return True
        else:
            return False

