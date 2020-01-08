from django import forms

class TitanicForm(forms.Form):
	PCLASS1 = 1
	PCLASS2 = 2
	PCLASS3 = 3
	PCLASS_CHOICES=[(PCLASS1,'1'), (PCLASS2,'2'), (PCLASS3, '3')]
	pclass = forms.TypedChoiceField(label='Passenger Class', coerce=int, choices=PCLASS_CHOICES)

	age = forms.FloatField(label='Age', min_value=0, max_value=100)
	sibsp = forms.IntegerField(label='Siblings and Spouces Aboard', min_value=0, max_value=20)
	parch = forms.IntegerField(label='Parents and Children Aboard', min_value=0, max_value=20)
	fare = forms.FloatField(label='Fare', min_value=0, max_value=1000)

	SEX_CHOICES = [('male', 'Male'), ('female', 'Female')]
	sex = forms.ChoiceField(label='Sex', choices=SEX_CHOICES)

	EMBARKED_CHOICES = [('C', 'Cherbourg'), ('Q', 'Queenstown'), ('S', 'Southampton')]
	embarked = forms.ChoiceField(label='Embarked', choices=EMBARKED_CHOICES)