<script setup>
import MapView from './views/MapView.vue';
</script>

<template>
  <div id="app">
    <MapView />
  </div>
</template>

<style scoped>
@import 'mapbox-gl/dist/mapbox-gl.css';

#app {
  margin: 5%;
}
</style>
