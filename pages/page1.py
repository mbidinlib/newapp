import streamlit as st

my_image = st.file_uploader("Upload image", type="jpg")

if my_image is not None:
    st.session_state["my_image"] = my_image

if "my_image" in st.session_state:
    st.sidebar.image(st.session_state["my_image"])
if "my_csv" in st.session_state:
    st.dataframe(pd.read_csv(StringIO(st.session_state["my_csv"])))