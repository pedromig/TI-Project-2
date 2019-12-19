import contextlib

from PIL import Image

import Codec.src.PPmd.compress as ppm
from Codec.src.Burrows_Wheeler.bw import BurrowsWheelerEncoder, BurrowsWheelerDecoder
from Codec.src.PPmd import arithmeticcoding
from Codec.src.RLE.rle import encodeRLE, decodeRLE, toString


def ppmCompress(input, output):
    with open(input, "rb") as inp, contextlib.closing(
            arithmeticcoding.BitOutputStream(open(output, "wb"))) as bitout:
        ppm.compress(inp, bitout)


def burrowsWheelerCompress(input, output):
    encoder = BurrowsWheelerEncoder()

    with open(input, "r") as input, open(output, "w") as output:
        lines = input.readlines()
        for line in lines:
            data = encoder.encode(line[:-1])
            output.write(str(data[0]) + "|" + str(data[1]) + "\n")


def burrowWheelerDecompress(input, output):
    decoder = BurrowsWheelerDecoder()

    with open(input, "r") as input, open(output, "w") as output:
        lines = input.readlines()
        for line in lines:
            aux = line.split("|", 1)
            string = decoder.decode(aux[1][:-1], int(aux[0]))
            output.write(string + "\n")


def rle_compress(input, output):
    with open(input, "r") as input, open(output, "w") as output:
        lines = input.readlines()
        for line in lines:
            data = encodeRLE(line)
            output.write(toString(data))


def rle_decompress(input, output):
    with open(input, "r") as input, open(output, "w") as output:
        lines = input.readlines()
        for line in lines:
            data = decodeRLE(line)
            output.write(data)


def imageOpen(image):
    with Image.open(image, "r") as img:
        imageComponents = list(img.getdata())
        imageColors = [x[0] for x in imageComponents]
        img.save("../DataSets/image.png", "PNG")

        with open("../DataSets/image.txt", "w") as imageFile:
            for i in imageColors:
                imageFile.write(chr(i))
    print(imageColors)


if __name__ == '__main__':
    #imageOpen("../DataSets/cromenco_c10.bmp")
    # burrowsWheelerCompress("../DataSets/image.txt", "../DataSets/xxx.txt")
    #ppmCompress("../DataSets/image.png", "../DataSets/compressed.png")
    ppmCompress("../DataSets/cromenco_c10.bmp", "../DataSets/compressed_ORIGINAL.png")

    # ppmCompress("../DataSets/cromenco_c10.bmp", "../DataSets/output")
    # burrowsWheelerCompress("../DataSets/cromenco_c10.bmp", "../DataSets/Compressed/bw_only_image.txt")
    # rle_compress("../DataSets/Compressed/new_bw.txt", "../DataSets/Compressed/new_bw_rle.txt")
    # rle_compress("../DataSets/war_and_peace.txt", "../DataSets/Compressed/new_rle_only.txt")

    # rle_decompress("../DataSets/Compressed/rle.txt","../DataSets/Compressed/rle_decomp.txt")
    # ppmCompress( "../DataSets/Compressed/new.txt", "../DataSets/Compressed/new2.txt")

    # ppmCompress("../DataSets/war_and_peace.txt", "../DataSets/Compressed/new3.txt")
    # burrowWheelerDecompress("../DataSets/Compressed/new.txt", "../DataSets/Compressed/decoded.txt")
