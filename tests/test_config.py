import json
import logging
import os
import joblib
import pytest
from prediction_service.prediction import form_response, api_response
import prediction_service

input_data = {
    "incorrect_range": 
    {"Area": 7897897, 
    "Perimeter": 555, 
    "Compactness": 99, 
    "Kernel.Length": 99, 
    "Kernel.Width": 12, 
    "Asymmetry.Coeff": 789, 
    "Kernel.Groove": 75, 
    },

    "correct_range":
    {"Area": 11, 
    "Perimeter": 15, 
    "Compactness": 0.89, 
    "Kernel.Length": 5.67, 
    "Kernel.Width": 3.678, 
    "Asymmetry.Coeff": 4.023, 
    "Kernel.Groove": 5.78, 
    },

    "incorrect_col":
    {"area": 11, 
    "Perimeter": 15, 
    "Compactness": 0.89, 
    "Kernel.Length": 5.67, 
    "Kernel.Width": 3.678, 
    "Asymmetry.Coeff": 4.023, 
    "Kernel.Groove": 5.78, 
    }
}

Type_range = {
   "min": 1,
   "max": 3
}

#Type_min = int(1)
#Type_max = int(3)

def test_form_response_correct_range(data=input_data["correct_range"]):
    res = form_response(data)
    assert  Type_range["min"] <= res <= Type_range["max"]

def test_api_response_correct_range(data=input_data["correct_range"]):
    res = api_response(data)
    assert  Type_range["min"] <= res["response"] <= Type_range["max"]

def test_form_response_incorrect_range(data=input_data["incorrect_range"]):
    with pytest.raises(prediction_service.prediction.NotInRange):
        res = form_response(data)

def test_api_response_incorrect_range(data=input_data["incorrect_range"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInRange().message

def test_api_response_incorrect_col(data=input_data["incorrect_col"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInCols().message