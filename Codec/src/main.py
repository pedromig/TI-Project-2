import contextlib
import sys

import Codec.src.PPmd.compress as ppm
from Codec.src.PPmd import arithmeticcoding


def main(args):
    if len(args) != 2:
        sys.exit("Usage: python3 compress.py InputFile OutputFile")

    input = args[0]
    output = args[1]

    with open(input, "rb") as inp, contextlib.closing(
            arithmeticcoding.BitOutputStream(open(output, "wb"))) as bitout:
        ppm.compress(inp, bitout)


if __name__ == '__main__':
    main(["../DataSets/war_and_peace.txt", "../DataSets/Compressed/new.txt"])
