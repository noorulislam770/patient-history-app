<template>
  <div class="container mx-4 px-4 py-8">
    <h2 class="text-2xl font-bold mb-6">Patient List</h2>
    <SearchBar @search="handleSearch" /> <!-- Listen for the search event -->
    <div v-if="loading" class="text-center">
      <p class="text-xl">Loading patients...</p>
    </div>
    <div v-else-if="patients.length === 0" class="text-center">
      <p class="text-xl">No patients found.</p>
    </div>
    <div v-else class="bg-white shadow-md rounded-lg overflow-hidden">
      <table class="w-full">
        <thead>
          <tr class="bg-gray-100 text-left">
            <th class="py-3 px-4 font-semibold">Name</th>
            <th class="py-3 px-4 font-semibold">Age</th>
            <th class="py-3 px-4 font-semibold">Gender</th>
            <th class="py-3 px-4 font-semibold">Mobile No.</th>
            <th class="py-3 px-4 font-semibold">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="patient in patients" :key="patient.id" class="border-t border-gray-200 hover:bg-gray-50">

            <td class="py-3 px-4">{{ patient.name }}</td>
            <td class="py-3 px-4">{{ patient.age }}</td>
            <td class="py-3 px-4">{{ patient.gender }}</td>
            <td class="py-3 px-4">{{ patient.mobile_no || 'N/A' }}</td>
            <td class="py-3 px-4">
              <router-link :to="`/patients/${patient.id}`" class="text-blue-500 hover:text-blue-700 transition-colors">
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
