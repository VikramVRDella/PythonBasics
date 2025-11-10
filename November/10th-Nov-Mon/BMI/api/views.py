from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class BmiAPI(APIView):
    def get(self,request,bmi_id=None):
        if bmi_id==None:
            all_bmi=BMICalculator.objects.all()
            bmis_data=BMI_Serializer(all_bmi,many=True).data
            return Response(bmis_data)
        else:
            one_bmi=BMICalculator.objects.get(id=bmi_id)
            bmi_data=BMI_Serializer(one_bmi).data
            return Response(bmi_data)

    def post(self,request):

        Bmi=request.data['weight']/((request.data['height'])**2)
        if Bmi < 18.5:
            cat="Underweight"
        elif Bmi >18.5 and Bmi<24.9:
            cat="Normal"
        elif Bmi>25 and Bmi<29.9:
            cat="OverWeight"
        else:
            cat="Obese"

        new_data=BMICalculator(
            weight=request.data['weight'],
            height=request.data['height'],
            bmi=Bmi,
            category=cat
        )

        new_data.save()
        return Response("Data Added")

    def patch(self,request,bmi_id):
        bmi_instance=BMICalculator.objects.get(id=bmi_id)
        weight = float(request.data.get('weight', bmi_instance.weight))
        height = float(request.data.get('height', bmi_instance.height))
        
        Bmi=weight/(height**2)

        if Bmi < 18.5:
            cat="Underweight"
        elif Bmi >18.5 and Bmi<24.9:
            cat="Normal"
        elif Bmi>25 and Bmi<29.9:
            cat="OverWeight"
        else:
            cat="Obese"
        
        bmi_instance.weight=weight
        bmi_instance.height=height
        bmi_instance.bmi=Bmi
        bmi_instance.category=cat

        bmi_instance.save()

        return Response(f"BMI Updated for {bmi_id}")

    def delete(self,request,bmi_id):
        delete_bmi=BMICalculator.objects.get(id=bmi_id)
        delete_bmi.delete()
        return Response("Data Deleted")