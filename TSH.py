def main():
    filename = 'test_data.txt'
    pat_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for x in pat_nums:
        person = create_person(filename, x)
        tsh_diagnosis(person)
        # retrieve_patient_info(person)
        save_patient_files(person)


def create_person(filename, patient_num):
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
    return person_dict


def tsh_diagnosis(patient):
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
