from django.shortcuts import render
from rest_framework.views import APIView
import pickle
from rest_framework.response import Response
# Create your views here.

class Salary_API(APIView):

    def get(self,request,experience):
        regressor = pickle.load(open("salary_predictor.pk","rb"))
        salary = regressor.predict([[experience]])
        return Response(salary)