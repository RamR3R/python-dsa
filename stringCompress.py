s = "aaaaaabbccdeee"
res = "a6b2c2de3"



# using extra space with TC O(n) andCS O(n)

# store = dict()
# for i in range(0 , len(str)):
#     if str[i] in store:
#         store[str[i]] = store[str[i]] + 1
#     else:
#         store[str[i]] = 1
# pointer = 0
# while pointer < len(str):
#     res = res + f"{str[pointer]}{store[str[pointer]]}"
#     pointer += 1 
#     while pointer < len(str) and str[pointer] == str[pointer - 1]:
#         pointer += 1
# print(res)

left = 0
right = 0
count = 0
while right < len(s):
    if s[left] == s[right]:
        count += 1
        right += 1
    else:
        res = res + s[left]
        if count > 1:
             res += str(count)
        left = right
        count = 0
res = res + s[left]
if count > 1:
        res += str(count)
print(res)

# Questions
1 toogle cases
2 Remove spaces
3 Reverse Each word "I love coding" => "I evol gnidoc"
4 Longest Substring  without