
from django import forms
from .models import Record

 
class RecordCreateForm(forms.ModelForm):
   class Meta:
     model = Record
     fields = ['date', 'eventname', 'adobe', 'record','hero','source','note']

class RecordUpdateForm(forms.ModelForm):
	class Meta:
		model = Record
		fields = ['date', 'eventname', 'adobe', 'record','hero','source','note']