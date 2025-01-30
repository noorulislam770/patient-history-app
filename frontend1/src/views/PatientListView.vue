<template>
  <div class="container shadow-xl shadow-cyan-500/50 rounded-xl mt-4 max-w-5xl mx-auto">
    <div class="text-center bg-gradient-to-r rounded-t-xl from-cyan-500 to-blue-500 pt-3 pb-1">
      <h2 class="text-3xl font-semibold text-white mb-4 text-gray-800">Patient List</h2>
    </div>
    <SearchBar class="mx-2 border-2 border-gray-400 rounded-lg mt-2" @search="handleSearch" />

    <div v-if="loading" class="text-center py-12">
      <p class="text-xl text-gray-600">Loading patients...</p>
    </div>

    <div v-else-if="patients.length === 0" class="text-center py-12">
      <p class="text-xl text-gray-600">No patients found.</p>
    </div>

    <div v-else class="bg-white shadow-lg overflow-hidden">
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
            class="border-t border-gray-100 hover:bg-gray-300 transition-colors duration-150">
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

      <!-- Pagination Controls -->
      <div class="flex justify-between items-center px-6 py-4 bg-gray-50">
        <div class="text-gray-600">
          Showing {{ currentPage * pageSize - pageSize + 1 }} to
          {{ Math.min(currentPage * pageSize, totalItems) }} of {{ totalItems }} entries
        </div>
        <div class="flex space-x-2">
          <button @click="changePage(currentPage - 1)" :disabled="currentPage === 1"
            class="px-4 py-2 border rounded-md hover:bg-gray-100 disabled:opacity-50 disabled:cursor-not-allowed">
            Previous
          </button>
          <button @click="changePage(currentPage + 1)" :disabled="currentPage >= totalPages"
            class="px-4 py-2 border rounded-md hover:bg-gray-100 disabled:opacity-50 disabled:cursor-not-allowed">
            Next
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SearchBar from '@/components/searchBar.vue';

export default {
  components: {
    SearchBar,
  },
  data() {
    return {
      patients: [],
      loading: true,
      currentPage: 1,
      pageSize: 10,
      totalItems: 0,
      totalPages: 1,
    };
  },
  async created() {
    await this.fetchPatients();
  },
  methods: {
    async fetchPatients(query = '') {
      this.loading = true;
      try {
        const response = await this.$axios.get('/api/patients/', {
          params: {
            query,
            page: this.currentPage,
          },
        });

        // Handle paginated response
        this.patients = response.data.results;
        this.totalItems = response.data.count;
        this.totalPages = Math.ceil(response.data.count / this.pageSize);
      } catch (error) {
        console.error('Error fetching patients:', error);
      } finally {
        this.loading = false;
      }
    },
    async changePage(page) {
      if (page >= 1 && page <= this.totalPages) {
        this.currentPage = page;
        await this.fetchPatients();
      }
    },
    async handleSearch(results) {
      // Reset pagination when searching
      this.currentPage = 1;
      if (Array.isArray(results)) {
        // Handle direct search results
        this.patients = results;
        this.totalItems = results.length;
        this.totalPages = 1;
      } else if (results.results) {
        // Handle paginated search results
        this.patients = results.results;
        this.totalItems = results.count;
        this.totalPages = Math.ceil(results.count / this.pageSize);
      }
    },
  },
};
</script>
