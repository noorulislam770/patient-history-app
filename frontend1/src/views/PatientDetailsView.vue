<template>
    <div class="p-4">
      <h1 class="text-2xl font-bold mb-4">Patient Details</h1>
      <div v-if="loading" class="text-center">Loading...</div>
      <div v-else>
        <div class="border p-4 rounded">
          <h3 class="text-xl font-semibold">{{ patient.name }}</h3>
          <p>Age: {{ patient.age }}</p>
          <p>Gender: {{ patient.gender }}</p>
          <p>Address: {{ patient.address }}</p>
          <p>Mobile No: {{ patient.mobile_no }}</p>
          <p>Email: {{ patient.email }}</p>
          <p>Profession: {{ patient.profession }}</p>
          <p>Referred By: {{ patient.referred_by }}</p>
          <router-link :to="`/patients/${patient.id}/edit`" class="text-blue-500 hover:underline">Edit</router-link>
        </div>
      </div>
    </div>
  </template>

  <script>
  export default {
    data() {
      return {
        patient: {},
        loading: true,
      };
    },
    async created() {
      const patientId = this.$route.params.id;
      try {
        const response = await this.$axios.get(`/api/patients/${patientId}/`);
        this.patient = response.data;
      } catch (error) {
        console.error('Error fetching patient:', error);
      } finally {
        this.loading = false;
      }
    },
  };
  </script>
