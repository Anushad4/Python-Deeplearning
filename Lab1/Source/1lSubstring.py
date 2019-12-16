# function to find the longest substring
def findLongestSubstring(string):
    n = len(string)
    st = 0
    maxlen = 0
    start = 0
    temp = {}
    # Last occurrence of first
    # character is index 0
    temp[string[0]] = 0

    for i in range(1, n):
        if string[i] not in temp:
            temp[string[i]] = i

        else:
            if temp[string[i]] >= st:
                currlen = i - st
                if maxlen < currlen:
                    maxlen = currlen
                    start = st
                st = temp[string[i]] + 1
            temp[string[i]] = i
    if maxlen < i - st:
        maxlen = i - st
        start = st
    return string[start: start + maxlen]

if __name__ == "__main__":
    # taking input from user
    string = input('Enter the string:')
    # call function to find the longest substring and pass the input string
    tup = (findLongestSubstring(string), len(list(findLongestSubstring(string))))
    print(tup)
