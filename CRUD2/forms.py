from django import forms
from .models import INFO



class EmployeeForm(forms.ModelForm):

	class Meta:

		model = INFO
		fields = ('fullname','age','telephone','description')
		labels = {
		'fullname':'Full Name',
		'telephone':'Phone Number'
		}


	def __init__(self, *args, **kwargs):
		super(EmployeeForm,self).__init__(*args, **kwargs)	
		self.fields['description'].empty_label= "Select"
		#self.fields['age'].required = False