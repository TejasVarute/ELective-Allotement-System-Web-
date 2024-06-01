import streamlit as st
from items import Main_Process
import os

file=''
st.set_page_config(
    page_icon="📨",
    page_title="Elective Allotement System",
)
st.title("Open Elective Allotement System")
st.sidebar.success('''Provide proper Information About
                   :red[Please read Instruction 
before to perform]''')
# File upload
try:
    file1 = st.file_uploader("Upload Student Choice File", type=["xlsx"])
    file2 = st.file_uploader("Upload Subject with branch File", type=["xlsx"])
    op_file=Main_Process.allocationprocess(file1, file2)
    def get_file(file):
        with open(file, "rb") as template_file:
            return template_file.read()
    file = get_file(op_file)

except:
    st.subheader(":red[Please Select Files]")

if file != '':
    if st.download_button(label="Click to Download Allotement File", data=file, file_name="Allotement.xlsx",mime='application/octet-stream'):
        st.success("File Downloaded Successfully") 
        os.remove(op_file)
else:
    st.subheader(":red[Download File Not ready]")