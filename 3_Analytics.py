import streamlit as st
import pandas as pd
import plotly.express as px
from textblob import TextBlob


st.set_page_config(
    page_title="Analytics",
    page_icon="📈"
)

st.title("📈 Analytics Dashboard")
st.markdown("""
### 📈 Visual Analytics

Explore sentiment distributions,
charts and trend patterns.
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

    sentiment_count = (
        df["Sentiment"]
        .value_counts()
        .reset_index()
    )

    sentiment_count.columns = [
        "Sentiment",
        "Count"
    ]

    st.subheader("📈 Sentiment Distribution")

    fig = px.bar(
        sentiment_count,
        x="Sentiment",
        y="Count",
        color="Sentiment",
        title="Sentiment Analysis Results"
    )
    st.markdown("---")  
    
    st.plotly_chart(
        fig,
        use_container_width=True
    )

    pie_fig = px.pie(
        sentiment_count,
        values="Count",
        names="Sentiment",
        title="Sentiment Share"
    )

    st.plotly_chart(
        pie_fig,
        use_container_width=True
    )

    st.subheader("📈 Sentiment Trend Analysis")

    total_reviews = len(df)

    positive = len(
        df[df["Sentiment"] == "Positive"]
    )

    negative = len(
        df[df["Sentiment"] == "Negative"]
    )

    neutral = len(
        df[df["Sentiment"] == "Neutral"]
    )

    positive_percent = round(
        (positive / total_reviews) * 100,
        1
    )

    negative_percent = round(
        (negative / total_reviews) * 100,
        1
    )

    if positive_percent >= 60:

        st.success(
            "Trend: Strong Positive Sentiment"
        )

    elif negative_percent >= 60:

        st.error(
            "Trend: Strong Negative Sentiment"
        )

    else:

        st.info(
            "Trend: Mixed Public Opinion"
        )