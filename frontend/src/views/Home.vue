<template>
  <div class="home">
    <vuemodoro/>
  </div>
</template>

<script>
// @ is an alias to /src
import Vuemodoro from '@/components/Vuemodoro.vue'

export default {
  name: 'Home',
  components: {
    Vuemodoro
  }
}
</script>
