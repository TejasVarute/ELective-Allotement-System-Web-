import streamlit as st

st.title(":red[instructions]")
instructions = '''1. To create student choice data use google form to get information from students.
\n2. To create subject with branch file use refence of give sample file.
\n3. Set the column names as same as given sample file as it is Case sensitive.
\n4. Choose proper file while uploading.
\n5. You can be set number of choices, subjects, branches.
\n6. Use File format as .xlsx(Excel Workbook).
\n7. Make sure the subject Names in both files are sames.'''

st.markdown(instructions)
st.subheader(":red[Google Form Sample]")
st.link_button("Google Form link", "https://forms.gle/nFMwVVuUvJ9Xuv8W9")