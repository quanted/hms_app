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
    now_date = datetime.datetime.now()
    end_date = now_date + datetime.timedelta(hours=18)
    startCOMID = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'title': 'Starting segment for the stream network.'
        }),
        required=True,
        label="Start COMID",
        initial=6277141
    )
    endCOMID = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'title': 'Final segment for the stream network.'
        }),
        required=True,
        label="End COMID",
        initial=6275977
    )
    startDate = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'datepicker'
        }),
        required=True,
        label='Start Date',
        input_formats=DATE_INPUT_FORMATS,
        initial=now_date.strftime("%Y-%m-%d")
    )
    startHour = forms.IntegerField(
        widget=forms.TextInput(),
        required=True,
        label='Start Hour',
        max_value=23,
        min_value=0,
        initial=now_date.hour
    )
    endDate = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'datepicker'
        }),
        required=True,
        label='End Date',
        input_formats=DATE_INPUT_FORMATS,
        initial=end_date.strftime("%Y-%m-%d")
    )
    endHour = forms.IntegerField(
        widget=forms.TextInput(),
        required=True,
        label='End Hour',
        max_value=23,
        min_value=0,
        initial=end_date.hour
    )
    inflowSource = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Choose to input contaminant inflow data manually or download National Water Model forecast data.'
        }),
        label='Source of Contaminant Inflow Data',
        choices=(("Input Table", "Input Table"), ("National Water Model", "National Water Model")),
        initial="National Water Model"
    )
    field_order = ['startCOMID', 'endCOMID', 'startDate', 'startHour', 'endDate', 'endHour', 'inflowTable']
