import streamlit as st
from textblob import TextBlob
st.sidebar.title("😊 Sentiment Dashboard")

st.sidebar.info("""
Task 6 Project

✔ Text Analysis
✔ CSV Dashboard
✔ Analytics
✔ Insights
✔ Reports
""")
st.title("✍️ Text Sentiment Analysis")

st.write("Enter any review, feedback, tweet, or comment.")

text = st.text_area(
    "Enter Text",
    height=200
)

if st.button("Analyze Sentiment"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:

        analysis = TextBlob(text)

        polarity = analysis.sentiment.polarity

        if polarity > 0:
            sentiment = "😊 Positive"

        elif polarity < 0:
            sentiment = "😞 Negative"

        else:
            sentiment = "😐 Neutral"

        st.subheader("Result")

        st.success(sentiment)

        st.metric(
            "Polarity Score",
            round(polarity, 2)
        )
st.markdown("---")

st.markdown(
    """
    Built with ❤️ using
    Python • Streamlit • NLP • Data Science
    """
)