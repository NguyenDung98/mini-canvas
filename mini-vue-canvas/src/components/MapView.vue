<script setup>
import { onMounted } from 'vue'
import mapboxgl from 'mapbox-gl'

// Use environment variable for token
mapboxgl.accessToken = import.meta.env.VITE_MAPBOX_TOKEN
const apiBase = import.meta.env.VITE_API_BASE_URL;

onMounted(() => {
  const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    zoom: 0,
  })

  // Request data from the API
  let url = apiBase ? `${apiBase}/api/events/` : './mock/events.json';
  fetch(url)
    .then(response => response.json())
    .then(data => {
      data.forEach(event => {
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
      });
    });
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
