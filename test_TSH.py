import pytest


@pytest.mark.parametrize('pat_num, expected', [
    (0, 'normal thyroid function'),
    (1, 'hyperthyroidism'),
    (2, 'normal thyroid function'),
    (3, 'hypothyroidism'),
])
def test_tsh_diagnosis(pat_num, expected):
    from TSH import tsh_diagnosis
    from TSH import create_person
    filename = 'test_data.txt'
    patient = create_person(filename, pat_num)
    answer = tsh_diagnosis(patient)
    assert answer == expected
