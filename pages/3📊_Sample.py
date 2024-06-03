import streamlit as st
import pandas as pd

st.title("Sample Tables")
st.header("Student Choice Table")

st.subheader(":red[Please make sure your google form sheet containes following colomns]")

clms1 = {"Timestamp":[],
       "PRN":[],
       "First Name":[],
       "Middle Name":[],
       "Last Name":[],
       "Branch":[],
       "Div":[],
       "Roll No.":[],
       "CGPA":[],
       "[choice 1]":[],
       "[choice 2]":[],
       "[choice 3]":[],
       "[choice 4]":[],
       "[choice 5]":[],
       "[choice 6]":[],
       "[choice 7]":[],
       "[choice 8]":[],
       "[choice nth]":[]}

clms2 = {"Subject":['subject 1','subject 2','subject 3','subject 4','subject nth'],
         "Branch":['Branch 1','Branch 2','Branch 3','Branch 4','Branch nth'],
         "Seats":['Subjects 1 seat intake','Subjects 2 seat intake','Subjects 3 seat intake','Subjects 4 seat intake','Subjects nth seat intake']}

choices_df = pd.DataFrame(clms1)
seats_df = pd.DataFrame(clms2)
st.table(choices_df)

st.header("Subject with their branch and seats intakes")
st.subheader(":red[Please make sure you filled this file properly]")
st.table(seats_df)