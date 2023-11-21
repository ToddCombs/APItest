def test_two():
    assert 1 == 1
    assert 1 != 2
    assert 1 < 2
    assert 2 > 1
    assert 1 >= 1
    assert 1 <= 1

    assert 'a' not in 'abc'
    assert 'a' not in 'bcd'
    assert True is True
    assert False is not True
