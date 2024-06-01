import streamlit as st
from items import Main_Process
import openpyxl as op
import io

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
book=''
try:
    file1 = st.file_uploader("Upload Student Choice File", type=["xlsx"])
    file2 = st.file_uploader("Upload Subject with branch File", type=["xlsx"])
    book=Main_Process.allocationprocess(file1, file2)
    buffer=io.BytesIO()
    book.save(buffer)
    buffer.seek(0)
except:
    st.subheader(":red[Please Upload both Files]")

if book!='':
    st.title("Download Excel File")
    if st.download_button(label="Click to Download Allotement File", data=buffer, file_name="Allotement.xlsx",mime='application/octet-stream'):
        st.success("File Downloaded Successfully")
        buffer.truncate(0)
else:
    st.subheader(":red[Download File Not ready]")
