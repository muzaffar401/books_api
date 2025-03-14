import streamlit as st
import requests

def fetch_books(query):
    API_KEY = st.secrets["API_KEY"]  # Get API key from secrets
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={API_KEY}&country=US"
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
        info_link = volume_info.get("infoLink", "#")

        with st.container():
            col1, col2 = st.columns([1, 3])
            if thumbnail:
                col1.image(thumbnail, use_container_width=True)  # ✅ Updated parameter
            col2.subheader(title)
            col2.write(f"**Author(s):** {authors}")
            col2.write(description[:300] + "...")
            col2.markdown(f"[📖 More Info]({info_link})", unsafe_allow_html=True)
            st.write("---")

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
