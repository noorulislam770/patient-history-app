# patients/serializers.py
from rest_framework import serializers
from .models import Patient, MedicalHistory, DentalHistory, Appointment

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'  # Include all fields from the Patient model

class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = '__all__'

class DentalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DentalHistory
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'