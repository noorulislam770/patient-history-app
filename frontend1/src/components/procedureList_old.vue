<!-- src/components/ProcedureList.vue -->
<template>
    <div class="mt-8">
        <h3 class="text-xl font-bold mb-4">Procedures</h3>
        <button @click="openAddProcedureModal" class="mb-4 p-2 bg-blue-500 text-white rounded">
            Add Procedure
        </button>
        <div v-if="loading" class="text-center">
            <p class="text-xl">Loading procedures...</p>
        </div>
        <div v-else-if="procedures.length === 0" class="text-center">
            <p class="text-xl">No procedures found.</p>
        </div>
        <div v-else class="bg-white shadow-md rounded-lg overflow-hidden">
            <table class="w-full">
                <thead>
                    <tr class="bg-gray-100 text-left">
                        <th class="py-3 px-4 font-semibold">Date</th>
                        <th class="py-3 px-4 font-semibold">Description</th>
                        <th class="py-3 px-4 font-semibold">Amount</th>
                        <th class="py-3 px-4 font-semibold">Amount Paid</th>
                        <th class="py-3 px-4 font-semibold">Balance</th>
                        <th class="py-3 px-4 font-semibold">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="procedure in procedures" :key="procedure.id"
                        class="border-t border-gray-200 hover:bg-gray-50">
                        <td class="py-3 px-4">{{ procedure.date }}</td>
                        <td class="py-3 px-4">{{ procedure.description }}</td>
                        <td class="py-3 px-4">{{ procedure.total_amount }}</td>
                        <td class="py-3 px-4">{{ procedure.amount_paid }}</td>
                        <td class="py-3 px-4">{{ procedure.balance }}</td>
                        <td class="py-3 px-4">
                            <router-link :to="`/patients/${patientId}/procedures/${procedure.id}`"
                                class="text-blue-500 hover:text-blue-700 mr-2">
                                View
                            </router-link>
                            <button @click="editProcedure(procedure)" class="text-blue-500 hover:text-blue-700 mr-2">
                                Edit
                            </button>
                            <button @click="deleteProcedure(procedure.id)" class="text-red-500 hover:text-red-700">
                                Delete
                            </button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Add/Edit Procedure Modal -->
        <div v-if="isModalOpen" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4">
            <div class="bg-white rounded-lg shadow-lg w-full max-w-2xl p-6">
                <div class="flex justify-between items-center mb-4">
                    <h2 class="text-xl font-bold">{{ isEditing ? 'Edit Procedure' : 'Add Procedure' }} </h2>
                    <button @click="closeModal" class="text-gray-500 hover:text-gray-700">
                        &times;
                    </button>
                </div>
                <p class="text-gray-600 block">for patient <b class="uppercase">{{ patientName }}</b> </p>
                <form @submit.prevent="submitForm">
                    <div class="space-y-4">
                        <input v-model="form.date" type="date" placeholder="Date" class="p-2 border rounded w-full"
                            required />
                        <input v-model="form.description" ref="descriptionInput" type="text" placeholder="Description"
                            class="p-2 border rounded w-full" required />
                        <input v-model="form.total_amount" type="number" placeholder="Total Amount"
                            class="p-2 border rounded w-full" required @input="updateBalance" />
                        <input v-model="form.amount_paid" type="number" placeholder="Amount Paid"
                            class="p-2 border rounded w-full" required @input="updateBalance" />
                        <input v-model="form.balance" type="number" placeholder="Balance"
                            class="p-2 border rounded w-full" readonly />
                        <textarea v-model="form.notes" placeholder="Notes" class="p-2 border rounded w-full"></textarea>
                    </div>
                    <div class="mt-6">
                        <button type="submit" class="p-2 bg-blue-500 text-white rounded">
                            {{ isEditing ? 'Update' : 'Add' }}
                        </button>
                        <button @click="closeModal" type="button" class="p-2 bg-gray-500 text-white rounded ml-2">
                            Cancel
                        </button>
                    </div>
                </form>
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
        console.log("patientId : ", this.patientId); await this.fetchProcedures();
    },
    watch: {
        patientId: {
            immediate: true, // Trigger the watcher immediately
            handler(newPatientId) {
                if (newPatientId) {

                    this.fetchProcedures();
                }
            },
        },
    },
    methods: {
        async fetchProcedures() {
            this.loading = true;
            console.log("patientId : ", this.patientId);
            try {
                const response = await this.$axios.get(`/api/procedures/?patient_id=${this.patientId}`);
                this.procedures = response.data;
            } catch (error) {
                console.error('Error fetching procedures:', error);
            } finally {
                this.loading = false;
            }
        },
        openAddProcedureModal() {
            this.isEditing = false;
            this.form = {
                id: null,
                date: new Date().toISOString().split('T')[0], // Set today's date
                description: '',
                total_amount: 0,
                amount_paid: 0,
                balance: 0,
                notes: '',
            };

            this.isModalOpen = true;
            this.$nextTick(() => {
                this.$refs.descriptionInput.focus(); // Focus the description input
            });
        },
        editProcedure(procedure) {
            this.isEditing = true;
            this.form = { ...procedure };
            this.isModalOpen = true;
            this.$nextTick(() => {
                this.$refs.descriptionInput.focus(); // Focus the description input
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
