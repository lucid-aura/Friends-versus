<template>
  <div id="app">
    <v-app>
        <div class="cover-container d-flex h-100 p-2 mx-auto flex-column">
          <NavBar />
          <Base id="app-container" />
          <Footer />
        </div>
    </v-app>
  </div>
</template>

<script>
  import NavBar from '@/components/NavBar.vue'
  import Base from '@/components/Base.vue'
  import Footer from '@/components/Footer.vue'

  export default {
    name: 'app',
    components: {
      NavBar,
      Base,
      Footer
  },
}
</script>