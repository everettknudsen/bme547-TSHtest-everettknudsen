In this project, patient data in a text file is parsed into a unique patient dictionary. Values of TSH are then examined by a function, and an appropriate diagnosis is determined based on the values. 

## dictionary_and_diagnostic(filename)

This function takes a specific text file, determines the number of patients in the file, creates unique dictionaries, diagnoses patients, and outputs the information in json files. This is the function to import and test when grading or trying a new text file besides the test_data.txt file. It uses the functions in the rest of the code to achieve these things.

## determine_patient_number()

This function determines the number of patients in a given filename.txt.

## create_person(filename)

This function is responsible for making unique patient dictionaries based on the informaiton in filename.txt

## tsh_diagnosis(patient)

This function will diagnost and sort the TSH values low to high.

## retrieve_patient_info(patient)

This function outputs patient information. This function was primarily an experiement for me to determine if everything was working properly!

## save_patient_files(patient)

This function saves and outputs the fully updated json file based on the patient's information.


