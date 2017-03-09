"""
Precipitation parameters.
"""

from django import forms

SOURCE_OPTIONS = ['NLDAS','GLDAS','DAYMET']

class PrecipInput(forms.Form):
    source = forms.ChoiceField(
        label='Source',
        choices=SOURCE_OPTIONS,
        intial='NLDAS',
    )
    start_date = forms.DateField(
        label='Start Date',
    )
    end_date = forms.DateField(
        label='End Date',
    )
    latitude = forms.DecimalField(
        label='Latitude',
        intial=33.925575
    )
    longitude = forms.DecimalField(
        label='Longitude',
        intial=-83.356893
    )


