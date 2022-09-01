from io import StringIO

import pandas as pd
import streamlit as st

my_csv = st.file_uploader("Upload csv", type="csv")

if my_csv is not None:
    st.session_state["my_csv"] = my_csv.getvalue().decode("utf-8")

if "my_csv" in st.session_state:
    st.sidebar.dataframe(pd.read_csv(StringIO(st.session_state["my_csv"])))