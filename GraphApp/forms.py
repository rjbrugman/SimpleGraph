from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.

from django import forms

class GraphInputForm(forms.Form):
    # x_coefficient = forms.IntegerField(label="x coef", help_text="help", min_value=-10, max_value=10)
    x_coefficient = forms.IntegerField( min_value=-100, max_value=100)
    x_exponent = forms.IntegerField( min_value=-8, max_value=8)
    c_constant = forms.IntegerField(min_value=-100, max_value=100)

    x2_coefficient = forms.IntegerField(min_value=-100, max_value=100)
    x2_exponent = forms.IntegerField(min_value=-8, max_value=8)
    c2_constant = forms.IntegerField(min_value=-100, max_value=100)