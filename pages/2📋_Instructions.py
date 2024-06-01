import streamlit as st

st.title("instructions")
instructions = '''


1. To create student choice data use google form to get information from students.

2. To create subject with branch file use refence of give sample file.

3. Set the column names as same as given sample file as it is Case sensitive.

4. Choose proper file while browsing.

5. You can be set number of choices, subjects, branches.

6. Use File format as .xlsx(Excel Workbook).


'''

st.markdown(instructions)
st.link_button("Google Form", "https://forms.gle/nFMwVVuUvJ9Xuv8W9")