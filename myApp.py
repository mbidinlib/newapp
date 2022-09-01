from io import StringIO

import pandas as pd
import streamlit as st


col1, col2 = st.columns(2)

with col1:
    my_csv = st.file_uploader("Upload csv", type="csv")

with col2:
    if my_csv is not None:
        st.session_state["my_csv"] = my_csv.getvalue().decode("utf-8")
    if "my_csv" in st.session_state:
        st.sidebar.dataframe(pd.read_csv(StringIO(st.session_state["my_csv"])))