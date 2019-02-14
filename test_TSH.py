import pytest


@pytest.mark.parametrize('pat_num, expected', [
    (0, 'normal thyroid function'),
    (1, 'hyperthyroidism'),
    (2, 'normal thyroid function'),
    (3, 'hypothyroidism'),
])
def test_tsh_diagnosis(pat_num, expected):
    """

    Args:
        pat_num: this is the number which corresponds
        to the patient's location within the file
        expected: this is the expected TSH diagnosis
         against which the function output can be checked

    Returns:
        tests the diagnosis function for correct result

    """
    from TSH import tsh_diagnosis
    from TSH import create_person
    filename = 'test_data.txt'
    patient = create_person(filename, pat_num)
    answer = tsh_diagnosis(patient)
    assert answer == expected


def test_determine_patient_number():
    """

    Returns: Tests to make sure the determine_patient_number()
    function is giving the expected value

    """
    from TSH import determine_patient_number
    filename = 'test_data.txt'
    answer = determine_patient_number(filename)
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert answer == expected
