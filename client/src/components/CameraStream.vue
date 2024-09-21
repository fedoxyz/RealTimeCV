<template>
  <div>
    <video ref="video" width="640" height="480" autoplay></video>
    <canvas ref="canvas" width="640" height="480" style="display:none;"></canvas>
    <img :src="processedImageSrc" width="640" height="480" alt="Processed image" />
  </div>
</template>

<script setup>
  import { ref, onMounted, onUnmounted } from 'vue';
  import { io } from 'socket.io-client';

  const video = ref(null);
  const canvas = ref(null);
  const processedImageSrc = ref('');

  const ctx = ref(null);

  let socket;
  let streamInterval;

  const constraints = ref({
    audio: false,
    video: true
  })

  const startStream = async () => {
    ctx.value = canvas.value.getContext("2d");

    await navigator.mediaDevices
      .getUserMedia(constraints.value)
      .then(SetStream)
      .catch(error => {
        console.error('Error accessing the camera:', error);
      });
  };

  const SetStream = (stream) => {
    video.value.srcObject = stream;
    video.value.play()

    requestAnimationFrame(Draw)
  }

  function Draw() {
    ctx.value.drawImage(video.value, 0, 0, canvas.value.width, canvas.value.height)

    requestAnimationFrame(Draw);
  }

  const sendImageToServer = () => {
    const imageData = canvas.value.toDataURL('image/jpeg');
    socket.emit('image', imageData);
  };

  onMounted(() => {
    socket = io('http://192.168.1.103:5000'); // http://localhost:5000 
    socket.on('processed_image', (processedImage) => {
      processedImageSrc.value = 'data:image/jpeg;base64,' + processedImage;
    });
    if (video.value && canvas.value) {
      console.log("video.value");
      startStream();
      streamInterval = setInterval(sendImageToServer, 100);  // Adjust interval in ms ?
    }
  });

  onUnmounted(() => {
    clearInterval(streamInterval);
    if (socket) socket.disconnect();
  });

</script>
