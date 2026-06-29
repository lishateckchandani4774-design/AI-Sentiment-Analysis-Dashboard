import streamlit as st
import pandas as pd
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

st.set_page_config(
    page_title="Insights",
    page_icon="☁️"
)

st.title("☁️ AI Insights")
st.markdown("""
### ☁️ AI Insights

Discover important discussion topics,
keywords and sentiment drivers.
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

    all_text = " ".join(
        df[review_column].astype(str)
    )

    st.subheader("☁️ Word Cloud")

    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color="white"
    ).generate(all_text)

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.imshow(
        wordcloud,
        interpolation="bilinear"
    )

    ax.axis("off")

    st.pyplot(fig)
    st.subheader("🔥 Most Common Keywords")

    words = all_text.lower().split()

    common_words = Counter(words).most_common(10)

    keyword_df = pd.DataFrame(
        common_words,
        columns=["Word", "Frequency"]
    )

    st.dataframe(
        keyword_df,
        use_container_width=True
    )