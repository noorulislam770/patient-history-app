import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import PatientListView from '../views/PatientListView.vue'
import AddPatientView from '../views/AddPatientView.vue'
import EditPatientView from '../views/EditPatientView.vue'
import PatientDetailsView from '../views/PatientDetailsView.vue'
import ProcedureDetailsView from '../views/ProcedureDetailsView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView,
  },
  {
    path: '/patients',
    name: 'patients',
    component: PatientListView,
  },
  {
    path: '/patients/add',
    name: 'add-patient',
    component: AddPatientView,
  },
  {
    path: '/patients/:id',
    name: 'patient-details',
    component: PatientDetailsView,
  },
  {
    path: '/patients/:id/edit',
    name: 'edit-patient',
    component: EditPatientView,
  },
  {
    path: '/patients/:patientId/procedures/:procedureId',
    name: 'procedure-details',
    component: ProcedureDetailsView,
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
