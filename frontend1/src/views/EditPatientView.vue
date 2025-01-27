<template>
  <div class="min-h-screen bg-gray-50 py-8 px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl mx-auto">
      <!-- Header -->
      <div class="text-center mb- 8 text-center bg-gradient-to-r rounded-t-xl from-cyan-500 to-blue-500 p-6">
        <h1 class="text-3xl font-bold text-white  inline-block">
          Dot Dentistry - Dental Care
        </h1>
        <p class="mt-2 text-lg font-light tracking-wider leading-loose text-white">Edit Patient Information</p>
      </div>

      <!-- Form -->
      <form @submit.prevent="submitForm" class="space-y-6">
        <!-- Essential Information Card -->
        <!-- <input type="hidden" v-model="patient.id" /> -->
        <div class="bg-white shadow rounded-lg p-6">
          <h2 class="text-xl font-semibold text-gray-800 mb-4 ">Essential Information</h2>
          <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
            <div>
              <label class="block text-sm font-medium text-gray-700">Pateint ID #</label>
              <input v-model="patient.id" type="text" readonly
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
            </div>
            <div>
              <label class="block text-sm  font-medium text-gray-700">Name *</label>
              <input v-model="patient.name" type="text" required
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Age *</label>
              <input v-model="patient.age" type="number" required
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Gender</label>
              <select v-model="patient.gender"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
                <option v-if="patient.gender == ''" value="">Select Gender</option>
                <option v-if="patient.gender == 'male'" value="male">Male</option>
                <option v-if="patient.gender == 'female'" value="female">Female</option>
                <option v-if="patient.gender == 'other'" value="other">Other</option>
              </select>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700">S/D/W of, Self</label>
              <input v-model="patient.guardian_name" type="text" required
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Profession</label>
              <input v-model="patient.profession" type="text" required
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Referred By</label>
              <input v-model="patient.referred_by" type="text" required
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
            </div>


            <div class="md:col-span-2">
              <label class="block text-sm font-medium text-gray-700">Address *</label>
              <textarea v-model="patient.address" required rows="2"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500"></textarea>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Mobile No. *</label>
              <input v-model="patient.mobile_no" type="tel" required
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Email</label>
              <input v-model="patient.email" type="email"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
            </div>

          </div>
        </div>

        <!-- Dental History Card -->
        <div class="bg-white shadow rounded-lg p-6">
          <h2 class="text-xl font-semibold text-gray-800 mb-4">Dental History</h2>
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700">Current dental concerns</label>
              <textarea v-model="patient.dental_concerns" rows="2"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500"
                placeholder="Are you aware of any particular trouble with your teeth or gums now?"></textarea>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Discomfort of Pain</label>
              <textarea v-model="patient.discomfort_of_pain" rows="2"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500"
                placeholder="Are you having any discomfort of pain?"></textarea>
            </div>
            <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
              <div>
                <label class="block text-sm font-medium text-gray-700">Last dental examination</label>
                <input v-model="patient.last_dental_exam" type="date"
                  class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Last dental X-ray</label>
                <input v-model="patient.last_dental_xray" type="date"
                  class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
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
                <input v-model="patient.medications" type="text"
                  class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Physician's name</label>
                <input v-model="patient.physician_name" type="text"
                  class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
              </div>
            </div>

            <!-- Medical Conditions Checkboxes -->
            <div class="space-y-3">
              <h3 class="text-sm font-medium text-gray-700">Medical Conditions</h3>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                <label class="flex items-center space-x-2">
                  <input type="checkbox" v-model="patient.diabetes" class="rounded text-blue-600">
                  <span class="text-sm">Diabetes</span>
                </label>
                <label class="flex items-center space-x-2">
                  <input type="checkbox" v-model="patient.tuberculosis" class="rounded text-blue-600">
                  <span class="text-sm">Tuberculosis</span>
                </label>
                <label class="flex items-center space-x-2">
                  <input type="checkbox" v-model="patient.high_blood_pressure" class="rounded text-blue-600">
                  <span class="text-sm">High Blood Pressure</span>
                </label>
                <label class="flex items-center space-x-2">
                  <input type="checkbox" v-model="patient.hepatitis" class="rounded text-blue-600"
                    @change="showHepatitisDropdown = patient.hepatitis">
                  <span class="text-sm">Hepatitis</span>
                </label>

                <!-- Hepatitis Dropdown -->
                <div v-if="showHepatitisDropdown" class="md:col-span-2">
                  <label class="block text-sm font-medium text-gray-700">Hepatitis Type</label>
                  <select v-model="patient.hepatitis_type"
                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
                    <option value="">Select type</option>
                    <option value="A">Hepatitis A</option>
                    <option value="B">Hepatitis B</option>
                    <option value="C">Hepatitis C</option>
                  </select>
                </div>

                <label class="flex items-center space-x-2">
                  <input type="checkbox" v-model="patient.rheumatic_fever" class="rounded text-blue-600">
                  <span class="text-sm">Rheumatic Fever</span>
                </label>
                <label class="flex items-center space-x-2">
                  <input type="checkbox" v-model="patient.excessive_bleeding" class="rounded text-blue-600">
                  <span class="text-sm">Excessive Bleeding</span>
                </label>
              </div>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700">Allergies</label>
              <textarea v-model="patient.allergies" rows="2"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500"></textarea>
            </div>

            <!-- Pregnancy Question -->
            <div class="border-t pt-4">
              <label class="block text-sm font-medium text-gray-700 mb-2">For females only:</label>
              <div class="flex items-center space-x-4">
                <span class="text-sm">Are you pregnant?</span>
                <label class="flex items-center space-x-2">
                  <input type="radio" v-model="patient.is_pregnant" :value="true" class="text-blue-600">
                  <span class="text-sm">Yes</span>
                </label>
                <label class="flex items-center space-x-2">
                  <input type="radio" v-model="patient.is_pregnant" :value="false" class="text-blue-600">
                  <span class="text-sm">No</span>
                </label>
              </div>
            </div>
          </div>
        </div>

        <!-- Footer -->
        <div class="text-center space-y-4">
          <p class="text-sm text-gray-600">
            This Personal information is to help us do our best in maintaining your Smile, comfort and ability to chew.
            This information is, of course, confidential and we consider it a privilege to be given the opportunity to
            take care of you.
          </p>
          <button type="submit"
            class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
            Update Patient
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
        // Essential Information
        id: '',
        name: '',
        age: '',
        gender: '',
        address: '',
        mobile_no: '',
        email: '',
        profession: '',
        referred_by: '',

        // Dental History
        dental_concerns: '',
        discomfort_of_pain: '',
        last_dental_exam: '',
        last_dental_xray: '',

        // Medical History
        medications: '',
        physician_name: '',
        diabetes: false,
        tuberculosis: false,
        high_blood_pressure: false,
        hepatitis: false,
        rheumatic_fever: false,
        excessive_bleeding: false,
        allergies: '',
        is_pregnant: null,
        hepatitis_type: '',
      },
      showHepatitisDropdown: false,
    };
  },
  async created() {
    const patientId = this.$route.params.id;
    try {
      const response = await this.$axios.get(`/api/patients/${patientId}/`);
      this.patient = response.data;
      console.log(this.patient);
      this.showHepatitisDropdown = this.patient.hepatitis; // Show dropdown if hepatitis is true
    } catch (error) {
      console.error('Error fetching patient:', error);
    }
  },
  methods: {
    async submitForm() {
      try {
        const patientId = this.$route.params.id;
        await this.$axios.put(`/api/patients/${patientId}/`, this.patient);
        // alert('Patient updated successfully!');
        this.$router.push(`/patients/${patientId}`); // Redirect to patient list
      } catch (error) {
        console.error('Error updating patient:', error);
        alert('Failed to update patient.');
      }
    },
  },
};
</script>
