MAX_CHAR = 26

# function to return true if
# strings have common substring
# and no if strings have no
# common substring
def twoStrings(s1, s2, str3, str4):

    # vector for storing character
    # occurrences
    v = [0] * (MAX_CHAR)

    # increment vector index for every
    # character of str1
    for i in range(len(s1)):
        v[ord(s1[i]) - ord("a")] = True

    # checking common substring
    # of str2 in str1
    for i in range(len(s2)):
        if v[ord(s2[i]) - ord("a")]:
            return True

    return False


# Driver Code
if __name__ == "__main__":
    str1 = "hello"
    str2 = "world"
    if twoStrings(str1, str2, str3, str4):
        print("Yes")
    else:
        print("No")

