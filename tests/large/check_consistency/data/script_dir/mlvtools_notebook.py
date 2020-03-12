#!/usr/bin/env python3
# Generated from ./notebooks/notebook.ipynb
import argparse


def mlvtools_notebook(sanitized_data, octal_data, binary_data, size_bin_data):
    """
    :param str sanitized_data: path to input sanitized data
    :param str octal_data: path to octal data output file
    :param str binary_data: path to binary data output file
    :param int size_bin_data: number of bits in a binary value
    :dvc-in sanitized_data: ./dummy/data/sanitized_data.txt
    :dvc-out octal_data: ./dummy/data/octal_data.txt
    :dvc-out binary_data: ./dummy/data/binary_data.txt
    :dvc-extra: --size-bin-data 8
    """

    # # Dummy pipeline - test step

    # This step splits data input file in 2 files. One with octal values the other with binaries values.

    # > In this case we use **dvc-extra** to provide a parameter which neither an input nor an output (--size-bin-data).

    with open(sanitized_data, 'r') as fd:
        data = fd.read()

    binaries = [d for d in data.split() if len(d.split('=')[1]) >= size_bin_data]

    octals = [d for d in data.split() if len(d.split('=')[1]) == 3]

    with open(octal_data, 'w') as fd:
        fd.write(' '.join(octals))

    with open(binary_data, 'w') as fd:
        fd.write(' '.join(binaries))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Command for script mlvtools_notebook')

    parser.add_argument('--sanitized-data', type=str, required=True, help="path to input sanitized data")

    parser.add_argument('--octal-data', type=str, required=True, help="path to octal data output file")

    parser.add_argument('--binary-data', type=str, required=True, help="path to binary data output file")

    parser.add_argument('--size-bin-data', type=int, required=True, help="number of bits in a binary value")

    args = parser.parse_args()

    mlvtools_notebook(args.sanitized_data, args.octal_data, args.binary_data, args.size_bin_data)
