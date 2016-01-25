import os.path
import os
import sys
from collections import Counter
from argparse import ArgumentParser


def get_valid_file(file_name):
    """
    Checks to see if a given file exists and returns a boolean indicating the result.
    :param file_name: Name (and path if possible) of file to check
    :return: True if file exists and false otherwise
    """
    valid_file = False
    try:
        if os.path.exists(file_name):
            valid_file = True
            print "Valid File"
        else:
            valid_file = False
            raise Exception('Vic Sucks')

    # TODO : Validate file informaiton here
    except Exception as ex:
        print ex.message


def main():
    print "Main"
    get_valid_file("DearJosh.txt")


if __name__ == "__main__":
    main()
