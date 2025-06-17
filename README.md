# Carrt Mapping Dashboard

An interactive geospatial visualization tool built for nonprofits and mobile food banks to identify and serve vulnerable communities efficiently. This platform integrates **Community Vulnerability Index (CVI)** scoring, **K-Means clustering**, and optional **linear regression** to guide equitable resource allocation.

## Features

- Leaflet-powered interactive map with styled markers and zones
- CVI scoring to assess community needs based on socioeconomic indicators
- K-Means clustering to group stops into priority service zones (A–D)
- Optional linear regression to model demand or optimize routing
- Custom popups with address, organization name, and zone info
- Lightweight, front-end-only implementation (no server required)

## Demo

> To preview the map locally:
1. Clone this repository.
2. Place your `stopsnzones.json` file in the `data/` folder.
3. Open `index.html` in a modern web browser.

## File Structure

/project-root
├── index.html # Main application page
├── data/
│ ├── stops_n_zones.json # GeoJSON Point features with stop info and zone IDs
│ ├── CVI.json # GeoJSON data with vulnerability scoring
│ └── municipal_boundary.json# GeoJSON polygon of the service boundary
└── README.md # Project documentation

## Data Format

The app expects a valid GeoJSON file (`stopsnzones.json`) with Point features. Each feature should have at least the following structure:

```json
{
  "type": "Feature",
  "properties": {
    "NAME": "Example Site",
    "STREET": "123 Main St",
    "zone_id": 0,
    "CVI": 0.82
  },
  "geometry": {
    "type": "Point",
    "coordinates": [-10624995.2202, 3510718.3868]
  }
}
