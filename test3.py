def merge(string1, string2):
    if len(string1 + string2) == 0:
        return ''
    elif (len(string1) > 0 and len(string2) == 0) or (len(string1) == 0 and len(string2) > 0):
        return string1 + string2
    else:
        if string1[0] < string2[0]:
            return string1[0] + merge(string1[1:], string2)
        elif string2[0] < string1[0]:
            return string2[0] + merge(string1, string2[1:])
        else: # if they're equal
            return string1[0] + string2[0] + \
                merge(string1[1:], string2[1:])


def main():
    string1 = "domi"
    string2 = "nic"
    

    print("First string: ", string1)
    print("Second string: ", string2)
    print("Result : ", end=' ')
    print(merge("domi", "nic"))


main()