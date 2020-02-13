import argparse

parser = argparse.ArgumentParser(description='A Molecule utility that reads XYZ files and calculates the distance between atoms at index1 and index2.')
parser.add_argument('filename', type=str, help='The XYZ file to read.')
parser.add_argument('index1', type=int, help='Index of the first atom.')
parser.add_argument('index2', type=int, help='Index of the second atom.')

args = parser.parse_args()

print(parser)
print(args)
print(args.filename)
print(args.index1)
