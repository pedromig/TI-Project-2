class BurrowsWheelerEncoder:

    def get_permutations(self, string):

        ret = list()
        for i in range(len(string)):
            ret = ret + [string[i:] + string[:i]]
        return ret

    def encode(self, string):
        index = 0

        perms = self.get_permutations(string)
        perms.sort()

        last_column = ""

        for line in perms:
            last_column += line[len(line) - 1]

        for index in range(0, len(perms)):
            if perms[index] == string:
                break

        return index, last_column


class BurrowsWheelerDecoder:

    def get_indexes(self, str, sorted):

        used_pos = dict()
        indexes = []
        for i in range(0, len(str)):
            for j in range(0, len(sorted)):
                if sorted[j] == str[i] and (not used_pos.get(j, 0)):
                    used_pos[j] = True
                    indexes = indexes + [j]
                    break
        return indexes

    def decode(self, str, index):

        sorted = [str[i] for i in range(0, len(str))]
        sorted.sort()
        indexes = self.get_indexes(str, sorted)
        ret = ''
        T = index
        for i in range(0, len(str)):
            char = str[T]
            ret = char + ret
            T = indexes[T]
        return ret


if __name__ == "__main__":
    str = "Hello World"

    # encode
    encoder = BurrowsWheelerEncoder()
    (index, last_column) = encoder.encode(str)
    print('encoded:', index, last_column)

    '''# decode
    decoder = BurrowsWheelerDecoder()
    decoded = decoder.decode(last_column, index)
    print('decoded:', decoded)'''
