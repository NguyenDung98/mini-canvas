<script setup>
import { onMounted } from 'vue'
import mapboxgl from 'mapbox-gl'

mapboxgl.accessToken = import.meta.env.VITE_MAPBOX_TOKEN
const BASE_URL = import.meta.env.BASE_URL;
const API_BASE = import.meta.env.VITE_API_BASE_URL;

function createMarker(event, map) {
  const markerEl = document.createElement('div');
  markerEl.className = 'marker';
  markerEl.style.backgroundColor = event.severity === 'high' ? 'red' : event.severity === 'medium' ? 'gold' : 'green';

  const popup = new mapboxgl.Popup({ offset: 25 })
    .setHTML(`<strong>Time:</strong> ${new Date(event.timestamp).toLocaleString()}<br>
          <strong>Severity:</strong> ${event.severity}<br>
          <span>${event.description}</span>`);

  new mapboxgl.Marker(markerEl)
    .setLngLat([event.location.longitude, event.location.latitude])
    .setPopup(popup)
    .addTo(map);
}

async function fetchEvents(url) {
  const response = await fetch(url);
  return response.json();
}

onMounted(async () => {
  const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    zoom: 0,
  })

  let url = API_BASE ? `${API_BASE}/api/events/` : `${BASE_URL}/mock/events.json`;
  const data = await fetchEvents(url);
  data.forEach(event => createMarker(event, map));
})
</script>

<template>
  <div id="map" class="map-container"></div>
</template>

<style>
.map-container {
  margin: auto;
  width: 90%;
  height: 80vh;
}

.marker {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  cursor: pointer;
}
</style>