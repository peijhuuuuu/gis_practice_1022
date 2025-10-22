import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd 
st.set_page_config(layout="wide")
st.title("Leafmap + GeoPandas (向量)")

url ="https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"

gdf = gpd.read_file(url)

st.dataframe(gdf.head())
basemap_options = [
    "OpenStreetMap",
    "OpenTopoMap",
    "Esri.WorldImagery",
    "CartoDB.Positron",
]
selected_basemap = st.selectbox("選擇底圖", basemap_options, index=1)
m = leafmap.Map(center=[24.0, 121.0], zoom=7) 
m.add_basemap(selected_basemap)

m.add_gdf(
 gdf,
 layer_name="全球國界(Vector)",
 style={"fillOpacity": 0, "color": "black", "weight": 0.5}, # ún}
 highlight=False
)
m.add_layer_control()
m.to_streamlit(height=700)