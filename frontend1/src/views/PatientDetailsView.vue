<template>
  <div class="min-h-screen bg-gray-50 py-8 px-2 sm:px-2 lg:px-4">
    <!-- Main Grid Layout -->
    <div class="grid grid-cols-1 lg:grid-cols-8 gap-4 mx-8">
      <!-- Procedures Section (2/3 width) -->
      <div class="lg:col-span-5">
        <ProcedureList v-if="patient.id" :patientId="patient.id" :patientName="patient.name" />
      </div>

      <!-- Patient Details Section (1/3 width) -->
      <div class="lg:col-span-3 mt-2">
        <!-- Patient Details Card -->
        <div class="bg-white shadow-xl shadow-cyan-500/50 shadow-lg rounded-xl mt-6 pb-4 sticky top-8">
          <!-- Header -->
          <div class="text-center bg-gradient-to-r rounded-t-xl from-cyan-500 to-blue-500 p-6">
            <h1 class="text-xl font-semibold text-white pb-3 inline-block">
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

          <div v-if="!loading && !error" class="space-y-8">
            <!-- Essential Information Card -->
            <div class="bg-white shadow-lg rounded-xl p-6">
              <p class="text-xs font-semibold text-gray-600  border-b">Patient<span
                  class=" block text-2xl font-bold text-gray-800 mb-6 border-b capitalize pb-2">{{
                    patient.name }}</span></p>
              <div class="space-y-4 grid grid-cols-1 lg:grid-cols-2 gap-4">
                <div>
                  <p class="text-sm font-medium text-gray-600 mb-1">Patient ID #</p>
                  <h3 class="text-xl">{{ patient.id }}</h3>
                </div>
                <div>
                  <p class="text-sm font-medium text-gray-600 mb-1">Age</p>
                  <h3 class="text-lg">{{ patient.age }}</h3>
                </div>
                <div>
                  <p class="text-xs font-medium text-gray-600 mb-1">Gender</p>
                  <h3 class="text-lg capitalize capitalize">{{ patient.gender }}</h3>
                </div>
                <div>
                  <p class="text-xs font-medium text-gray-600 mb-1">Mobile No.</p>
                  <h3 class="text-lg capitalize">{{ patient.mobile_no }}</h3>
                </div>
                <div>
                  <p class="text-xs font-medium text-gray-600 mb-1">Email</p>
                  <h3 class="text-lg">{{ patient.email }}</h3>
                </div>
                <div>
                  <p class="text-xs font-medium text-gray-600 capalize mb-1">Address</p>
                  <h3 class="text-lg capitalize">{{ patient.address }}</h3>
                </div>
                <div>
                  <p class="text-xs font-medium text-gray-600 capitalize mb-1">Profession</p>
                  <h3 class="text-lg capitalize">{{ patient.profession }}</h3>
                </div>
                <div>
                  <p class="text-xs font-medium text-gray-600 mb-1">Entry Date</p>
                  <h3 class="text-lg capitalize">{{ patient.entry_date }}</h3>
                </div>
                <div>
                  <p class="text-xs font-medium text-gray-600 capalize mb-1">Referred By</p>
                  <h3 class="text-lg capitalize">{{ patient.referred_by }}</h3>
                </div>
                <div>
                  <p class="text-xs font-medium text-gray-600 capalize mb-1">Guardian Name</p>
                  <h3 class="text-lg capitalize">{{ patient.guardian_name }}</h3>
                </div>
              </div>
            </div>

            <!-- Dental History Card -->
            <div class="px-6 py-4">

              <h2 class="text-2xl font-semibold text-gray-800 mb-6 border-b pb-2">Dental History</h2>
              <div class="space-y-4 grid grid-cols-1 lg:grid-cols-2 gap-4">
                <div class="col-span-2">
                  <p class="text-sm font-medium text-gray-600 mb-1">Current dental concerns</p>
                  <p class="text-md font-semibold whitespace-pre-line">{{ patient.dental_concerns }}</p>
                </div>
                <div>
                  <p class="text-sm font-medium text-gray-600 mb-1">Last dental examination</p>
                  <h3 class="text-xl">{{ patient.last_dental_exam }}</h3>
                </div>
                <div>
                  <p class="text-sm font-medium text-gray-600 mb-1">Last dental X-ray</p>
                  <h3 class="text-xl">{{ patient.last_dental_xray }}</h3>
                </div>
                <div class="col-span-2">
                  <p class="text-sm font-medium text-gray-600 mb-1">Discomfort or Pain</p>
                  <h3 class="text-md font-semibold  whitespace-pre-line">{{ patient.discomfort_of_pain }}</h3>
                </div>
              </div>
            </div>


            <!-- Medical History Card -->
            <div class="px-6 py-4">


              <h2 class="text-2xl font-semibold text-gray-800 mb-6 border-b pb-2">Medical History</h2>
              <div class="space-y-4">
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
                  <div>
                    <p class="text-sm font-medium text-gray-600 mb-1">Current medications</p>
                    <h3 class="text-xl">{{ patient.medications }}</h3>
                  </div>
                  <div>
                    <p class="text-sm font-medium text-gray-600 mb-1">Physician Name</p>
                    <h3 class="text-xl">{{ patient.physician_name }}</h3>
                  </div>
                  <div class="col-span-2">
                    <p class="text-sm font-medium text-gray-600 mb-1">Allergies</p>
                    <p class="text-md font-semibold whitespace-pre-line">{{ patient.allergies }}</p>
                  </div>
                  <div>
                    <p class="text-sm font-medium text-gray-600 mb-1">Other Medical Problems</p>
                    <h3 class="text-xl">{{ patient.other_medical_problems }}</h3>
                  </div>
                </div>
              </div>
            </div>
            <div>
              <!-- Medical Conditions -->
              <div class="px-4 py-4">
                <p class="text-sm font-medium text-gray-600 mb-3">Medical Conditions</p>
                <div class="grid grid-cols-2 gap-4">
                  <div v-if="patient.diabetes" class="text-blue-600">
                    <span class="font-medium">Diabetes</span>
                  </div>
                  <div v-if="patient.tuberculosis" class="text-blue-600">
                    <span class="font-medium">Tuberculosis</span>
                  </div>
                  <div v-if="patient.high_blood_pressure" class="text-blue-600">
                    <span class="font-medium">High Blood Pressure</span>
                  </div>
                  <div v-if="patient.hepatitis" class="text-blue-600">
                    <span class="font-medium">Hepatitis {{ patient.hepatitis_type }}</span>
                  </div>
                  <div v-if="patient.rheumatic_fever" class="text-blue-600">
                    <span class="font-medium">Rheumatic Fever</span>
                  </div>
                  <div v-if="patient.excessive_bleeding" class="text-blue-600">
                    <span class="font-medium">Excessive Bleeding</span>
                  </div>
                  <div v-if="patient.heart_trouble" class="text-blue-600">
                    <span class="font-medium">Heart Trouble</span>
                  </div>
                  <div v-if="patient.is_pregnant" class="text-blue-600">
                    <span class="font-medium">Currently Pregnant</span>
                  </div>
                </div>
              </div>
            </div>


            <!-- Edit Button -->
            <div class="text-center">
              <button type="button" @click="goToEditPage"
                class="inline-flex justify-center py-3 px-6 border border-transparent shadow-sm text-sm font-medium rounded-lg text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors">
                Edit Patient
              </button>
            </div>
          </div>
        </div>




      </div>
    </div>
  </div>
</template>

<script>
import ProcedureList from '@/components/procedureList.vue';

export default {
  components: {
    ProcedureList
  },
  data() {
    return {
      patient: {},
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
      this.loading = true;
      try {
        const response = await this.$axios.get(`/api/patients/${this.$route.params.id}/`);
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
