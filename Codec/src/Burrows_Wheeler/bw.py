import sys


class bwt_encoder:
    """
        Transforma um bloco de caracteres em uma seqüência
        mais facilmente comprimível usando o método de
        Burrows-Wheeler, de acordo com o descrito em

    """

    def get_permutations(self, str):
        """
            Cria as permutações de um bloco que são
            necessárias ao BWT.
        """
        ret = []
        for i in range(0, len(str)):
            ret = ret + [str[i:] + str[0:i]]
        return ret

    def encode(self, str):
        """
            A "codificação" corresponde simplesmente a se
            selecionar a última coluna da matriz de
            permutações ordenadas lexicograficamente,
            além de informar a posição da cadeia original
            nesta matriz de permutações.
        """
        perms = self.get_permutations(str)
        perms.sort()
        last_column = ''
        for line in perms:
            last_column = last_column + line[len(line) - 1]
        index = 0
        for index in range(0, len(perms)):
            if perms[index] == str:
                break
        return (index, last_column)


class bwt_decoder:
    """
        Faz a transformação reversa da
        descrita em bwt_encode.
    """

    def get_indexes(self, str, sorted):
        """
            Os índices mapeiam cada símbolo da cadeia
            "codificada" com os símbolos da cadeia
            ordenada. Esta lista de índices é o
            elemento essencial na transformação reversa.
        """
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
        """
            Usando a lista de índices calculadas no método
            get_indexes e o índice correspondentes a linha
            original na matriz, reconstruímos a linha
            original, que corresponde ao arquivo decodificado.
        """
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
    encoder = bwt_encoder()
    (index, last_column) = encoder.encode(str)
    print('encoded:', index, last_column)

    # decode
    decoder = bwt_decoder()
    decoded = decoder.decode(last_column, index)
    print('decoded:', decoded)
