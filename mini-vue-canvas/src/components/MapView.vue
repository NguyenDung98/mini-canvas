<script setup>
import { onMounted } from 'vue'
import mapboxgl from 'mapbox-gl'

// Use environment variable for token
mapboxgl.accessToken = import.meta.env.VITE_MAPBOX_TOKEN
const data = [
  {
    "id": "evt-001",
    "timestamp": "2023-10-27T10:00:00Z",
    "location": {
      "latitude": 34.0522,
      "longitude": -118.2437
    },
    "severity": "high",
    "description": "Unidentified vessel detected off the coast of Los Angeles."
  },
  {
    "id": "evt-002",
    "timestamp": "2023-10-27T11:30:00Z",
    "location": {
      "latitude": 40.7128,
      "longitude": -74.0060
    },
    "severity": "medium",
    "description": "Anomalous communication signal intercepted near New York City."
  },
  {
    "id": "evt-003",
    "timestamp": "2023-10-27T12:15:00Z",
    "location": {
      "latitude": 48.8566,
      "longitude": 2.3522
    },
    "severity": "low",
    "description": "Routine satellite pass over Paris confirms normal activity."
  },
  {
    "id": "evt-004",
    "timestamp": "2023-10-27T14:00:00Z",
    "location": {
      "latitude": 35.6895,
      "longitude": 139.6917
    },
    "severity": "high",
    "description": "Cybersecurity breach detected in Tokyo financial district."
  }
]
onMounted(() => {
  const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    zoom: 0,
  })

  data.forEach(event => {
    const markerEl = document.createElement('div');
    markerEl.className = 'marker';
    markerEl.style.backgroundColor = event.severity === 'high' ? 'red' : event.severity === 'medium' ? 'orange' : 'green';

    const popup = new mapboxgl.Popup({ offset: 25 })
      .setHTML(`<strong>Time:</strong> ${new Date(event.timestamp).toLocaleString()}<br>
                <strong>Severity:</strong> ${event.severity}<br>
                <span>${event.description}</span>`);

    new mapboxgl.Marker(markerEl)
      .setLngLat([event.location.longitude, event.location.latitude])
      .setPopup(popup)
      .addTo(map);
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
