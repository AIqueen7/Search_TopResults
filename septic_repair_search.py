#use the Google Search API in a Streamlit app to search for "septic repair in Alberta" and retrieve the top results:
#AIQueen

import streamlit as st
import requests

# Set your API key and CX
api_key = "AIzaSyBJS7e3XnWLC5IJN4YtJC7QgrUHGEa489U"
cx = "95963cf6977654301"

st.set_page_config(page_title="Septic Repair Search", page_icon=":guardsman:", layout="wide")

# Create a function to send the search request
def search(query):
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}"
    response = requests.get(url)
    results = response.json().get("items", [])
    return results

# Create a main function
def main():
    st.title("Septic Repair Search")
    query = st.text_input("Enter search query (ex: septic repair in Alberta)")

    if st.button("Search"):
        results = search(query)

        if not results:
            st.error("No results found. Please try again with a different query.")
        else:
            st.header("Results:")
            for result in results:
                title = result.get("title", "")
                link = result.get("link", "")
                st.markdown(f"- [{title}]({link})")

# Run the main function
if __name__ == "__main__":
    main()