def main():
    filename = 'test_data.txt'
    first_person = create_person(filename, 5)
    tsh_diagnosis(first_person)
    retrieve_diagnosis(first_person)


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


def retrieve_diagnosis(patient):
    y = patient['Diagnosis']
    print(y)
    z = patient['TSH Values']
    print(z)


if __name__ == '__main__':
    main()
