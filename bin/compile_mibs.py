#!/usr/bin/env python3
import argparse
#from piat.utils.mib_compiler import compile

parser = argparse.ArgumentParser(description='compile mib files')
parser.add_argument('--source-dir', dest='source_dir', help='source directory of the MIBs',required=True)


def main():
    args = parser.parse_args()
    print(args.source_dir)


if __name__ == '__main__':
    main()
