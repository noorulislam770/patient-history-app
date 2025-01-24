<template>
    <div class="p-4">
      <h1 class="text-2xl font-bold mb-4">Edit Patient</h1>
      <form @submit.prevent="submitForm" class="space-y-4">
        <input v-model="patient.name" placeholder="Name" class="p-2 border rounded w-full" />
        <input v-model="patient.age" placeholder="Age" class="p-2 border rounded w-full" />
        <input v-model="patient.gender" placeholder="Gender" class="p-2 border rounded w-full" />
        <input v-model="patient.address" placeholder="Address" class="p-2 border rounded w-full" />
        <input v-model="patient.mobile_no" placeholder="Mobile No" class="p-2 border rounded w-full" />
        <input v-model="patient.email" placeholder="Email" class="p-2 border rounded w-full" />
        <input v-model="patient.profession" placeholder="Profession" class="p-2 border rounded w-full" />
        <input v-model="patient.referred_by" placeholder="Referred By" class="p-2 border rounded w-full" />
        <button type="submit" class="p-2 bg-blue-500 text-white rounded">Update</button>
      </form>
    </div>
  </template>

  <script>
  export default {
    data() {
      return {
        patient: {
          name: '',
          age: '',
          gender: '',
          address: '',
          mobile_no: '',
          email: '',
          profession: '',
          referred_by: '',
        },
      };
    },
    async created() {
      const patientId = this.$route.params.id;
      try {
        const response = await this.$axios.get(`/api/patients/${patientId}/`);
        this.patient = response.data;
      } catch (error) {
        console.error('Error fetching patient:', error);
      }
    },
    methods: {
      async submitForm() {
        try {
          const patientId = this.$route.params.id;
          await this.$axios.put(`/api/patients/${patientId}/`, this.patient);
          alert('Patient updated successfully!');
          this.$router.push('/patients'); // Redirect to patient list
        } catch (error) {
          console.error('Error updating patient:', error);
          alert('Failed to update patient.');
        }
      },
    },
  };
  </script>
