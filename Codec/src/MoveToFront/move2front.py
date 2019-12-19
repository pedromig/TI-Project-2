def move_to_front(plain_text):
    # Initialise the list of characters (i.e. the dictionary)
    dictionary = sorted(set(plain_text))

    # Transformation
    compressed_text = list()
    rank = 0

    # Read in each character
    for c in plain_text:
        rank = dictionary.index(str(c))  # Find the rank of the character in the dictionary
        compressed_text.append(str(rank))  # Update the encoded text

        # Update the dictionary
        dictionary.pop(rank)
        dictionary.insert(0, c)

    dictionary.sort()  # sort dictionary
    return compressed_text, dictionary  # Return the encoded text as well as the dictionary


def inverse_move_to_front(compressed_data):
    compressed_text = compressed_data[0]
    dictionary = list(compressed_data[1])

    plain_text = ""
    rank = 0

    for i in compressed_text:
        rank = int(i)
        plain_text += str(dictionary[rank])

        e = dictionary.pop(rank)
        dictionary.insert(0, e)

    return plain_text


if __name__ == "__main__":
