"""
HMS Precipitation comparision parameters
"""

from django import forms

# Allowed Date formats for django form
DATE_INPUT_FORMATS = ('%Y-%m-%d', '%m-%d-%Y', '%m-%d-%y','%m/%d/%Y', '%m/%d/%y', '%b %d %Y', '%b %d, %Y',
                      '%d %b %Y', '%d %b, %Y', '%B %d %Y', '%B %d, %Y', '%d %B %Y', '%d %B, %Y' )


class PrecipitationCompareFormInput(forms.Form):
    """
    Input form fields for precipitation comparision.
    """
    stationID = forms.CharField(
        widget=forms.TextInput(attrs={
                'title': 'NCDC station ID.'
            }
        ),
        label='NCDC StationID'
    )
    startDate = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'datepicker'
        }),
        label='Start Date',
        input_formats=DATE_INPUT_FORMATS
    )
    endDate = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'datepicker'
        }),
        label='End Date',
        input_formats=DATE_INPUT_FORMATS
    )

