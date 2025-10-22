import streamlit as st
pages = [
 st.Page("page_home.py", title="專案首頁", icon="🐕"),
 st.Page("page_map.py", title="互動地圖瀏覽", icon="😍"),
 st.Page("page_about.py", title="關於我們", icon="🌷")
]

with st.sidebar:
 st.title("App導覽")
 selected_page = st.navigation(pages)

selected_page.run()