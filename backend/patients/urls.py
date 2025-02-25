# patients/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientCreateView, PatientSearchView, PatientViewSet,  AppointmentViewSet, ProcedureViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'procedures', ProcedureViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('patients/', PatientCreateView.as_view(), name='patient-create'),
    path('search/', PatientSearchView.as_view(), name='patient-search'),
]
