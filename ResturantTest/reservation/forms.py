from django import forms
from .models import Reservation
class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reservation
        # fields = ['name', 'email', 'phone', 'number', 'date', 'time']
        fields = '__all__'
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if not phone.isdigit():
            raise forms.ValidationError('Please enter your phone correct')
        return phone