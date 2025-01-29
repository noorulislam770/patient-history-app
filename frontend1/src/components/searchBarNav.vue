<template>
  <button @click="openModal"
    class="text-white text-lg text-light tracking-wide leading-loose font-semibold hover:text-gray-300">
    Search Patient 🔎
  </button>
  <div>
    <!-- Modal -->
    <div v-if="isModalOpen" style="z-index: 1;"
      class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4" @click="handleOverlayClick">
      <div class="bg-white rounded-lg shadow-lg w-full max-w-2xl p-6" @click.stop>
        <!-- Modal Header -->
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-xl font-bold">Search Patients </h2>
          <button @click="closeModal" class="text-gray-500 hover:text-gray-700">
            &times;
          </button>
        </div>

        <!-- Search Input -->
        <input ref="searchInput" v-model="searchQuery" type="text" placeholder="Search patients..."
          class="p-2 border rounded w-full mb-4" @input="handleSearch" @keyup.enter="handleEnter" />

        <!-- Loading State -->
        <div v-if="loading" class="text-center">
          <p class="text-xl">Loading...</p>
        </div>

        <!-- Search Results -->
        <div v-else-if="results.length === 0" class="text-center">
          <p class="text-xl">No patients found.</p>
        </div>
        <div v-else class="bg-white shadow-md rounded-lg overflow-hidden">
          <table class="w-full">
            <thead>
              <tr class="bg-gray-100 text-left">
                <th class="py-3 px-4 font-semibold">ID</th>
                <th class="py-3 px-4 font-semibold">Name</th>
                <th class="py-3 px-4 font-semibold">Age</th>
                <th class="py-3 px-4 font-semibold">Gender</th>
                <th class="py-3 px-4 font-semibold">Mobile No.</th>
                <th class="py-3 px-4 font-semibold">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="patient in results" :key="patient.id" class="border-t border-gray-200 hover:bg-gray-50">
                <td class="py-3 px-4">{{ patient.id }}</td>
                <td class="py-3 px-4">{{ patient.name }}</td>
                <td class="py-3 px-4">{{ patient.age }}</td>
                <td class="py-3 px-4">{{ patient.gender }}</td>
                <td class="py-3 px-4">{{ patient.mobile_no || 'N/A' }}</td>
                <td class="py-3 px-4">
                  <router-link :to="`/patients/${patient.id}`"
                    class="text-blue-500 hover:text-blue-700 transition-colors" @click="closeModal">
                    View Details
                  </router-link>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useDebounceFn } from '@vueuse/core';

export default {
  data() {
    return {
      isModalOpen: false,
      searchQuery: '',
      results: [],
      loading: false,
    };
  },
  methods: {
    openModal() {
      this.isModalOpen = true;
      this.$nextTick(() => {
        this.$refs.searchInput.focus();
        window.addEventListener('keydown', this.handleKeydown);
      });
    },
    closeModal() {
      this.isModalOpen = false;
      this.searchQuery = '';
      this.results = [];
      window.removeEventListener('keydown', this.handleKeydown);
    },
    handleOverlayClick(event) {
      // Close modal when clicking the overlay
      if (event.target === event.currentTarget) {
        this.closeModal();
      }
    },
    handleSearch: useDebounceFn(async function () {
      if (this.searchQuery.trim() === '') {
        this.results = [];
        return;
      }

      this.loading = true;
      try {
        const response = await this.$axios.get('/api/search/', {
          params: { query: this.searchQuery },
        });
        this.results = response.data;
      } catch (error) {
        console.error('Error fetching search results:', error);
        this.results = [];
      } finally {
        this.loading = false;
      }
    }, 300),
    handleEnter() {
      if (this.results.length > 0) {
        const firstPatient = this.results[0];
        this.$router.push(`/patients/${firstPatient.id}`);
        this.closeModal();
      }
    },
    handleKeydown(event) {
      if (event.key === 'Escape') {
        this.closeModal();
      }
    },
  },
};
</script>
