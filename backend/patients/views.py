# patients/views.py
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Patient, Procedure, Appointment
from .serializers import PatientSerializer, AppointmentSerializer, ProcedureSerializer


class PatientCreateView(APIView):
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            patient = serializer.save()  # Save the new patient
            return Response(
                {
                    'id': patient.id,  # Return the new patient's ID
                    'message': 'Patient added successfully!',
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientUpdateView(APIView):
    def put(self, request):
        patient = Patient.objects.get(id=request.data['id'])
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the updated patient
            return Response(
                {
                    # Return the updated patient's ID
                    'id': serializer.data['id'],
                    'message': 'Patient updated successfully!',
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientSearchView(APIView):
    def get(self, request):
        # Get the search query from the URL
        query = request.query_params.get('query', '')
        if query:
            patients = Patient.objects.filter(
                name__icontains=query)  # Case-insensitive search
        else:
            patients = Patient.objects.all()  # Return all patients if no query is provided
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class ProcedureViewSet(viewsets.ModelViewSet):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer

    def get_queryset(self):
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            patient = Patient.objects.get(id=patient_id)
            procedure = Procedure.objects.filter(patient_id=patient_id)
            # print(procedure)
            return procedure
        elif not patient_id:
            return Procedure.objects.all().order_by('-date')
        # return Patient.objects.all()
