😊 AI Sentiment Analysis Dashboard

An interactive Streamlit-based Sentiment Analysis Dashboard that uses Natural Language Processing (NLP) to analyze text, customer reviews, social media posts, and feedback. The application provides sentiment classification, visual analytics, keyword insights, and downloadable reports to help users understand public opinion.

📌 Features
✍️ 1. Text Sentiment Analysis
Analyze individual text inputs.
Classifies sentiment as:
😊 Positive
😐 Neutral
😞 Negative
Displays sentiment polarity score.


📊 2. CSV Dashboard
Upload CSV datasets containing reviews or comments.
Preview uploaded data.
Automatically analyze sentiment for each record.
Display:
Positive reviews
Negative reviews
Neutral reviews
Total reviews
Generate overall public opinion summary.
Download analyzed dataset as a CSV report.


📈 3. Analytics Dashboard
Interactive bar chart showing sentiment distribution.
Pie chart for sentiment share.
Trend analysis indicating:
Strong Positive Sentiment
Strong Negative Sentiment
Mixed Public Opinion


☁️ 4. AI Insights
Generate a word cloud from uploaded reviews.
Display the top 10 most frequent keywords.
Identify commonly discussed topics.


🛠️ Technologies Used
Python
Streamlit
Pandas
TextBlob
Plotly
Matplotlib
WordCloud


📂 Project Structure
AI-Sentiment-Analysis/
│
├── Home.py
├── pages/
│   ├── 1_Text_Analysis.py
│   ├── 2_CSV_Dashboard.py
│   ├── 3_Analytics.py
│   └── 4_Insights.py
│   ├── Reviews
├── requirements.txt
└── Readme.md


📦 Requirements
streamlit
pandas
plotly
textblob
matplotlib
wordcloud

👩‍💻 Author
Lisha Teckchandani
