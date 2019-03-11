def compare_subjects_within_student(subj1_all_students,
                                    subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    The function takes two dictionaries as an argument. where the key is the name of the student and inside each key inserted is the scores he got.
    The dictionary MUST contain a key named 'subject name' which include the subject's name.
    """
    
    for key1 in subj1_all_students:
        for key2 in subj2_all_students:
            if key1 == key2 != 'subject name':
                if (subj1_all_students[key1][1] + subj1_all_students[key1][0]) > (subj2_all_students[key1][1] + subj2_all_students[key1][0]):
                    print(key1, subj1_all_students['subject name'])
                else:
                    print(key1, subj2_all_students['subject name'])
                    
                    
                    
subj1_all_students = {'subject name':'History','Amit':[10,80],'Ben':[70,85],'Charlie':[99,100],'Daniel':[72,24],'Eli':[72,84]}
subj2_all_students = {'subject name':'Math','Amit':[86,40],'Charlie':[69,40],'Daniel':[98,64],'Eli':[54,76]}
compare_subjects_within_student(subj1_all_students,subj2_all_students)