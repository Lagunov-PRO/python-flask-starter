def test_dict():
    first = {'id': 1, 'name': 'Ivan'}
    second = {'name': 'Ivan', 'id': 1}

    assert first == second

