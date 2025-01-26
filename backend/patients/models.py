from django.db import models


class Patient(models.Model):
    # Essential Information
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    mobile_no = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    referred_by = models.CharField(max_length=255, blank=True, null=True)
    guardian_name = models.CharField(max_length=255, blank=True)
    entry_date = models.DateField(auto_now_add=True)
    # Dental History
    dental_concerns = models.TextField(blank=True, null=True)
    discomfort_of_pain = models.TextField(blank=True, null=True)
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
    other_medical_problems = models.TextField(blank=True, null=True)
    medications = models.TextField(blank=True, null=True)
    physician_name = models.CharField(max_length=255, blank=True)
    is_pregnant = models.BooleanField(default=False)
    hepatitis_type = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name


class Procedure(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='procedures')
    date = models.DateField()
    description = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.description} on {self.date} for {self.patient.name}"


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    procedure = models.TextField()
    comments = models.TextField(blank=True)
