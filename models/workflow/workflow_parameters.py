"""
HMS Workflow submodule Input form parameters
"""

import datetime
from django import forms

DATE_INPUT_FORMATS = ('%Y-%m-%d', '%m-%d-%Y', '%m-%d-%y', '%m/%d/%Y', '%m/%d/%y', '%b %d %Y', '%b %d, %Y',
                      '%d %b %Y', '%d %b, %Y', '%B %d %Y', '%B %d, %Y', '%d %B %Y', '%d %B, %Y')


class TimeOfTravelFormInput(forms.Form):
    """
    Input form fields for time of travel data.
    """
    startCOMID = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'title': 'Starting segment for the stream network.'
        }),
        required=True,
        label="Start COMID"
    )
    endCOMID = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'title': 'Final segment for the stream network.'
        }),
        required=True,
        label="End COMID"
    )
    startDate = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'datepicker'
        }),
        required=True,
        label='Start Date',
        input_formats=DATE_INPUT_FORMATS,
        initial=datetime.datetime.now().strftime("%Y-%m-%d")
    )
    endDate = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'datepicker'
        }),
        required=True,
        label='End Date',
        input_formats=DATE_INPUT_FORMATS,
        initial=(datetime.datetime.now() + datetime.timedelta(hours=18)).strftime("%Y-%m-%d")
    )

    field_order = ['startCOMID', 'endCOMID', 'startDate', 'endDate']

