import streamlit as st
import pandas as pd
st.title("Streamlit 核心 Widgets")
with st.sidebar:
 st.header("這裡是側邊欄")
 option = st.selectbox(
 "你最喜歡的GIS軟體?",
 ("QGIS", "ArcGIS", "ENVI", "GRASS")
 )
 year = st.slider("你所選擇的年份", 1990, 2030, 2024)

st.write(f"你選的軟體是: {option}")
st.write(f"你選的年份是: {year}")

if st.button("點我顯示氣球"):
 st.balloons()

uploaded_file = st.file_uploader(
 "上傳你的Shapefile (.zip) 或 GeoTIFF (.tif) 或 GeoJSON (.json)",
 type=["zip", "tif", "json"]
)
if uploaded_file is not None:
 st.success(f"你上傳了: {uploaded_file.name} (大小: {uploaded_file.size} bytes)")