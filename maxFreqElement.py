arr = [1 , 2, 2 , 2, 1, 1]

freq = {}

for i in range(0 , len(arr)):
    if arr[i] in freq:
        freq[arr[i]] = freq[arr[i]] + 1
    else:
        freq[arr[i]] = 1

print(freq)

# in my home
maxFreq = -1
maxFreqElement = -1
for i in freq.keys():
    if maxFreq < freq[i]:
        maxFreq = freq[i]
        maxFreqElement = i
    elif maxFreq == freq[i]:
        if maxFreqElement < i:
            maxFreqElement = i


print(maxFreqElement)

