# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from mlserver.apps import MlserverConfig

import numpy as np


# custom method for generating predictions
def getPredictions(values):
    # import pickle
    # model = pickle.load(open("titanic_survival_ml_model.sav", "rb"))
    # scaled = pickle.load(open("scaler.sav", "rb"))
    # prediction = model.predict()

    x = values[0]
    y = values[1]
    z = values[2]

    features = np.array([[x, y, z]])

    prediction = MlserverConfig.model.predict(features)

    if prediction == 1:
        return "Accident !"
    else:
        if prediction == 0:
            return "Not Accident !"

    return "error"


class MLserver(APIView):

    def get(self, request):
        if request.method == 'GET':
            query = request.GET['values']

            values = [int(item) for item in query.split(',')]

            result = getPredictions(values)

            return JsonResponse(result, safe=False)