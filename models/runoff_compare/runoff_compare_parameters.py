"""
HMS Runoff comparisino parameters
"""

from django import forms

# Allowed Date formats for django form
DATE_INPUT_FORMATS = ('%Y-%m-%d', '%m-%d-%Y', '%m-%d-%y','%m/%d/%Y', '%m/%d/%y', '%b %d %Y', '%b %d, %Y',
                      '%d %b %Y', '%d %b, %Y', '%B %d %Y', '%B %d, %Y', '%d %B %Y', '%d %B, %Y' )


class RunoffCompareFormInput(forms.Form):
    """
    Input form fields for runoff comparision.
    """
    latitude = forms.DecimalField(
        label='Latitude',
        initial=33.925575,
        required=True
    )
    longitude = forms.DecimalField(
        label='Longitude',
        initial=-83.356893,
        required=True
    )
    startDate = forms.DateField(
        label='Start Date',
        input_formats=DATE_INPUT_FORMATS
    )
    endDate = forms.DateField(
        label='End Date',
        input_formats=DATE_INPUT_FORMATS
    )
