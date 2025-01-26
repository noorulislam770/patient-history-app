<template>
  <div class="min-h-screen bg-white">
    <!-- Hero Section -->
    <div class="container mx-auto px-4 py-12 items-center relative">
      <div class="flex flex-col lg:flex-row items-center">
        <!-- Left Content -->
        <div class="lg:w-1/2 z-10 items-center">
          <h1 class="text-4xl md:text-5xl font-bold text-gray-800 mb-4">
            Dot Dentistry - Dental Care
          </h1>
          <p class="text-gray-600 mb-8">
            Portal for Patient Management System
          </p>

        </div>
      </div>
    </div>

    <!-- Info Cards Section -->
    <div class="bg-gray-50 py-16">
      <div class="container mx-auto px-4">
        <div class="grid md:grid-cols-3 gap-8">
          <!-- Emergency Service Card -->
          <div class="bg-[#B4F7F7] rounded-lg p-8">
            <h2 class="text-3xl font-bold text-gray-800 mb-4">Add New Patient</h2>
            <h3 class="font-semibold text-gray-700 mb-4">Pateint Registration</h3>
            <p class="text-gray-600 mb-6">
              Add new patient to the system such that later they can be searched for. Added various procedures and keep
              track of dental history.
            </p>
            <router-link :to="'/patients/add'">
              <button class="bg-white px-6 py-2 rounded-full text-gray-800 hover:shadow-lg transition duration-300">
                Add Patient
              </button>
            </router-link>
          </div>

          <!-- Appointment Card -->
          <div class="bg-[#B4F7F7] rounded-lg p-8">
            <div class="mb-4">
              <CalendarIcon class="w-8 h-8 text-gray-800" />
            </div>
            <h2 class="text-3xl font-bold text-gray-800 mb-4">Search For Patient</h2>
            <h3 class="font-semibold text-gray-700 mb-4">Searching throug various patients properties</h3>
            <p class="text-gray-600 mb-6">
              You can search for patient through various properties such as name, phone number, Pateint ID.
            </p>
            <router-link :to="'/patients'">
              <button class="bg-white px-6 py-2 rounded-full text-gray-800 hover:shadow-lg transition duration-300">
                Search Patients
              </button>
            </router-link>
          </div>

          <!-- Opening Hours Card -->
          <div class="bg-[#B4F7F7] rounded-lg p-8">
            <div class="mb-4">
              <ClockIcon class="w-8 h-8 text-gray-800" />
            </div>
            <h2 class="text-3xl font-bold text-gray-800 mb-4">Appointment Calander</h2>
            <h3 class="font-semibold text-gray-700 mb-4">Setup Future Appointments</h3>
            <div class="text-gray-600 mb-2">Monday - Friday</div>
            <div class="text-gray-600 mb-6">Saturday - Sunday</div>
            <button class="bg-white px-6 py-2 rounded-full text-gray-800 hover:shadow-lg transition duration-300">
              Contact Us
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { HeartPulse, Stethoscope, Calendar, Clock } from 'lucide-vue-next'
</script>
<script>
export default {
  name: 'HomeView',
};
</script>
