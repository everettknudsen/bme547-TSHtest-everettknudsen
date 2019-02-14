def main():
    """

    Returns: the main function of the code which
    will run the dictionary_and_diagnosis on a data file.

    """
    dictionary_and_diagnostic('test_data.txt')


def dictionary_and_diagnostic(filename):
    """

    Args:
        filename: takes filename.txt assuming patient
        takes up 4 lines/ patient and has final line with "END"

    Returns: json file with proper TSH diagnosis
    based on TSH values. The output file is in format First-Last.json

    """
    pat_nums = determine_patient_number(filename)
    for x in pat_nums:
        person = create_person(filename, x)
        tsh_diagnosis(person)
        retrieve_patient_info(person)
        save_patient_files(person)


def determine_patient_number(filename):
    """

    Args:
        filename: takes an input file with patient information.
        will remove the last line--it is assumed this line contains
        only the word END. Then, it is assumed that a patient will
        take only four lines of information, so 1 patient = 4 lines

    Returns:
        pat_list: a list of integers which will be used to loop
        through the total patients for the
        dictionary_and_diagnostic() function

    """
    f = open(filename)
    parsed = f.readlines()
    parsed.pop()
    total_lines = len(parsed)
    pat_num = int(total_lines/4)
    pat_list = list(range(pat_num))
    return pat_list


def create_person(filename, patient_num):
    """

    Args:
        filename: the data file which has all of
        the patient information stored in it to be
        made into a unique patient dictionary
        patient_num: a list which specifies
        how many patients are in the file filename. Used to loop
        through the patients in the file

    Returns:
        person_dict: a unique patient dictionary with
        First Name, Last Name, Age, Sex, Diagnosis, and TSH Values
        Diagnosis remains undiagnosed until run through tsh_diagnosis()

    """
    f = open(filename)
    person = f.readlines()
    index = patient_num*4
    name = person[0+index].split()
    age = person[1+index]
    sex = person[2+index]
    tsh = person[3+index]
    person_dict = {'First Name': name[0],
                   'Last Name': name[1],
                   'Age': age.rstrip('\n'),
                   'Sex': sex.rstrip('\n'),
                   'Diagnosis': 'undiagnosed',
                   'TSH Values': tsh.rstrip('\n')
                   }
    f.close()
    return person_dict


def tsh_diagnosis(patient):
    """

    Args:
        patient: the unique patient dictionary created
        in create_person(). This function pulls TSH values and
        makes an appropriate diagnosis of the patient.
        It then modifies the diagnosis and
        sorts the TSH values low to high.

    Returns:
        diagnosis: which is then stored in the appropriate
        location within the patient's unique dictionary


    """
    tsh_string = patient['TSH Values']
    new_str = tsh_string.replace('TSH,', '')
    no_commas = new_str.replace(',', ' ')
    new = no_commas.split()
    new.sort(key=float)
    s = ', '
    tsh_sorted = s.join(new)
    final_nums = [float(i) for i in new]
    for x in final_nums:
        if x < 1.0:
            diagnosis = 'hyperthyroidism'
            break
        elif x > 4.0:
            diagnosis = 'hypothyroidism'
            break
        else:
            diagnosis = 'normal thyroid function'
    patient['Diagnosis'] = diagnosis
    patient['TSH Values'] = tsh_sorted
    return diagnosis


def retrieve_patient_info(patient):
    """

    THIS FUNCTION IS NOT ENTIRELY NECESSARY TO RUN THE PROGRAM,
    IT WAS MADE IN ORDER TO CHECK FOR PROPER FUNCTIONALITY

    Args:
        patient: takes the fully modified patient
        dictionary and outputs each key and definition

    Returns:
        prints the keys and definitions
        of the modified patient dictionary

    """
    first_name = patient['First Name']
    last_name = patient['Last Name']
    age = patient['Age']
    sex = patient['Sex']
    diagnosis = patient['Diagnosis']
    tsh_values = patient['TSH Values']

    print('First Name: {} {}'.format(first_name, last_name))
    print('Age: {}'.format(age))
    print('Sex: {}'.format(sex))
    print('Diagnosis: {}'.format(diagnosis))
    print('TSH Values: {}'.format(tsh_values))


def save_patient_files(patient):
    """

    Args:
        patient: takes the fully modified patient
        dictionary and writes a json file in the format
        First-Last.json which contains all the
        information from the dictionary.

    Returns:
        will create a json file with all the
        information for the patient and TSH diagnosis.

    """
    import json
    full_name = [patient['First Name'], patient['Last Name']]
    d = '-'
    file_type = '.json'
    full_name = d.join(full_name) + file_type
    out_file = open(full_name, 'w')
    json.dump(patient, out_file)
    out_file.close()


if __name__ == '__main__':
    main()
