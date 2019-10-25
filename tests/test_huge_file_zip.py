from huge_file_zip import huge_file_zipper, file_generator, is_empty


EXPECTED_LIST = [
        'file1-1', 'file2-1', 'file3-1',
        'file1-2', 'file2-2', 'file3-2',
        'file1-3', 'file2-3', 'file3-3',
        'file1-4', 'file2-4', 'file3-4',
        'file1-1', 'file2-5', 'file3-5',
        'file1-2', 'file2-1', 'file3-6',
        'file1-3', 'file2-2', 'file3-7',
        'file1-4', 'file2-3', 'file3-1',
        'file1-1', 'file2-4', 'file3-2',
        'file1-2', 'file2-5', 'file3-3',
        'file1-3', 'file2-1', 'file3-4',
        'file1-4', 'file2-2', 'file3-5',
        'file1-1', 'file2-3', 'file3-6',
        'file1-2', 'file2-4', 'file3-7',
        'file1-3', 'file2-5', 'file3-1',
        'file1-4', 'file2-1', 'file3-2',
    ]


def test_file_generator():
    """
    We pass file1 in function, file look like:
    file1-1
    file1-2
    file1-3
    file1-4
    :return: eternal generator
    """
    expected_value = ['file1-1', 'file1-2', 'file1-3', 'file1-4']
    file = file_generator('file1')

    cycle = 10
    while cycle > 0:
        for expect in expected_value:
            line = next(file)
            assert line == expect
            cycle -= 1


def test_is_empty():
    # create empty file
    with open('empty', 'w'):
        pass
    assert is_empty('empty') is True
    # check not empty file
    assert is_empty('file1') is False


def test_huge_file_zipper():
    """
    We pass file1, file2, file3, files look like:
    |----------|-------------|----------|
    |  file1   |    file2    |   file3  |
    |==========|=============|==========|
    |file1-1   |   file2-1   |  file3-1 |
    |file1-2   |   file2-2   |  file3-2 |
    |file1-3   |   file2-3   |  file3-3 |
    |file1-4   |   file2-4   |  file3-4 |
    |          |   file2-5   |  file3-5 |
    |          |             |  file3-6 |
    |          |             |  file3-7 |
    |==========|=============|==========|
    :return: eternal generator, that zip files, output sequence look like:
    file1-1, file2-1, file3-1, file1-2 , file2-2, file3-2...
    """

    generator = huge_file_zipper('file1', 'file2', 'file3')

    for expect in EXPECTED_LIST:
        assert expect == next(generator)


def test_huge_file_zipper_with_empty_files():
    # create empty file
    with open('empty', 'w'):
        pass
    generator = huge_file_zipper('empty', 'file1', 'file2', 'file3')

    for expect in EXPECTED_LIST:
        assert expect == next(generator)

    # check that happens if we call functions with one empty file
    assert huge_file_zipper('empty') is None


def test_not_exist_file():

    try:
        huge_file_zipper('some_not_exist_file', 'some_not_exist_file2')
    except FileNotFoundError as e:
        assert e