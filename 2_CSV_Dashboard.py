import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from textblob import TextBlob
from collections import Counter

st.title("📊 CSV Sentiment Dashboard")
st.markdown("""
### 📊 Dashboard Overview

Upload a CSV file and generate
sentiment summaries, metrics,
and executive reports.
""")

st.sidebar.title("😊 Sentiment Dashboard")

st.sidebar.info("""
Task 6 Project

✔ Text Analysis
✔ CSV Dashboard
✔ Analytics
✔ Insights
✔ Reports
""")
uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

    review_column = st.selectbox(
        "Select Review Column",
        df.columns
    )

    sentiments = []

    for review in df[review_column]:

        analysis = TextBlob(str(review))

        polarity = analysis.sentiment.polarity

        if polarity > 0:
            sentiments.append("Positive")

        elif polarity < 0:
            sentiments.append("Negative")

        else:
            sentiments.append("Neutral")

    df["Sentiment"] = sentiments

    st.subheader("✅ Analyzed Dataset")
    st.dataframe(df)

    sentiment_count = (
        df["Sentiment"]
        .value_counts()
        .reset_index()
    )

    sentiment_count.columns = [
        "Sentiment",
        "Count"
    ]

    positive = len(
        df[df["Sentiment"] == "Positive"]
    )

    negative = len(
        df[df["Sentiment"] == "Negative"]
    )

    neutral = len(
        df[df["Sentiment"] == "Neutral"]
    )

    st.subheader("📊 Dashboard Metrics")
    total_reviews = len(df)
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Positive",
            positive
        )

    with col2:
        st.metric(
            "Negative",
            negative
        )

    with col3:
        st.metric(
            "Neutral",
            neutral
        )

    with col4:
        st.metric(
            "Total Reviews",
            total_reviews
        )

    report = df.to_csv(index=False)

    st.subheader("🧠 Public Opinion Insight")

    if positive > negative:

        st.success(
            "Overall public opinion is Positive."
        )

    elif negative > positive:

        st.error(
            "Overall public opinion is Negative."
        )

    else:

        st.info(
            "Public opinion is Neutral."
        )
        st.subheader("📋 Executive Summary")

        positive_percent = round(
            (positive / total_reviews) * 100,
            1
        )

        negative_percent = round(
            (negative / total_reviews) * 100,
            1
        )

        neutral_percent = round(
            (neutral / total_reviews) * 100,
            1
        )

        st.info(
            f"""
        Total Reviews Analyzed: {total_reviews}

        Positive Reviews: {positive_percent}%

        Negative Reviews: {negative_percent}%

        Neutral Reviews: {neutral_percent}%
        """
        )

        st.download_button(
            label="📄 Download Sentiment Report",
            data=report,
            file_name="sentiment_report.csv",
            mime="text/csv"
        )

    st.subheader("☁️ Word Cloud")

    all_text = " ".join(
        df[review_column].astype(str)
    )



    st.markdown("---")

    st.markdown(
        """
        Built with ❤️ using
        Python • Streamlit • NLP • Data Science
        """
    )