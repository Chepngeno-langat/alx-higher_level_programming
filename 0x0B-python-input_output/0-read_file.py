#!/usr/bin/python3
""" read_file module """


def read_line(filename=""):
    """
    function that read specific file
    Args:
         fileName: name of the file
    """

    with open(filename, encoding="UTF8", "r") as file1:
        content = file1.readlines()
        print(content end="")
