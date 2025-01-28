<!-- src/views/ProcedureDetailsView.vue -->
<template>
  <div class="container  my-4 rounded-xl max-w-3xl mx-auto shadow-xl shadow-cyan-500/50">
    <h1
      class="text-center bg-gradient-to-r rounded-t-xl text-2xl font-semibold text-white from-cyan-500 to-blue-500 p-6">
      Procedure
      Details</h1>
    <div v-if="loading" class="text-center">
      <p class="text-xl">Loading procedure details...</p>
    </div>
    <div v-else class="bg-white shadow-md rounded-lg overflow-hidden p-6">
      <form @submit.prevent="submitForm">
        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700">Date</label>
            <input v-model="form.date" type="date"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500"
              required />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700">Description</label>
            <input v-model="form.description" type="text"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500"
              required />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700">Total Amount </label>
            <input v-model="form.total_amount" type="number"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500"
              required />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700">Amount Paid</label>
            <input v-model="form.amount_paid" type="number"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500"
              required />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700">Balance</label>
            <input v-model="form.balance" type="number"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500"
              required />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700">Notes</label>
            <textarea v-model="form.notes"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500"></textarea>
          </div>
        </div>
        <div class="mt-6">
          <button type="submit" class="p-2 bg-blue-500 text-white rounded">
            Save Changes
          </button>
          <router-link :to="`/patients/${patientId}`" class="p-2 bg-gray-500 text-white rounded ml-2">
            Back to Patient
          </router-link>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {

      form: {
        date: '',
        description: '',
        total_amount: 0,
        amount_paid: 0,
        balance: 0,
        notes: '',

      },
      loading: true,
      patientId: null,
    };
  },
  async created() {
    await this.fetchProcedure();
  },
  methods: {
    async fetchProcedure() {
      const procedureId = this.$route.params.procedureId;
      console.log(procedureId);
      console.log("procedureId : ", procedureId)
      try {
        const response = await this.$axios.get(`/api/procedures/${procedureId}/`);
        this.form = response.data;
        this.patientId = response.data.patient;
      } catch (error) {
        console.error('Error fetching procedure details:', error);
      } finally {
        this.loading = false;
      }
    },
    async submitForm() {
      const procedureId = this.$route.params.procedureId;
      try {
        await this.$axios.put(`/api/procedures/${procedureId}/`, this.form);
        alert('Procedure updated successfully!');
        this.$router.push(`/patients/${this.patientId}`);
      } catch (error) {
        console.error('Error updating procedure:', error);
        alert('Failed to update procedure.');
      }
    },
  },
};
</script>
