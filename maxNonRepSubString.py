s = "abcacdefab"
# longest non repeating substring
store = set() # TC => O(n) || SC = O(n)
left = 0
maxLength = 0
for right in range( 0  , len(s)): #O(n)
    while s[right] in store:
        store.remove(s[left])
        left += 1
    print(s[left : right + 1])
    store.add(s[right])
    maxLength = max(maxLength , right - left + 1)

print(maxLength)
