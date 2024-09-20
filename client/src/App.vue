<template>
  <div id="app">
    <h1>Real-time Object Detection</h1>
    <CameraStream />
  </div>
</template>

<script>
import CameraStream from './components/CameraStream.vue'

export default {
  name: 'App',
  components: {
    CameraStream
  }
}
</script>
