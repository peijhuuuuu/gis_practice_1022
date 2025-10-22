import streamlit as st

st.title("歡迎來到我的gis專頁")
st.write("這是一個互動地圖")

video_url = "https://i.imgur.com/1GoAB0C.mp4"
st.write(f"正在撥放影片 {video_url}")
st.video(video_url)

image_url = "https://i.imgur.com/uf1T4ND.png"
st.image(image_url)