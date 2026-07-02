def generate(index , subset , arr):
    #base condition
    if index == len(arr):
        print(subset)
        return
    subset.append(arr[index]) # choosing my arr[index]
    generate(index + 1 , subset , arr)
    subset.pop() # backracking and moving without choosing
    generate(index + 1 , subset , arr)


x = [1 , 2, 3]
generate(0 , [] , x)

