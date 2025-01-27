<template>
  <div>
    <nav class="bg-gradient-to-r from-cyan-500 to-blue-500 p-4">
      <div class="container mx-auto flex justify-between items-center">
        <router-link to="/" class="text-white text-xl font-bold">Dot Dentistry - Dental Care</router-link>
        <div class="space-x-4">
          <router-link to="/" class="text-white hover:text-gray-200">Home</router-link>
          <router-link to="/patients" class="text-white hover:text-gray-200">Patients</router-link>
          <router-link to="/patients/add" class="text-white hover:text-gray-200">Add Patient</router-link>
          <SearchBarNav />
        </div>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<script>
import SearchBarNav from './components/SearchBarNav.vue';

export default {
  components: {
    SearchBarNav,
  },
  name: 'App',
};
</script>
