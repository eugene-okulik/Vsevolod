students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

students_list = ', '.join(students)
subjects_list = ', '.join(subjects)

my_text = f'Students {students_list} study these objects: {subjects_list}'

print(my_text)
