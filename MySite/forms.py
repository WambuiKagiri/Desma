from django import forms
from bootstrap_datepicker.widgets import DatePicker

from .models import subscriber
from .models import listings_waiting_list
from .models import customer
from .models import booked_viewings,properties

class subscribe_form(forms.ModelForm):
	class Meta:
		model = subscriber
		fields = ['Email']

class list_form(forms.ModelForm):
	class Meta:
		model = listings_waiting_list
		fields = ['property_id','name','mobile_no','location','price','purpose','tyype']

class customer_form(forms.ModelForm):
	class Meta:
		model = customer
		fields = ['name','mobile_no','email']

class booking_form(forms.ModelForm):
	class Meta:
		model = booked_viewings
		fields = ['name','mobile_no','date']
		
class property_form(forms.ModelForm):
	description = forms.CharField( widget=forms.Textarea )
	class Meta:
		model = properties
		fields = '__all__'

	