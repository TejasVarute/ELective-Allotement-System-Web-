import pandas as pd
from openpyxl import Workbook

def allocationprocess(data_file, sub_file):
    #getting Files
    df1 = pd.read_excel(data_file)
    df2 = pd.read_excel(sub_file)

    #sorting
    temp_df1 = df1.sort_values(by='Timestamp', ascending=False)
    temp_df1 = temp_df1.sort_values(by='First Name', ascending=True)
    temp_df1 = temp_df1.sort_values(by='Last Name', ascending=True)
    student_data = temp_df1.sort_values(by='CGPA', ascending=False)

    #List Declarations
    sub,branch,f_name,m_name,l_name,roll,div,subject,st_branch,st_cgpa,prn,seats=[[] for i in range (12)]
    
    #Getting Subject and Branches
    for _, ele in df2.iterrows():
            sub.append(ele['Subject'])
            branch.append(ele['Branch'])
            seats.append(ele['Seats'])

    #Declaring Seats per subject as User given
    subjects_capacity = {sub[i]: seats[i] for i in range(len(sub))}
    subjects_branch ={sub[i] : branch[i] for i in range (len(sub))}

    #Alloting       
    for _, student in student_data.iterrows():
            for i in range(len(sub)): 
                    subject_choice = student[f' [Choice {i+1}]']
                    branch=student['Branch']
                    if subjects_capacity[subject_choice] > 0 and subjects_branch[subject_choice] != branch and student['PRN'] not in prn:
                            f_name.append(student['First Name'])
                            m_name.append(student['Middle Name'])
                            l_name.append(student['Last Name'])
                            div.append(student['Div'])
                            st_cgpa.append(student['CGPA'])
                            roll.append(student['Roll No.'])
                            subject.append(subject_choice)
                            st_branch.append(branch)
                            prn.append(student['PRN'])
                            subjects_capacity[subject_choice] -= 1
                            break

    #Creating Full Name
    Full_name=[f'{f_name[i]} {m_name[i]} {l_name[i]}' for i in range (len(f_name))]
    wb = Workbook()
    wb.remove(wb.active)
    for ele in range(len(sub)):
        temp_name, temp_roll, temp_sub, temp_branch, temp_div, temp_cgpa, temp_prn = ([] for i in range(7))
        for ele1 in range(len(f_name)):
            if sub[ele] == subject[ele1]:
                temp_name.append(Full_name[ele1])
                temp_roll.append(roll[ele1])
                temp_div.append(div[ele1])
                temp_sub.append(subject[ele1])
                temp_branch.append(st_branch[ele1])
                temp_cgpa.append(st_cgpa[ele1])
                temp_prn.append(prn[ele1])
            sheet_name = subjects_branch[sub[ele]]
        ws = wb.create_sheet(title=sheet_name)
        ws.append(['PRN', 'Division', 'Roll No.', 'Branch', 'Name', 'CGPA', 'Subject'])

        for i in range(len(temp_prn)):
                ws.append([temp_prn[i], temp_div[i], temp_roll[i], temp_branch[i], temp_name[i], temp_cgpa[i], temp_sub[i]])
    return wb
#allocationprocess(r"D:\PERSONAL\Programs\Project\Subject allotment\Sample My\My GForm Sample\Student Response.xlsx",r"D:\PERSONAL\Programs\Project\Subject allotment\Sample My\My GForm Sample\Subject with Branch.xlsx")
