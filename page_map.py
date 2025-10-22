import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd # / GeoPandas
st.set_page_config(layout="wide")
st.title("Leafmap + GeoPandas (Uß)")

url =
"https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zi
p"

gdf = gpd.read_file(url)

st.dataframe(gdf.head())

m = leafmap.Map(center=[0, 0])

m.add_gdf(
 gdf,
 layer_name="_} (Vector)",
 style={"fillOpacity": 0, "color": "black", "weight": 0.5}, # ún}
 highlight=False
)
m.add_layer_control()
m.to_streamlit(height=700)