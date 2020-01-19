import pandas as pd
import numpy as np

from django.shortcuts import render
from joblib import load
import requests

from .forms import TitanicForm

def home(request):
	titanic_form = TitanicForm()
	return render(request, 'home.html', {'titanic_form': titanic_form})


def titanic(request):

	if request.method == 'POST':
		titanic_form = TitanicForm(request.POST)
		if titanic_form.is_valid():

			X_test = {
				"Pclass": titanic_form.cleaned_data['pclass'],
				"Age": titanic_form.cleaned_data['age'],
				"Sibp": titanic_form.cleaned_data['sibsp'],
				"Parch": titanic_form.cleaned_data['parch'],
				"Fare": titanic_form.cleaned_data['fare'],
				"Sex": titanic_form.cleaned_data['sex'],
				"Embarked": titanic_form.cleaned_data['embarked']
			}

			prediction = requests.post("https://seandeery-api.com/titanic_prediction/", data = X_test).json()

			return render(request, 'titanic.html', {'titanic_form': titanic_form, 'prediction': prediction})
	else:
		titanic_form = TitanicForm()
		return render(request, 'titanic.html', {'titanic_form': titanic_form})

	