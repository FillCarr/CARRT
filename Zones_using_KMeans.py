"""
Cluster Points into Zones using KMeans

This script loads point data from a GeoJSON file, applies KMeans clustering
from scikit-learn to group them into geographic zones, and exports the result.

Dependencies:
- geopandas
- matplotlib
- scikit-learn

Author: Philip
Date: 06/16/2025
"""

import geopandas as gpd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# -------- CONFIG --------
INPUT_POINTS_PATH = "stops.json"
OUTPUT_PATH = "stopsnzones.json"
CRS = "EPSG:4326"  # Projected CRS for accurate distance calculation
NUM_CLUSTERS = 5  # Adjust based on how many zones you want

# -------- LOAD DATA --------
print("Loading point data...")
gdf = gpd.read_file(INPUT_POINTS_PATH)
gdf = gdf.to_crs(CRS)  # Reproject for distance-based clustering

# -------- PREP COORDINATES FOR CLUSTERING --------
print("Extracting coordinates...")
gdf["x"] = gdf.geometry.x
gdf["y"] = gdf.geometry.y
coords = gdf[["x", "y"]].values

# -------- RUN KMEANS CLUSTERING --------
print(f"Running KMeans with {NUM_CLUSTERS} clusters...")
kmeans = KMeans(n_clusters=NUM_CLUSTERS, random_state=42)
gdf["zone_id"] = kmeans.fit_predict(coords)

# -------- EXPORT RESULT --------
print(f"Saving clustered GeoJSON to {OUTPUT_PATH}...")
gdf.to_file(OUTPUT_PATH, driver="GeoJSON")

# -------- OPTIONAL: PLOT --------
print("Plotting clusters...")
gdf.plot(column="zone_id", cmap="Set2", legend=True, figsize=(10, 6), markersize=20)
plt.title("KMeans Clustered Zones")
plt.axis("off")
plt.show()
