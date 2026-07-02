def validPalCheck(s):
    left = 0
    right = len(s) - 1

    while left < right: # TC => O(n) || SC => O(1)
        if s[left].isalnum() and s[right].isalnum():
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        else:
            if not s[left].isalnum():
                left += 1
            else:
                right -= 1
    return True



x = "A man, a plan, a canal: Panama"
print(validPalCheck(x))
