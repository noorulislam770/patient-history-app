# patients/views.py
from rest_framework import viewsets
from .models import Patient, MedicalHistory, DentalHistory, Appointment
from .serializers import PatientSerializer, MedicalHistorySerializer, DentalHistorySerializer, AppointmentSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class MedicalHistoryViewSet(viewsets.ModelViewSet):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer

class DentalHistoryViewSet(viewsets.ModelViewSet):
    queryset = DentalHistory.objects.all()
    serializer_class = DentalHistorySerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer