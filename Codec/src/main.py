import base64
import bz2 as bzip2
import contextlib

from PIL import Image

import Codec.src.PPmd.compress as ppm
from Codec.src.Burrows_Wheeler.bw import BurrowsWheelerEncoder
from Codec.src.PPmd import arithmeticcoding
from Codec.src.RLE.rle import encodeRLE, toString


def ppmCompress(input, output):
    with open(input, "rb") as inp, contextlib.closing(
            arithmeticcoding.BitOutputStream(open(output, "wb"))) as bitout:
        ppm.compress(inp, bitout)


def rle_compress(input, output):
    with open(input, "r") as input, open(output, "w") as output:
        lines = input.readlines()
        for line in lines:
            data = encodeRLE(line)
            output.write(toString(data))


def pngCompress(image, output):
    with Image.open(image, "r") as img:
        img.save(output, "PNG")


def bzip2Compress(input, output):
    compressor = bzip2.BZ2Compressor()
    chunk = 512
    data = b""
    with open(input, "rb") as file:
        while True:
            block = file.read(chunk)
            if not block:
                break
            data += compressor.compress(block)
        data += compressor.flush()
    with open(output, "wb") as dst:
        dst.write(data)


def bwCompress(input, output):
    encoder = BurrowsWheelerEncoder()
    data = ""

    with open(input, "r") as input:
        lines = input.readlines()
        for line in lines:
            temp = encoder.encode(line[:-1])
            data += (str(temp[0]) + "|" + str(temp[1]) + "\n")
    with open(output, "w") as output:
        output.write(data)


def imageBwCompress(input, output):
    encoder = BurrowsWheelerEncoder()
    chunk = 512
    data = ""
    with open(input, "rb") as input:
        while True:
            block = input.read(chunk)
            if not block:
                break
            block = base64.b64encode(block)
            temp = encoder.encode(block.decode("ascii"))
            data += (str(temp[0]) + "|" + str(temp[1]) + "\n")
    with open(output, "w") as out:
        out.write(data)


if __name__ == '__main__':
    generic_path = "../DataSets/"
    war_and_peace_path = "../DataSets/war_and_peace.txt"
    image_path = "../DataSets/cromenco_c10.bmp"

    bwCompress(war_and_peace_path, generic_path + "bw.txt")
    bzip2Compress( generic_path + "bw.txt", generic_path + "bw_bzip2.txt")
