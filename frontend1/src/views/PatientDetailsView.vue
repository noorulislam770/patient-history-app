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

      <!-- Patient Details -->
      <div v-if="!loading && !error" class="space-y-6">
        <!-- Essential Information Card -->
        <div class="bg-white shadow rounded-lg p-6">
          <h2 class="text-xl font-semibold text-gray-800 mb-4">Essential Information</h2>
          <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
            <div>
              <label class="block text-sm font-medium text-gray-700">Name</label>
              <p class="mt-1 text-sm text-gray-900">{{ patient.name }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Age</label>
              <p class="mt-1 text-sm text-gray-900">{{ patient.age }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Gender</label>
              <p class="mt-1 text-sm text-gray-900">{{ patient.gender }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Profession</label>
              <p class="mt-1 text-sm text-gray-900">{{ patient.profession }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Referred By</label>
              <p class="mt-1 text-sm text-gray-900">{{ patient.referred_by }}</p>
            </div>
            <div class="md:col-span-2">
              <label class="block text-sm font-medium text-gray-700">Address</label>
              <p class="mt-1 text-sm text-gray-900">{{ patient.address }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Mobile No.</label>
              <p class="mt-1 text-sm text-gray-900">{{ patient.mobile_no }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Email</label>
              <p class="mt-1 text-sm text-gray-900">{{ patient.email }}</p>
            </div>
          </div>
        </div>

        <!-- Dental History Card -->
        <div class="bg-white shadow rounded-lg p-6">
          <h2 class="text-xl font-semibold text-gray-800 mb-4">Dental History</h2>
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700">Current dental concerns</label>
              <p class="mt-1 text-sm text-gray-900">{{ patient.dentalConcerns }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Last dental examination</label>
              <p class="mt-1 text-sm text-gray-900">{{ formatDate(patient.lastExamination) }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Last dental X-ray</label>
              <p class="mt-1 text-sm text-gray-900">{{ formatDate(patient.lastXray) }}</p>
            </div>
          </div>
        </div>

        <!-- Medical History Card -->
        <div class="bg-white shadow rounded-lg p-6">
          <h2 class="text-xl font-semibold text-gray-800 mb-4">Medical History</h2>
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700">Current medications</label>
              <p class="mt-1 text-sm text-gray-900">{{ patient.medications }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Physician's name</label>
              <p class="mt-1 text-sm text-gray-900">{{ patient.physicianName }}</p>
            </div>

            <!-- Medical Conditions -->
            <div>
              <label class="block text-sm font-medium text-gray-700">Medical Conditions</label>
              <div class="mt-1 text-sm text-gray-900">
                <p v-if="patient.diabetes">Diabetes</p>
                <p v-if="patient.tuberculosis">Tuberculosis</p>
                <p v-if="patient.bloodPressure">High Blood Pressure</p>
                <p v-if="patient.hepatitis">Hepatitis (Type: {{ patient.hepatitisType }})</p>
                <p v-if="patient.rheumatic_fever">Rheumatic Fever</p>
                <p v-if="patient.excessive_bleeding">Excessive Bleeding</p>
              </div>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700">Allergies</label>
              <p class="mt-1 text-sm text-gray-900">{{ patient.allergies }}</p>
            </div>

            <!-- Pregnancy Status -->
            <div v-if="patient.gender === 'female'">
              <label class="block text-sm font-medium text-gray-700">Pregnancy Status</label>
              <p class="mt-1 text-sm text-gray-900">{{ patient.isPregnant ? 'Yes' : 'No' }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      patient: {
        name: '',
        age: '',
        address: '',
        mobile_no: '',
        email: '',
        gender: '',
        profession: '',
        referred_by: '',
        dentalConcerns: '',
        lastExamination: '',
        lastXray: '',
        medications: '',
        physicianName: '',
        diabetes: false,
        tuberculosis: false,
        bloodPressure: false,
        hepatitis: false,
        rheumatic_fever: false,
        excessive_bleeding: false,
        allergies: '',
        isPregnant: null,
      },
      loading: true,
      error: null,
    };
  },
  async created() {
    const patientId = this.$route.params.id;
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
  methods: {
    formatDate(dateString) {
      if (!dateString) return 'Not available';
      return new Date(dateString).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
      });
    },
  },
};
</script>

<style scoped>
/* Add any custom styles here */
</style>
