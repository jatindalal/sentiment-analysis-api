import streamlit as st
import requests
import os

API_ADDRESS = os.getenv('API_ADDRESS', 'backend')
API_PORT = os.getenv('API_PORT', 80)

st.title("Sentiment Analysis")
text = st.text_area("Enter your thoughts...")

fetch_results = st.button("Check Sentiment")

if fetch_results:
    try:
        if text == "":
            raise ValueError("Empty text")
        reply = requests.get(f"http://{API_ADDRESS}:{API_PORT}/api/?text={text}")
        sentiment = reply.json()['sentiment']
        st.write("Predicted Sentiment: {}".format(sentiment))
        tags = ""
        if (sentiment == 'Negative'):
            tags = "motivational|pain|self-help"
        else:
            tags = "inspirational|leadership|character"

        try:
            quote_reply = requests.get(f"https://api.quotable.io/random?tags={tags}")    
            st.write(f"Checkout this quote: {quote_reply.json()['content']}")
        except:
            st.write("We'd show you a quote if we could connect to the quotable API💨")
    except ValueError:
        st.write("Can't make predictions on empty text, can we? 🤔")
    except:
        st.write("Unable to reach the API at the moment...😞")