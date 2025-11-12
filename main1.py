import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("basic streamlit demo")
st.header("using various streamlit components")
st.markdown("---")

st.sidebar.header("Sidebar Controls")
st.sidebar.button("settings")
st.sidebar.button("options")

col1, col2 = st.columns(2)

with col1:
    st.subheader(" User details")
    name = st.text_input( "Enter your name")
    number = st.number_input("age", min_value=1, max_value=100, value=10)

with col2:
    st.subheader("gender selection")
    option = st.selectbox("gender", ('male', 'female', 'Other'))
    is_checked = st.checkbox("below or egual to 18", value=True)
    is_checked = st.checkbox("above or equal to 18", value=True)
st.markdown("---")


st.subheader("next actions")
if st.button("click here"):
    st.success(f"Action triggered! Hello")
    
if is_checked:
    st.info("thank you")
    st.write("Progress Bar and Spinner")
    with st.spinner('Waiting for data...'):
        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1)
        st.success("Simulation Complete!")
        st.markdown("---")


st.subheader("Data & Plot Visualization")
st.markdown("#### DataFrame")
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [number, number + 10, number - 5, number * 2],
    'Random': np.random.rand(4)
}
df = pd.DataFrame(data)
st.dataframe(df) 
st.markdown("#### Static Table")
st.table(df.head(3)) 
st.markdown("#### Line Chart ")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)
st.subheader(" Summary")
st.write(
    f"""
    * **Variables:** The selected option is **{option}**.
    * **DataFrames:** (See below)
    """
)
st.write(df)
st.caption("end of the demo")
st.button("submit")
 # Network URL: http://10.113.178.221:8503