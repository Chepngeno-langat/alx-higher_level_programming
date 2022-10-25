#!/usr/bin/python3
""" read_file module """


def read_file(filename=""):
    """
    function that read specific file
    Args:
         fileName: name of the file
    """

   with open(filename, encoding="UTF-8") as file1:
        content = file1.read()
        print(content, end="")
    file1.closed
