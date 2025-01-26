<template>
  <div class="min-h-screen bg-gray-50 py-8 px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl mx-auto">
      <!-- Header -->
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold text-blue-700 border-b-2 border-blue-700 pb-2 inline-block">
          DENTISTRY
        </h1>
        <h2 class="mt-2 text-md text-gray-600">Patient Details</h2>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="text-center">
        <p class="text-gray-600">Loading patient details...</p>
      </div>

      <!-- Error State -->
      <div v-if="error" class="text-center text-red-600">
        <p>{{ error }}</p>
      </div>

      <!-- Patient Details Form (Read-Only) -->
      <form v-if="!loading && !error" class="space-y-6">
        <!-- Essential Information Card -->
        <div class="bg-white shadow rounded-lg p-6">
          <h2 class="text-xl font-semibold text-gray-800 mb-4">Essential Information</h2>
          <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
            <div>
              <label class="block text-sm font-medium text-gray-700">Pateint ID # </label>
              <input v-model="patient.id" type="text" readonly
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm bg-gray-100 cursor-not-allowed">
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Name *</label>
              <input v-model="patient.name" type="text" readonly
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm bg-gray-100 cursor-not-allowed">
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Age *</label>
              <input v-model="patient.age" type="number" readonly
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm bg-gray-100 cursor-not-allowed">
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Gender</label>
              <input v-model="patient.gender" type="text" readonly
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm bg-gray-100 cursor-not-allowed">
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">S/D/W of, Self </label>
              <input v-model="patient.guardian_name" type="text" readonly
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm bg-gray-100 cursor-not-allowed">
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Profession </label>
              <input v-model="patient.profession" type="text" readonly
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm bg-gray-100 cursor-not-allowed">
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Referred By </label>
              <input v-model="patient.referred_by" type="text" readonly
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm bg-gray-100 cursor-not-allowed">
            </div>
            <div class="md:col-span-2">
              <label class="block text-sm font-medium text-gray-700">Address *</label>
              <textarea v-model="patient.address" readonly rows="2"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm bg-gray-100 cursor-not-allowed"></textarea>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Mobile No. *</label>
              <input v-model="patient.mobile_no" type="tel" readonly
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm bg-gray-100 cursor-not-allowed">
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Email</label>
              <input v-model="patient.email" type="email" readonly
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm bg-gray-100 cursor-not-allowed">
            </div>
          </div>
        </div>

        <!-- Dental History Card -->
        <div class="bg-white shadow rounded-lg p-6">
          <h2 class="text-xl font-semibold text-gray-800 mb-4">Dental History</h2>
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700">Current dental concerns</label>
              <textarea v-model="patient.dental_concerns" readonly rows="2"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm bg-gray-100 cursor-not-allowed"></textarea>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Discomfort of Pain</label>
              <textarea v-model="patient.discomfort_of_pain" readonly rows="2"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm bg-gray-100 cursor-not-allowed"></textarea>
            </div>
            <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
              <div>
                <label class="block text-sm font-medium text-gray-700">Last dental examination</label>
                <input v-model="patient.last_dental_exam" type="date" readonly
                  class="mt-1 block w-full rounded-md border-gray-300 shadow-sm bg-gray-100 cursor-not-allowed">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Last dental X-ray</label>
                <input v-model="patient.last_dental_xray" type="date" readonly
                  class="mt-1 block w-full rounded-md border-gray-300 shadow-sm bg-gray-100 cursor-not-allowed">
              </div>
            </div>
          </div>
        </div>

        <!-- Medical History Card -->
        <div class="bg-white shadow rounded-lg p-6">
          <h2 class="text-xl font-semibold text-gray-800 mb-4">Medical History</h2>
          <div class="space-y-4">
            <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
              <div>
                <label class="block text-sm font-medium text-gray-700">Current medications</label>
                <input v-model="patient.medications" type="text" readonly
                  class="mt-1 block w-full rounded-md border-gray-300 shadow-sm bg-gray-100 cursor-not-allowed">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Physician's name</label>
                <input v-model="patient.physician_name" type="text" readonly
                  class="mt-1 block w-full rounded-md border-gray-300 shadow-sm bg-gray-100 cursor-not-allowed">
              </div>
            </div>

            <!-- Medical Conditions Checkboxes -->
            <div class="space-y-3">
              <h3 class="text-sm font-medium text-gray-700">Medical Conditions</h3>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                <label class="flex items-center space-x-2">
                  <input type="checkbox" v-model="patient.diabetes" disabled class="rounded text-blue-600">
                  <span class="text-sm">Diabetes</span>
                </label>
                <label class="flex items-center space-x-2">
                  <input type="checkbox" v-model="patient.tuberculosis" disabled class="rounded text-blue-600">
                  <span class="text-sm">Tuberculosis</span>
                </label>
                <label class="flex items-center space-x-2">
                  <input type="checkbox" v-model="patient.high_blood_pressure" disabled class="rounded text-blue-600">
                  <span class="text-sm">High Blood Pressure</span>
                </label>
                <label class="flex items-center space-x-2">
                  <input type="checkbox" v-model="patient.hepatitis" disabled class="rounded text-blue-600">
                  <span class="text-sm">Hepatitis</span>
                  <span v-if="patient.hepatitis && patient.hepatitis_type"> ({{ patient.hepatitis_type }})</span>
                </label>
                <label class="flex items-center space-x-2">
                  <input type="checkbox" v-model="patient.rheumatic_fever" disabled class="rounded text-blue-600">
                  <span class="text-sm">Rheumatic Fever</span>
                </label>
                <label class="flex items-center space-x-2">
                  <input type="checkbox" v-model="patient.excessive_bleeding" disabled class="rounded text-blue-600">
                  <span class="text-sm">Excessive Bleeding</span>
                </label>
              </div>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700">Allergies</label>
              <textarea v-model="patient.allergies" readonly rows="2"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm bg-gray-100 cursor-not-allowed"></textarea>
            </div>

            <!-- Pregnancy Question -->
            <div class="border-t pt-4">
              <label class="block text-sm font-medium text-gray-700 mb-2">For females only:</label>
              <div class="flex items-center space-x-4">
                <span class="text-sm">Are you pregnant?</span>
                <label class="flex items-center space-x-2">
                  <input type="radio" v-model="patient.is_pregnant" :value="true" disabled class="text-blue-600">
                  <span class="text-sm">Yes</span>
                </label>
                <label class="flex items-center space-x-2">
                  <input type="radio" v-model="patient.is_pregnant" :value="false" disabled class="text-blue-600">
                  <span class="text-sm">No</span>
                </label>
              </div>
            </div>
          </div>
        </div>

        <!-- Edit Button -->
        <div class="text-center">
          <button type="button" @click="goToEditPage"
            class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
            Edit Patient
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      patient: {
        id: '',
        name: '',
        age: '',
        address: '',
        mobile_no: '',
        email: '',
        gender: '',
        profession: '',
        referred_by: '',
        dental_concerns: '',
        last_dental_exam: '',
        last_dental_xray: '',
        medications: '',
        physicianName: '',
        hepatitis_type: '',
        diabetes: false,
        tuberculosis: false,
        high_blood_pressure: false,
        hepatitis: false,
        rheumatic_fever: false,
        excessive_bleeding: false,

        allergies: '',
        is_pregnant: null,
      },
      loading: true,
      error: null,
    };
  },
  watch: {
    // Watch for changes in the route parameter `:id`
    '$route.params.id': {
      handler: 'fetchPatientData', // Call `fetchPatientData` when `:id` changes
      immediate: true, // Trigger the handler immediately on component creation
    },
  },
  async created() {
    const patientId = this.$route.params.id;
    try {
      const response = await this.$axios.get(`/api/patients/${patientId}/`);
      this.patient = response.data;
      console.log(this.patient);
    } catch (error) {
      console.error('Error fetching patient:', error);
      this.error = 'Failed to load patient data';
    } finally {
      this.loading = false;
    }
  },
  methods: {
    goToEditPage() {
      this.$router.push(`/patients/${this.$route.params.id}/edit`);
    },
    async fetchPatientData() {
      const patientId = this.$route.params.id;
      this.loading = true;
      try {
        const response = await this.$axios.get(`/api/patients/${patientId}/`);
        this.patient = response.data;
      } catch (error) {
        console.error('Error fetching patient details:', error);
      } finally {
        this.loading = false;
      }
    },
    handleSearch(results) {
      this.patients = results; // Update the patients list with search results
    },
    handleEnter() {
      if (this.patients.length > 0) {
        const firstPatient = this.patients[0]; // Get the first patient
        this.$router.push(`/patients/${firstPatient.id}`); // Navigate to the first patient
      }
    },
  },
};
</script>

<style scoped>
/* Add any custom styles here */
</style>
