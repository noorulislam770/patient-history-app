<template>
  <div class="mt-8 shadow-lg rounded-lg overflow-hidden">
    <div class="bg-gradient-to-r from-cyan-500 to-blue-500 p-6">
      <div class="max-w-7xl mx-auto flex flex-col lg:flex-row justify-between items-center">
        <h4 class="text-xl font-semibold text-gray-100">Procedures List for <span
            class="text-2xl text-white capitalize font-bold">{{ patientName }}</span>
        </h4>
        <button @click="openAddProcedureModal"
          class="mt-4 lg:mt-0 px-6 py-2 bg-white text-blue-600 font-semibold rounded-lg shadow-md hover:bg-gray-100 transition duration-300">
          + Add Procedure
        </button>
      </div>
    </div>

    <div class="bg-white p-6">
      <div v-if="loading" class="text-center py-8">
        <p class="text-xl text-gray-600">Loading procedures...</p>
      </div>
      <div v-else-if="procedures.length === 0" class="text-center py-8">
        <p class="text-xl text-gray-600">No procedures found.</p>
      </div>
      <div v-else class="overflow-x-auto">
        <table class="min-w-full bg-white">
          <thead class="bg-gray-50">
            <tr>
              <th class="py-3 px-4 text-left text-sm font-semibold text-gray-600 uppercase">ID</th>
              <th class="py-3 px-4 text-left text-sm font-semibold text-gray-600 uppercase">Date</th>
              <th class="py-3 px-4 text-left text-sm font-semibold text-gray-600 uppercase">Description</th>
              <th class="py-3 px-4 text-left text-sm font-semibold text-gray-600 uppercase">Amount</th>
              <th class="py-3 px-4 text-left text-sm font-semibold text-gray-600 uppercase">Amount Paid</th>
              <th class="py-3 px-4 text-left text-sm font-semibold text-gray-600 uppercase">Balance</th>
              <th class="py-3 px-4 text-left text-sm font-semibold text-gray-600 uppercase">View</th>
              <th class="py-3 px-4 text-left text-sm font-semibold text-gray-600 uppercase">Actions</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr v-for="procedure in procedures" :key="procedure.id" class="hover:bg-gray-50 transition duration-150">
              <td class="py-3 px-4 text-sm text-gray-700">{{ procedure.id }}</td>
              <td class="py-3 px-4 text-sm text-gray-700">{{ procedure.date }}</td>
              <td class="py-3 px-4 text-sm text-gray-700">{{ procedure.description }}</td>
              <td class="py-3 px-4 text-sm text-gray-700">${{ procedure.total_amount }}</td>
              <td class="py-3 px-4 text-sm text-gray-700">${{ procedure.amount_paid }}</td>
              <td class="py-3 px-4 text-sm text-gray-700">${{ procedure.balance }}</td>
              <td class="py-3 px-4">
                <router-link :to="`/patients/${patientId}/procedures/${procedure.id}`"
                  class="text-blue-500 hover:text-blue-700 transition duration-150">
                  View
                </router-link>
              </td>
              <td class="py-3 px-4">
                <button @click="editProcedure(procedure)"
                  class="text-blue-500 hover:text-blue-700 mr-2 transition duration-150">
                  Edit
                </button>
                <button @click="deleteProcedure(procedure.id)"
                  class="text-red-500 hover:text-red-700 transition duration-150">
                  Delete
                </button>
              </td>
            </tr>
          </tbody>
        </table>

        <!-- Pagination Controls -->
        <div class="flex justify-between items-center px-4 py-4 bg-gray-50 mt-4">
          <div class="text-sm text-gray-600">
            Showing {{ currentPage * pageSize - pageSize + 1 }} to
            {{ Math.min(currentPage * pageSize, totalItems) }} of {{ totalItems }} procedures
          </div>
          <div class="flex space-x-2">
            <button @click="changePage(currentPage - 1)" :disabled="currentPage === 1"
              class="px-4 py-2 border rounded-md hover:bg-gray-100 disabled:opacity-50 disabled:cursor-not-allowed">
              Previous
            </button>
            <button @click="changePage(currentPage + 1)" :disabled="currentPage >= totalPages"
              class="px-4 py-2 border rounded-md hover:bg-gray-100 disabled:opacity-50 disabled:cursor-not-allowed">
              Next
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Add/Edit Procedure Modal -->
    <div v-if="isModalOpen" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
      <div class="bg-white rounded-lg shadow-xl w-full max-w-2xl overflow-hidden">
        <div class="flex justify-between text-center items-center bg-gradient-to-r from-cyan-500 to-blue-500 p-6">
          <h2 class="text-xl font-bold text-center text-white">{{ isEditing ? 'Edit Procedure' : 'Add Procedure' }}</h2>
          <button @click="closeModal" class="text-white hover:text-gray-200 transition duration-150">
            &times;
          </button>
        </div>
        <div class="p-6">
          <p class="text-gray-600 mb-4">For patient <b class="uppercase">{{ patientName }}</b></p>
          <form @submit.prevent="submitForm">
            <div class="space-y-4">
              <label for="date" class="mb-0 text-md font-light text-gray-900">procedure date</label>
              <input v-model="form.date" type="date" placeholder="Date" style="margin-top: 2px"
                class="p-2 border rounded w-full focus:outline-none border-gray-400 focus:ring-2 focus:ring-blue-500"
                required />
              <label for="description" class="mb-0 text-md font-light text-gray-900">Description</label>
              <input v-model="form.description" ref="descriptionInput" type="text" placeholder="Description"
                style="margin-top: 2px"
                class="p-2 border rounded w-full focus:outline-none border-gray-400 focus:ring-2 focus:ring-blue-500"
                required />
              <label for="total_amount" class="mb-0 text-md font-light text-gray-900">Total Amount</label>
              <input v-model="form.total_amount" type="number" placeholder="Total Amount" style="margin-top: 2px"
                class="p-2 border rounded w-full focus:outline-none border-gray-400 focus:ring-2 focus:ring-blue-500"
                required @input="updateBalance" />
              <label for="amount_paid" class="mb-0 text-md font-light text-gray-900">Amount Paid</label>
              <input v-model="form.amount_paid" type="number" placeholder="Amount Paid" style="margin-top: 2px"
                class="p-2 border rounded w-full focus:outline-none border-gray-400 focus:ring-2 focus:ring-blue-500"
                required @input="updateBalance" />
              <label for="balance" class="mb-0 text-md font-light text-gray-900">Balance</label>
              <input v-model="form.balance" type="number" placeholder="Balance" style="margin-top: 2px"
                class="p-2 border rounded w-full bg-gray-100" readonly />
              <label for="notes" class="mb-0 text-md font-light text-gray-900">Notes</label>
              <textarea v-model="form.notes" placeholder="Notes" style="margin-top: 2px"
                class="p-2 border rounded w-full focus:outline-none border-gray-400 focus:ring-2 focus:ring-blue-500"></textarea>
            </div>
            <div class="mt-6 flex justify-end">
              <button type="submit"
                class="px-6 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition duration-150">
                {{ isEditing ? 'Update' : 'Add' }}
              </button>
              <button @click="closeModal" type="button"
                class="px-6 py-2 bg-gray-500 text-white rounded-lg hover:bg-gray-600 ml-2 transition duration-150">
                Cancel
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    patientId: {
      type: Number,
      required: true,
    },
    patientName: {
      type: String,
      required: false,
    },
  },
  data() {
    return {
      procedures: [],
      loading: true,
      isModalOpen: false,
      isEditing: false,
      // Pagination data
      currentPage: 1,
      pageSize: 10,
      totalItems: 0,
      totalPages: 1,
      form: {
        id: null,
        date: '',
        description: '',
        total_amount: 0,
        amount_paid: 0,
        balance: 0,
        notes: '',
      },
    };
  },
  async created() {
    await this.fetchProcedures();
  },
  watch: {
    patientId: {
      immediate: true,
      handler(newPatientId) {
        if (newPatientId) {
          this.currentPage = 1; // Reset to first page when patient changes
          this.fetchProcedures();
        }
      },
    },
  },
  methods: {
    async fetchProcedures() {
      this.loading = true;
      try {
        const response = await this.$axios.get(`/api/procedures/`, {
          params: {
            patient_id: this.patientId,
            page: this.currentPage,
          },
        });
        // Handle paginated response
        this.procedures = response.data.results;
        this.totalItems = response.data.count;
        this.totalPages = Math.ceil(response.data.count / this.pageSize);
      } catch (error) {
        console.error('Error fetching procedures:', error);
      } finally {
        this.loading = false;
      }
    },
    async changePage(page) {
      if (page >= 1 && page <= this.totalPages) {
        this.currentPage = page;
        await this.fetchProcedures();
      }
    },
    openAddProcedureModal() {
      this.isEditing = false;
      this.form = {
        id: null,
        date: new Date().toISOString().split('T')[0],
        description: '',
        total_amount: 0,
        amount_paid: 0,
        balance: 0,
        notes: '',
      };
      this.isModalOpen = true;
      this.$nextTick(() => {
        this.$refs.descriptionInput.focus();
      });
    },
    editProcedure(procedure) {
      this.isEditing = true;
      this.form = { ...procedure };
      this.isModalOpen = true;
      this.$nextTick(() => {
        this.$refs.descriptionInput.focus();
      });
    },
    async submitForm() {
      const url = this.isEditing
        ? `/api/procedures/${this.form.id}/`
        : '/api/procedures/';
      const method = this.isEditing ? 'put' : 'post';

      try {
        await this.$axios[method](url, {
          ...this.form,
          patient: this.patientId,
        });
        this.closeModal();
        await this.fetchProcedures();
      } catch (error) {
        console.error('Error saving procedure:', error);
      }
    },
    async deleteProcedure(procedureId) {
      if (confirm('Are you sure you want to delete this procedure?')) {
        try {
          await this.$axios.delete(`/api/procedures/${procedureId}/`);
          // Refetch current page, or go to previous page if this was the last item
          if (this.procedures.length === 1 && this.currentPage > 1) {
            this.currentPage--;
          }
          await this.fetchProcedures();
        } catch (error) {
          console.error('Error deleting procedure:', error);
        }
      }
    },
    closeModal() {
      this.isModalOpen = false;
    },
    updateBalance() {
      this.form.balance = this.form.total_amount - this.form.amount_paid;
    },
  },
};
</script>
