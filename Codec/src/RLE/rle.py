def encodeRLE(data):
    count = 1
    prev = ''
    lst = []
    for character in data:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    else:
        entry = (character, count)
        lst.append(entry)
        return lst


def toString(data):
    string = ""
    for t in data:
        if t[1] > 3:
            string += "@" + str(t[1]) + t[0]
        else:
            string += t[1] * t[0]

    return string


def decodeRLE(string):
    res = ""
    for index in range(len(string)):
        if (string[index] == '@'):
            res += int(string[index + 1]) * string[index + 2]
        elif (string[index] != '@' and string[index - 1] != '@' and string[index - 2] != '@'):
            res += string[index]
    return res


if __name__ == "__main__":
    value = encodeRLE("aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa")
    aux = toString(value)

    print("Encoded value is {}".format(aux))
    print("Decoded value is {}".format(decodeRLE(value)))
