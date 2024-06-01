# Open-elective-allotment-system
This is simple project using data analysis to perform open elective subject allocation in engineering colleges. 

What is open elective subject in engineering ?
-> Open elective subjects are subjects that students from other branches of engineering can choose to study in addition to their core subjects. 
   This allows students to broaden their knowledge and skills, and to explore areas of engineering that they are interested in.

How the allocation works ?
->  Frist get the student information as follows,
   •	A student choice file, containing the PRN, name, branch, division, roll number, and subject choices of each student.
   •	A branch and subject file, containing the branches and subjects that are available for open elective.

  Allocate subject using following condition,
   •	If a student chooses a subject that is the same as their branch, then the subject is not considered.
   •	Students are allocated to their preferred subjects in order of their CGPA.
   •	If two students have the same CGPA, then they are allocated to their preferred subjects in order of their last name.
   •	If a student is not satisfied with their allocated subject, they can fill out the google form again and their latest choices will be considered.
   •	The output of the software is an Excel file containing the names of the students who have been allocated to each subject. This file can then be used to generate the final allotment list.

Algorithm :
1)	START.
2)	Get student data file from user as student_data.
3)	Get file of branch and their subject as subject_data.
4)	Get output location to store output file as op_path.
5)	Get the seats available per subject from subject_data fie and assign it with each subject in form of dictionary (ex. {‘M1’: 20}).
6)	First, Sort student_data with their last name. Then, sort it with students CGPA.
7)	In loop,
•	Check if any seat available for student choice subject.
(a)	If yes:
(i)	Book seat for that subject.
(ii)	Decrement one seat in dictionary for that subject.
(b)	Else:
(i)	Check next choice.
(ii)	Repeat step a.
8)	Repeat step 7 until book all the seat of all the subjects.
9)	Write all students name with their details and allocated subject to an Excel file.
10)	Save the Excel file at op_path given by user.
11)	STOP.

Report : https://drive.google.com/file/d/1faFG4BxotW8VPrMLOonId5O1-L4y4E51/view?usp=sharing

