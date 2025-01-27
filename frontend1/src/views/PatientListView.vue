<template>
  <div class="container shadow-xl shadow-cyan-500/50 rounded-xl  mt-4 max-w-5xl mx-auto">
    <div class="text-center bg-gradient-to-r rounded-t-xl from-cyan-500 to-blue-500 pt-3 pb-1 ">
      <h2 class="text-3xl font-semibold text-white  mb-4 text-gray-800">Patient List</h2>
    </div>
    <SearchBar class="mx-2 border-2 border-gray-400 rounded-lg mt-2 " @search="handleSearch" />
    <!-- Listen for the search event -->

    <div v-if="loading" class="text-center py-12">
      <p class="text-xl text-gray-600">Loading patients...</p>
    </div>

    <div v-else-if="patients.length === 0" class="text-center py-12">
      <p class="text-xl text-gray-600">No patients found.</p>
    </div>

    <div v-else class="bg-white shadow-lg  overflow-hidden">
      <table class="w-full">
        <thead>
          <tr class="bg-gray-300 text-left text-gray-700">
            <th class="py-4 px-6 font-semibold uppercase text-sm">ID</th>
            <th class="py-4 px-6 font-semibold uppercase text-sm">Name</th>
            <th class="py-4 px-6 font-semibold uppercase text-sm">Entry Date</th>
            <th class="py-4 px-6 font-semibold uppercase text-sm">Mobile No.</th>
            <th class="py-4 px-6 font-semibold uppercase text-sm">Age</th>
            <th class="py-4 px-6 font-semibold uppercase text-sm">Gender</th>
            <th class="py-4 px-6 font-semibold uppercase text-sm">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="patient in patients" :key="patient.id"
            class="border-t border-gray-100 hover:bg-gray-300 transition-colors duration-150 ">

            <td class="py-4 px-6 text-gray-800">{{ patient.id }}</td>
            <td class="py-4 px-6 text-gray-800 capitalize">{{ patient.name }}</td>
            <td class="py-4 px-6 text-gray-800">{{ patient.entry_date }}</td>
            <td class="py-4 px-6 text-gray-700">{{ patient.mobile_no || 'N/A' }}</td>
            <td class="py-4 px-6 text-gray-700">{{ patient.age }}</td>
            <td class="py-4 px-6 text-gray-700 capitalize">{{ patient.gender }}</td>
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
