import pandas as pd
import numpy as np

from django.shortcuts import render
from joblib import load

from .forms import TitanicForm

def home(request):
	titanic_form = TitanicForm()
	return render(request, 'home.html', {'titanic_form': titanic_form})


def titanic(request):

	if request.method == 'POST':
		titanic_form = TitanicForm(request.POST)
		if titanic_form.is_valid():
			pclass = titanic_form.cleaned_data['pclass']
			age = titanic_form.cleaned_data['age']
			sibsp = titanic_form.cleaned_data['sibsp']
			parch = titanic_form.cleaned_data['parch']
			fare = titanic_form.cleaned_data['fare']
			sex = titanic_form.cleaned_data['sex']
			embarked = titanic_form.cleaned_data['embarked']

			X_test = pd.DataFrame(np.array([pclass, age, sibsp, parch, fare, sex, embarked]).reshape(1,-1), 
				columns=['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Sex', 'Embarked'])

			predictor = load("predictor.joblib")
			prediction = "Survived: Yes" if predictor.predict(X_test) == 1 else "Survived: No"

			return render(request, 'titanic.html', {'titanic_form': titanic_form, 'prediction': prediction})
	else:
		titanic_form = TitanicForm()
		return render(request, 'titanic.html', {'titanic_form': titanic_form})

	