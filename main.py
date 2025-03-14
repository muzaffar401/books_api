import streamlit as st
import requests

def fetch_books(query):
    API_KEY = "AIzaSyCuJyV-tEQnDEDWPL5pm9c7Twz8khbSfk4"  # Replace with your actual API key
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("items", [])
    return []

def display_books(books):
    for book in books:
        volume_info = book.get("volumeInfo", {})
        title = volume_info.get("title", "No Title")
        authors = ", ".join(volume_info.get("authors", ["Unknown Author"]))
        description = volume_info.get("description", "No description available.")
        thumbnail = volume_info.get("imageLinks", {}).get("thumbnail", "")
        
        with st.container():
            col1, col2 = st.columns([1, 3])
            if thumbnail:
                col1.image(thumbnail, use_container_width=True)
            col2.subheader(title)
            col2.write(f"**Author(s):** {authors}")
            col2.write(description[:300] + "...")
            col2.write("---")

def main():
    st.title("📚 Google Books Search")
    query = st.text_input("Search for a book:", "Python Programming")
    if st.button("Search"):
        books = fetch_books(query)
        if books:
            display_books(books)
        else:
            st.write("No books found. Try another search term.")

if __name__ == "__main__":
    main()
