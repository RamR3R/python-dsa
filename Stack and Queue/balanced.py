s = "()"

stack = []
valid = True
for i in range(0 , len(s)):
    if s[i] == "(":
        stack.append("(")
    else:
        if len(stack) == 0:
            valid = False
        else:
            stack.pop()

if len(stack) == 0 and valid:
    print("Balanced String")
else:
    print("Not a balanced Paranthesis")