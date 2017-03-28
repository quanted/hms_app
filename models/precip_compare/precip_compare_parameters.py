"""
Precipitation comparision parameters
"""

from django import forms


class PrecipitationCompareFormInput(forms.Form):
    stationID = forms.CharField(
        label='NCDC StationID'
    )
    startDate = forms.DateField(
        label='Start Date'
    )
    endDate = forms.DateField(
        label='End Date'
    )

