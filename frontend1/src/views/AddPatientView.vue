<template>
    <div class="p-4">
      <h1 class="text-2xl font-bold mb-4">Add New Patient</h1>
      <form @submit.prevent="submitForm" class="space-y-4">
        <input v-model="patient.name" placeholder="Name" class="p-2 border rounded w-full" />
        <input v-model="patient.age" placeholder="Age" class="p-2 border rounded w-full" />
        <input v-model="patient.gender" placeholder="Gender" class="p-2 border rounded w-full" />
        <input v-model="patient.address" placeholder="Address" class="p-2 border rounded w-full" />
        <input v-model="patient.mobile_no" placeholder="Mobile No" class="p-2 border rounded w-full" />
        <input v-model="patient.email" placeholder="Email" class="p-2 border rounded w-full" />
        <input v-model="patient.profession" placeholder="Profession" class="p-2 border rounded w-full" />
        <input v-model="patient.referred_by" placeholder="Referred By" class="p-2 border rounded w-full" />
        <button type="submit" class="p-2 bg-blue-500 text-white rounded">Submit</button>
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
    methods: {
      async submitForm() {
        try {
          const response = await this.$axios.post('/api/patients/', this.patient);
          alert('Patient added successfully!');
          this.$router.push('/patients'); // Redirect to patient list
        } catch (error) {
          console.error('Error adding patient:', error);
          alert('Failed to add patient.');
        }
      },
    },
  };
  </script>
