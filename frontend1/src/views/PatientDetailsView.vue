<template>
  <div class="min-h-screen bg-gray-50 py-8 px-2 sm:px-2 lg:px-4">
    <!-- Main Grid Layout -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 max-w-7xl mx-auto">
      <!-- Procedures Section (2/3 width) -->
      <div class="lg:col-span-2">
        <ProcedureList :patientId="patient.id" :patientName="patient.name" />
      </div>

      <!-- Patient Details Section (1/3 width) -->
      <div class="lg:col-span-1 ">
        <!-- Patient Details Card -->
        <div class="bg-white  shadow-xl shadow-cyan-500/50 shadow-lg rounded-xl p-6 sticky top-8">
          <!-- Header -->
          <div class="text-center  mb-6">
            <h1 class="text-2xl font-bold text-blue-700 border-b-2 border-blue-700 pb-2 inline-block">
              Patient Details
            </h1>
          </div>

          <!-- Loading State -->
          <div v-if="loading" class="text-center py-6">
            <p class="text-gray-600 text-lg">Loading patient details...</p>
          </div>

          <!-- Error State -->
          <div v-if="error" class="text-center py-6">
            <p class="text-red-600 text-lg">{{ error }}</p>
          </div>

          <!-- Patient Details Form (Read-Only) -->
          <form v-if="!loading && !error" class="space-y-6">
            <!-- Essential Information -->
            <div>
              <h2 class="text-xl font-semibold text-gray-800 mb-4">Essential Information</h2>
              <div class="space-y-4">
                <div>
                  <label class="block text-sm font-medium text-gray-600 mb-1">Patient ID #</label>
                  <input v-model="patient.id" type="text" readonly
                    class="mt-1 block w-full rounded-lg border-gray-200 bg-gray-50 text-gray-700 cursor-not-allowed">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-600 mb-1">Name *</label>
                  <input v-model="patient.name" type="text" readonly
                    class="mt-1 block w-full rounded-lg border-gray-200 bg-gray-50 text-gray-700 cursor-not-allowed">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-600 mb-1">Age *</label>
                  <input v-model="patient.age" type="number" readonly
                    class="mt-1 block w-full rounded-lg border-gray-200 bg-gray-50 text-gray-700 cursor-not-allowed">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-600 mb-1">Gender</label>
                  <input v-model="patient.gender" type="text" readonly
                    class="mt-1 block w-full rounded-lg border-gray-200 bg-gray-50 text-gray-700 cursor-not-allowed">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-600 mb-1">Mobile No. *</label>
                  <input v-model="patient.mobile_no" type="tel" readonly
                    class="mt-1 block w-full rounded-lg border-gray-200 bg-gray-50 text-gray-700 cursor-not-allowed">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-600 mb-1">Email</label>
                  <input v-model="patient.email" type="email" readonly
                    class="mt-1 block w-full rounded-lg border-gray-200 bg-gray-50 text-gray-700 cursor-not-allowed">
                </div>
              </div>
            </div>

            <!-- Dental History -->
            <div>
              <h2 class="text-xl font-semibold text-gray-800 mb-4">Dental History</h2>
              <div class="space-y-4">
                <div>
                  <label class="block text-sm font-medium text-gray-600 mb-1">Current dental concerns</label>
                  <textarea v-model="patient.dental_concerns" readonly rows="3"
                    class="mt-1 block w-full rounded-lg border-gray-200 bg-gray-50 text-gray-700 cursor-not-allowed"></textarea>
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-600 mb-1">Last dental examination</label>
                  <input v-model="patient.last_dental_exam" type="date" readonly
                    class="mt-1 block w-full rounded-lg border-gray-200 bg-gray-50 text-gray-700 cursor-not-allowed">
                </div>
              </div>
            </div>

            <!-- Medical History -->
            <div>
              <h2 class="text-xl font-semibold text-gray-800 mb-4">Medical History</h2>
              <div class="space-y-4">
                <div>
                  <label class="block text-sm font-medium text-gray-600 mb-1">Current medications</label>
                  <input v-model="patient.medications" type="text" readonly
                    class="mt-1 block w-full rounded-lg border-gray-200 bg-gray-50 text-gray-700 cursor-not-allowed">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-600 mb-1">Allergies</label>
                  <textarea v-model="patient.allergies" readonly rows="3"
                    class="mt-1 block w-full rounded-lg border-gray-200 bg-gray-50 text-gray-700 cursor-not-allowed"></textarea>
                </div>
              </div>
            </div>

            <!-- Edit Button -->
            <div class="text-center">
              <button type="button" @click="goToEditPage"
                class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-lg text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors">
                Edit Patient
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProcedureList from '@/components/procedureList.vue';

export default {
  components: {
    ProcedureList,
  },
  data() {
    return {
      patient: {
        id: '',
        name: '',
        age: '',
        gender: '',
        mobile_no: '',
        email: '',
        dental_concerns: '',
        last_dental_exam: '',
        medications: '',
        allergies: '',
      },
      loading: true,
      error: null,
    };
  },
  watch: {
    '$route.params.id': {
      handler: 'fetchPatientData',
      immediate: true,
    },
  },
  async created() {
    await this.fetchPatientData();
  },
  methods: {
    async fetchPatientData() {
      const patientId = this.$route.params.id;
      this.loading = true;
      try {
        const response = await this.$axios.get(`/api/patients/${patientId}/`);
        this.patient = response.data;
      } catch (error) {
        console.error('Error fetching patient:', error);
        this.error = 'Failed to load patient data';
      } finally {
        this.loading = false;
      }
    },
    goToEditPage() {
      this.$router.push(`/patients/${this.$route.params.id}/edit`);
    },
  },
};
</script>

<style scoped>
/* Add any custom styles here */
</style>
