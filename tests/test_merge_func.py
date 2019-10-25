from merge_func import merge

Seq1 = [1, 1, 2, 2, 3, 3, 4, 4, 5]
Seq2 = [2, 5, 8, 10,]
Seq3 = [1, 2, 3]


EXPECTED_RESULT = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 8, 10]


def test_merge_func_on_simple_lists():
    result = merge(Seq1, Seq2, Seq3)
    for i in EXPECTED_RESULT:
        mer = next(result)
        assert i == mer


def test_merge_func_on_iterable_objects():
    result = merge(Seq1.__iter__(), Seq2.__iter__(), Seq3.__iter__())
    for i in EXPECTED_RESULT:
        mer = next(result)
        assert i == mer


def test_merge_func_with_empty_object():
    result = merge([], [], [])
    assert len(list(result)) == 0
