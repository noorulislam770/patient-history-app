<template>
  <div class="min-h-screen bg-gray-50   py-8 px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl mx-auto">
      <!-- Header -->
      <div class="text-center mb- 8 text-center bg-gradient-to-r rounded-t-xl from-cyan-500 to-blue-500 p-6">
        <h1 class="text-3xl font-bold text-white  inline-block">
          Dot Dentistry - Dental Care
        </h1>
        <p class="mt-2 text-lg font-light tracking-wider leading-loose text-white">Add Patient Information</p>
      </div>

      <!-- Form -->
      <form @submit.prevent="handleSubmit" class="space-y-6 pb-4  shadow-xl shadow-cyan-500/50">
        <!-- Essential Information Card -->
        <div class="bg-white shadow rounded-lg p-6">
          <div class="grid grid-cols-1 gap-6 md:grid-cols-2 mb-2">
            <h2 class="text-xl font-semibold text-gray-800 mt-5">Essential Information</h2>
            <div>
              <label class="block text-sm font-small text-gray-700">Patient Entry Date</label>
              <input v-model="form.entry_date" type="date" required
                class="mt-0 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
            </div>
          </div>
          <hr>
          <div class="grid grid-cols-1 gap-6 md:grid-cols-2 mt-2">
            <div>
              <label class="block text-sm font-medium text-gray-700">Name *</label>
              <input v-model="form.name" type="text" required
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Age *</label>
              <input v-model="form.age" type="number" required
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Gender</label>
              <select v-model="form.gender"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
                <option value="">Select Gender</option>
                <option value="male">Male</option>
                <option value="female">Female</option>
                <option value="other">Other</option>
              </select>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700">S/D/W of, Self </label>
              <input v-model="form.guardian_name" type="text" required
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Profession </label>
              <input v-model="form.profession" type="text" required
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Referred By </label>
              <input v-model="form.referred_by" type="text" required
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
            </div>

            <div class="md:col-span-2">
              <label class="block text-sm font-medium text-gray-700">Address *</label>
              <textarea v-model="form.address" required rows="2"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500"></textarea>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Mobile No. *</label>
              <input v-model="form.mobile_no" type="tel" required
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Email</label>
              <input v-model="form.email" type="email"
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
              <textarea v-model="form.dentalConcerns" rows="2"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500"
                placeholder="Are you aware of any particular trouble with your teeth or gums now?"></textarea>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Discomfort of Pain</label>
              <textarea v-model="form.discomfortOfPain" rows="2"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500"
                placeholder="Are you having any discomfort of pain?"></textarea>
            </div>
            <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
              <div>
                <label class="block text-sm font-medium text-gray-700">Last dental examination</label>
                <input v-model="form.lastExamination" type="date"
                  class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Last dental X-ray</label>
                <input v-model="form.lastXray" type="date"
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
                <input v-model="form.medications" type="text"
                  class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Physician's name</label>
                <input v-model="form.physicianName" type="text"
                  class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
              </div>
            </div>

            <!-- Medical Conditions Checkboxes -->
            <div class="space-y-3">
              <h3 class="text-sm font-medium text-gray-700">Medical Conditions</h3>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                <label class="flex items-center space-x-2">
                  <input type="checkbox" v-model="form.conditions.diabetes" class="rounded text-blue-600">
                  <span class="text-sm">Diabetes</span>
                </label>
                <label class="flex items-center space-x-2">
                  <input type="checkbox" v-model="form.conditions.tuberculosis" class="rounded text-blue-600">
                  <span class="text-sm">Tuberculosis</span>
                </label>
                <label class="flex items-center space-x-2">
                  <input type="checkbox" v-model="form.conditions.bloodPressure" class="rounded text-blue-600">
                  <span class="text-sm">High Blood Pressure</span>
                </label>
                <label class="flex items-center space-x-2">
                  <input type="checkbox" v-model="form.conditions.hepatitis" class="rounded text-blue-600"
                    @change="showHepatitisDropdown = form.conditions.hepatitis">
                  <span class="text-sm">Hepatitis</span>
                </label>

                <!-- Hepatitis Dropdown -->
                <div v-if="showHepatitisDropdown" class="md:col-span-2">
                  <label class="block text-sm font-medium text-gray-700">Hepatitis Type</label>
                  <select v-model="form.hepatitisType"
                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500">
                    <option value="">Select type</option>
                    <option value="A">Hepatitis A</option>
                    <option value="B">Hepatitis B</option>
                    <option value="C">Hepatitis C</option>
                  </select>
                </div>

                <label class="flex items-center space-x-2">
                  <input type="checkbox" v-model="form.conditions.rheumatic_fever" class="rounded text-blue-600">
                  <span class="text-sm">Rheumatic Fever</span>
                </label>
                <label class="flex items-center space-x-2">
                  <input type="checkbox" v-model="form.conditions.excessive_bleeding" class="rounded text-blue-600">
                  <span class="text-sm">Excessive Bleeding</span>
                </label>
              </div>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700">Allergies</label>
              <textarea v-model="form.allergies" rows="2"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 border pl-2 py-2  focus:ring-blue-500"></textarea>
            </div>

            <!-- Pregnancy Question -->
            <div class="border-t pt-4">
              <label class="block text-sm font-medium text-gray-700 mb-2">For females only:</label>
              <div class="flex items-center space-x-4">
                <span class="text-sm">Are you pregnant?</span>
                <label class="flex items-center space-x-2">
                  <input type="radio" v-model="form.isPregnant" :value="true" class="text-blue-600">
                  <span class="text-sm">Yes</span>
                </label>
                <label class="flex items-center space-x-2">
                  <input type="radio" v-model="form.isPregnant" :value="false" class="text-blue-600">
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
            Add Patient
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
      form: {
        // Essential Information
        name: '',
        age: '',
        address: '',
        mobile_no: '',
        email: '',
        gender: '',
        profession: '',
        referred_by: '',
        entry_date: new Date().toISOString().split('T')[0],
        // Dental History
        dentalConcerns: '',
        lastExamination: '',
        lastXray: '',

        // Medical History
        medications: '',
        physicianName: '',
        conditions: {
          diabetes: false,
          tuberculosis: false,
          bloodPressure: false,
          hepatitis: false,
          rheumatic_fever: false,
          excessive_bleeding: false,
        },
        hepatitisType: '', // New field for hepatitis type
        allergies: '',
        isPregnant: null,
      },
      showHepatitisDropdown: false, // Controls visibility of the dropdown
    };
  },
  methods: {
    async handleSubmit() {
      try {
        console.log(this.form)
        const response = await this.$axios.post('/api/patients/', this.form);
        const newPatientId = response.data.id; // Get the new patient's ID from the response
        alert('Patient added successfully!');
        this.$router.push(`/patients/${newPatientId}`);
      } catch (error) {
        console.error('Error adding patient:', error);
        alert('Failed to add patient.');
      }
    },
  },
};
</script>
