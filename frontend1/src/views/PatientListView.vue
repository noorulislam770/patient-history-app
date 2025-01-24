<template>
  <div class="p-4">
    <h1 class="text-2xl font-bold mb-4">Patient List</h1>
    <div v-if="loading" class="text-center text-gray-600">Loading...</div>
    <ul v-else class="space-y-4">
      <li
        v-for="patient in patients"
        :key="patient.id"
        class="border border-gray-200 p-4 rounded-lg shadow-sm hover:shadow-md transition-shadow duration-300"
      >
        <h3 class="text-xl font-semibold text-gray-800 mb-2">{{ patient.name }}</h3>
        <ul class="space-y-2 text-gray-600">
          <li><span class="font-medium">Age:</span> {{ patient.age }}</li>
          <li><span class="font-medium">Gender:</span> {{ patient.gender }}</li>
          <li><span class="font-medium">Mobile No:</span> {{ patient.mobile_no }}</li>
        </ul>
        <router-link
          :to="`/patients/${patient.id}`"
          class="mt-3 inline-block text-blue-500 hover:text-blue-700 hover:underline transition-colors duration-300"
        >
          View Details
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      patients: [],
      loading: true,
    }
  },
  async created() {
    try {
      const response = await this.$axios.get('/api/patients/')
      this.patients = response.data
      console.log(this.patients)
    } catch (error) {
      console.error('Error fetching patients:', error)
    } finally {
      this.loading = false
    }
  },
}
</script>

<style scoped>
/* You can add custom styles here if needed */
</style>
