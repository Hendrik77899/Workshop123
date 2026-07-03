import streamlit as st
import pandas as pd
from analysis import *

st.title("Feldspar Price Time-Series Analyzer")

uploaded_file = st.file_uploader("Upload Feldspar CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Raw Data")
    st.dataframe(df)

    st.subheader("Statistics")
    st.dataframe(get_statistics(df))

    st.subheader("Price Trend")
    fig1 = create_line_plot(df, "Month", "Price (US)")
    st.pyplot(fig1)

    st.subheader("Moving Average")
    fig2 = create_moving_average_plot(df, "Month", "Price (US)", window=3)
    st.pyplot(fig2)

    st.subheader("Percentage Change")
    pct_df = calculate_percent_change(df, "Price (US)")
    st.dataframe(pct_df)
