from django import forms
from first.models import CustomerRegisterDB


class CustomerRegisterForm(forms.ModelForm):
    class Meta:
        model = CustomerRegisterDB
        fields = "__all__"

