from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=15)
    email = models.EmailField()
    profession = models.CharField(max_length=255)
    referred_by = models.CharField(max_length=255)

class MedicalHistory(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    diabetes = models.BooleanField(default=False)
    tuberculosis = models.BooleanField(default=False)
    high_blood_pressure = models.BooleanField(default=False)
    hepatitis = models.BooleanField(default=False)
    rheumatic_fever = models.BooleanField(default=False)
    excessive_bleeding = models.BooleanField(default=False)
    heart_trouble = models.BooleanField(default=False)
    allergies = models.TextField(blank=True)
    other_medical_problems = models.TextField(blank=True)

class DentalHistory(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    last_dental_exam = models.DateField(null=True, blank=True)
    last_dental_xray = models.DateField(null=True, blank=True)
    physicians_name = models.CharField(max_length=255, blank=True)
    current_medications = models.TextField(blank=True)
    pregnant = models.BooleanField(default=False)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    procedure = models.TextField()
    comments = models.TextField(blank=True)