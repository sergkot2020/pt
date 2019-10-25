"""
There are a few huge text files (>1TB each). You need to write an eternal generator,
which outputs those files in a multiplexed file-by-file line-by-line order.
The next line after the last one is the first one.
The next file after the last one is, again, the first one.

For example, you have three files:

File 1:
1
2
3

File 2:
A
B
C
D
               
File 3:
 -
 +

 In this case, if the files are passed to the generator as arguments in the above order,
 the beginning of the output sequence must be the following:               

 1
 A
 -
 2
 B
 +
 3
 C
 -
 1
 D
 +
 2
 A
 -
"""


def is_empty(file):
    """
    :param file: file path
    :return: True is file empty, another False.
    """
    with open(file) as f:
        first = f.readline()
        if first:
            return False
    return True


def file_generator(file):
    """
    :param file: file path like a '/etc/file.txt'
    :return: eternal object - generator
    """
    while True:
        with open(file) as f:
            for line in f:
                yield line.strip()
        continue


def huge_file_zipper(*args):
    """
    :param args: file path file1.txt, file2.txt ...
    :return: object - generator
    """
    generator_list = [file_generator(i) for i in args if not is_empty(i)]

    def generator_func(file_list):
        while True:
            for file in file_list:
                yield next(file)

    if generator_list:
        return generator_func(generator_list)
    return None  # or raise exception maybe
