<template>
  <div>
    <nav class="bg-blue-600 p-4">
      <div class="container mx-auto flex justify-between items-center">
        <router-link to="/" class="text-white text-xl font-bold">Dental Clinic</router-link>
        <div class="space-x-4">
          <router-link to="/" class="text-white hover:text-gray-200">Home</router-link>
          <router-link to="/about" class="text-white hover:text-gray-200">About</router-link>
          <router-link to="/patients" class="text-white hover:text-gray-200">Patients</router-link>
          <router-link to="/patients/add" class="text-white hover:text-gray-200">Add Patient</router-link>
        </div>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>
