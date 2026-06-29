import streamlit as st

# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="AI Sentiment Analysis",
    page_icon="😊",
    layout="wide"
)

# ---------------------------------
# CUSTOM CSS
# ---------------------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1 {
    color: #4CAF50;
}

h2, h3 {
    color: white;
}

[data-testid="stMetricValue"] {
    color: #4CAF50;
}

[data-testid="stMetricLabel"] {
    color: white;
}

.stAlert {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------
# SIDEBAR
# ---------------------------------

st.sidebar.title("😊 Sentiment Dashboard")

st.sidebar.info("""
Task 6 Project

✔ Text Analysis
✔ CSV Dashboard
✔ Analytics
✔ Insights
✔ Reports
""")

# ---------------------------------
# TITLE
# ---------------------------------

st.title("😊 AI Sentiment Analysis & Public Opinion Dashboard")

st.markdown("""
### Task 6 - Sentiment Analysis (AI + Data Science)

Analyze reviews, customer feedback, social media posts and public opinions using Natural Language Processing (NLP).
""")

# ---------------------------------
# KPI CARDS
# ---------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Sentiment Types",
        "3"
    )

with col2:
    st.metric(
        "Dashboard Pages",
        "5"
    )

with col3:
    st.metric(
        "Reports",
        "Downloadable"
    )

# ---------------------------------
# WORKFLOW
# ---------------------------------

st.markdown("---")

st.subheader("🔄 Sentiment Analysis Workflow")

st.markdown("""
📄 Reviews / Feedback / Social Posts

⬇️

🧠 NLP Sentiment Analysis

⬇️

😊 Positive | 😐 Neutral | ❌ Negative

⬇️

📊 Analytics Dashboard

⬇️

☁️ Insights & Trend Detection

⬇️

📄 Downloadable Report
""")

# ---------------------------------
# NAVIGATION
# ---------------------------------

st.markdown("---")

st.subheader("🧭 Application Navigation")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("""
Text Analysis

Analyze individual
reviews and feedback
""")

with col2:
    st.info("""
CSV Dashboard

Dataset preview,
metrics and summaries
""")

with col3:
    st.info("""
Analytics

Charts, trends and
sentiment distribution
""")

with col4:
    st.info("""
Insights

Word cloud and
keyword analysis
""")

# ---------------------------------
# INFO
# ---------------------------------

st.markdown("---")

st.info(
    "Use the pages in the left sidebar to start analyzing text and datasets."
)

st.markdown("---")

st.header("⚙️ Technologies Used")

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:
    st.success("Python")

with tech2:
    st.success("Streamlit")

with tech3:
    st.success("TextBlob")

with tech4:
    st.success("Plotly")
# ---------------------------------
# FOOTER
# ---------------------------------

st.markdown("---")

st.caption(
    "Built with Python • Streamlit • NLP • Data Science"
)