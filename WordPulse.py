import streamlit as st
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

st.set_page_config(page_title="WordPulse", layout="wide")

st.markdown("<h1 style='text-align: center; font-weight: bold;'>WordPulse</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Track the pulse of customer words</h4>", unsafe_allow_html=True)
st.write("---")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])


def find_column(df, keywords):
    for col in df.columns:
        col_lower = col.lower().strip()
        for kw in keywords:
            if kw in col_lower:
                return col
    return None

if uploaded_file is not None:
    
    df = pd.read_csv(uploaded_file, encoding="latin1")
    df.columns = df.columns.str.strip()


    reviews_col = find_column(df, ["review", "comment", "feedback", "text"])
    rating_col = find_column(df, ["rating", "stars", "score"])

    if reviews_col:
        source_col = reviews_col
        st.success(f"Using '{source_col}' column for sentiment analysis.")
    elif rating_col:
        source_col = rating_col
        st.success(f"Using '{source_col}' column (numeric ratings) for sentiment analysis.")
    else:
        st.error("No suitable column found for sentiment analysis.")
        st.stop()


    def clean_text(text):
        return str(text).strip()

    def get_sentiment_from_text(text):
        polarity = TextBlob(clean_text(text)).sentiment.polarity
        if polarity > 0.05:
            return "Positive"
        elif polarity < -0.05:
            return "Negative"
        else:
            return "Neutral"

    def get_sentiment_from_rating(rating):
        try:
            rating = float(rating)
            if rating >= 4:
                return "Positive"
            elif rating <= 2:
                return "Negative"
            else:
                return "Neutral"
        except:
            return "Neutral"


    if source_col == reviews_col:
        df["Sentiment"] = df[source_col].apply(get_sentiment_from_text)
    else:
        df["Sentiment"] = df[source_col].apply(get_sentiment_from_rating)


    st.subheader("Sentiment Report")
    st.dataframe(df[[source_col, "Sentiment"]])

    sentiment_counts = df["Sentiment"].value_counts()


    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Pie Chart")
        fig1, ax1 = plt.subplots(figsize=(4, 4))
        colors = {"Positive": "green", "Neutral": "gold", "Negative": "red"}
        ax1.pie(
            sentiment_counts,
            labels=sentiment_counts.index,
            autopct="%1.1f%%",
            colors=[colors.get(label, "gray") for label in sentiment_counts.index],
            startangle=140
        )
        ax1.axis("equal")
        st.pyplot(fig1)

    with col2:
        st.subheader("Bar Chart")
        fig2, ax2 = plt.subplots()
        sentiment_counts.plot(kind="bar", color=["green", "gold", "red"], ax=ax2)
        plt.xticks(rotation=0)
        plt.ylabel("Count")
        plt.title("Sentiment Count")
        st.pyplot(fig2)


    st.subheader("Overall Sentiment Report")
    st.write(sentiment_counts)

else:
    st.info("Please upload a CSV file to begin.")
