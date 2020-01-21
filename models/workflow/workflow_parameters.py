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
        input_formats=DATE_INPUT_FORMATS
    )
    startHour = forms.IntegerField(
        widget=forms.TextInput(),
        required=True,
        label='Start Hour',
        max_value=23,
        min_value=0
    )
    endDate = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'datepicker'
        }),
        required=True,
        label='End Date',
        input_formats=DATE_INPUT_FORMATS
    )
    endHour = forms.IntegerField(
        widget=forms.TextInput(),
        required=True,
        label='End Hour',
        max_value=23,
        min_value=0
    )
    field_order = ['startCOMID', 'endCOMID', 'startDate', 'startHour', 'endDate', 'endHour']
