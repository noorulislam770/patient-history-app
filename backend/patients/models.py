from django.db import models


class Patient(models.Model):
    # Essential Information
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=15)
    email = models.EmailField()
    profession = models.CharField(max_length=255)
    referred_by = models.CharField(max_length=255)

    # Dental History
    dental_concerns = models.TextField(blank=True)
    discomfort_of_pain = models.TextField(blank=True)
    last_dental_exam = models.DateField(null=True, blank=True)
    last_dental_xray = models.DateField(null=True, blank=True)

    # Medical History
    diabetes = models.BooleanField(default=False)
    tuberculosis = models.BooleanField(default=False)
    high_blood_pressure = models.BooleanField(default=False)
    hepatitis = models.BooleanField(default=False)
    rheumatic_fever = models.BooleanField(default=False)
    excessive_bleeding = models.BooleanField(default=False)
    heart_trouble = models.BooleanField(default=False)
    allergies = models.TextField(blank=True)
    other_medical_problems = models.TextField(blank=True)
    medications = models.TextField(blank=True)
    physician_name = models.CharField(max_length=255, blank=True)
    is_pregnant = models.BooleanField(default=False)
    hepatitis_type = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    procedure = models.TextField()
    comments = models.TextField(blank=True)
