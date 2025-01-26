<template>
  <div class="container px-8 py-8">
    <h2 class="text-3xl font-bold mb-8 text-gray-800">Patient List</h2>
    <SearchBar @search="handleSearch" class="mb-8" /> <!-- Listen for the search event -->

    <div v-if="loading" class="text-center py-12">
      <p class="text-xl text-gray-600">Loading patients...</p>
    </div>

    <div v-else-if="patients.length === 0" class="text-center py-12">
      <p class="text-xl text-gray-600">No patients found.</p>
    </div>

    <div v-else class="bg-white shadow-lg rounded-lg overflow-hidden">
      <table class="w-full">
        <thead>
          <tr class="bg-gray-50 text-left text-gray-700">
            <th class="py-4 px-6 font-semibold uppercase text-sm">Name</th>
            <th class="py-4 px-6 font-semibold uppercase text-sm">Age</th>
            <th class="py-4 px-6 font-semibold uppercase text-sm">Gender</th>
            <th class="py-4 px-6 font-semibold uppercase text-sm">Mobile No.</th>
            <th class="py-4 px-6 font-semibold uppercase text-sm">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="patient in patients" :key="patient.id"
            class="border-t border-gray-100 hover:bg-gray-50 transition-colors">
            <td class="py-4 px-6 text-gray-800">{{ patient.name }}</td>
            <td class="py-4 px-6 text-gray-700">{{ patient.age }}</td>
            <td class="py-4 px-6 text-gray-700">{{ patient.gender }}</td>
            <td class="py-4 px-6 text-gray-700">{{ patient.mobile_no || 'N/A' }}</td>
            <td class="py-4 px-6">
              <router-link :to="`/patients/${patient.id}`"
                class="text-blue-500 hover:text-blue-700 transition-colors font-semibold">
                View Details
              </router-link>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue';

export default {
  components: {
    SearchBar,
  },
  data() {
    return {
      patients: [], // Holds the list of patients
      loading: true, // Loading state
    };
  },
  async created() {
    // Fetch all patients when the component is created
    await this.fetchPatients();
  },
  methods: {
    async fetchPatients(query = '') {
      this.loading = true;
      try {
        const response = await this.$axios.get('/api/patients/', {
          params: { query }, // Pass the search query to the backend
        });
        this.patients = response.data; // Update the patients list
      } catch (error) {
        console.error('Error fetching patients:', error);
      } finally {
        this.loading = false;
      }
    },
    handleSearch(results) {
      this.patients = results; // Update the patients list with search results
    },
  },
};
</script>

<style>
/* Optional: Add custom styles if needed */
</style>
