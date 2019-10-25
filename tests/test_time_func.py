from time_func import seconds_returner


def test_check_second_returner_correct_work():
    """
    Checked correct input value
    """
    assert seconds_returner(30) == 30
    assert seconds_returner('15') == 15
    assert seconds_returner('30s') == 30
    assert seconds_returner('s') == 1
    assert seconds_returner('m') == 60
    assert seconds_returner('h') == 3600
    assert seconds_returner('60.5m') == 3630
    assert seconds_returner('s') == 1
    assert seconds_returner('1.5h') == 5400
    assert seconds_returner('1.3d') == 112320


def test_check_second_returner_with_fail_input():
    """
    Checked fail input value
    """
    fail_input = [
        '10seconds',
        'jkjbkjhouo',
        'jkjb543kjhouo',
        '',
        '.'
    ]

    for fail in fail_input:
        try:
            seconds_returner(fail)
        except Exception as e:
            assert e
