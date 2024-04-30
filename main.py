import streamlit as st
import geopandas as gpd
import fiona

fiona.drvsupport.supported_drivers['libkml'] = 'rw'
fiona.drvsupport.supported_drivers['LIBKML'] = 'rw'

def converter_kmz_para_geodataframe(arquivo_kmz):
    gdf = gpd.read_file(arquivo_kmz)
    
    if len(gdf) != 1:
        raise ValueError("O GeoDataFrame deve ter apenas uma linha.")
    
    gdf['centroid'] = gdf.centroid
    
    return gdf

st.markdown("## Captura de ponto geográfico")

arquivo_kmz = st.file_uploader("Selecione o arquivo KMZ/KML", type=['kmz', 'kml'])

if arquivo_kmz is not None:
    try:
        gdf = converter_kmz_para_geodataframe(arquivo_kmz)
        centroid = gdf['centroid'].squeeze() 
        st.write(f"Centroid capturado: {centroid.y, centroid.x}")
    except Exception as e:
        st.error("Erro ao processar o arquivo KMZ/KML: " + str(e))
