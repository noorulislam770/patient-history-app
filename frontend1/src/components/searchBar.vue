<template>
  <div class="mb-4">
    <input ref="searchInput" v-model="searchQuery" type="text"
      placeholder="Search patients ... by , id name phone or email" class="p-2 border rounded w-full"
      @input="handleSearch" @keyup.enter="handleEnter" />
    <div v-if="loading" class="text-center mt-4">Loading...</div>
  </div>
</template>

<script>
import { useDebounceFn } from '@vueuse/core';

export default {
  data() {
    return {
      searchQuery: '',
      loading: false,
    };
  },
  methods: {
    handleSearch: useDebounceFn(async function () {
      if (this.searchQuery.trim() === '') {
        this.$emit('search', []); // Emit an empty array if the search query is empty
        return;
      }

      this.loading = true;
      try {
        const response = await this.$axios.get('/api/search/', {
          params: { query: this.searchQuery },
        });
        this.$emit('search', response.data); // Emit the search results to the parent component
      } catch (error) {
        console.error('Error fetching search results:', error);
        this.$emit('search', []); // Emit an empty array on error
      } finally {
        this.loading = false;
      }
    }, 50), // Debounce for 300ms
    // Handle Enter key press

  },
  mounted() {
    this.$refs.searchInput.focus(); // Focus the search input when the component is mounted
  },
};
</script>
