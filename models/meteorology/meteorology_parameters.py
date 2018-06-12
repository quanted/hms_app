"""
HMS Meteorology submodule Input form parameters
"""

from django import forms


DATE_INPUT_FORMATS = ('%Y-%m-%d', '%m-%d-%Y', '%m-%d-%y', '%m/%d/%Y', '%m/%d/%y', '%b %d %Y', '%b %d, %Y',
                      '%d %b %Y', '%d %b, %Y', '%B %d %Y', '%B %d, %Y', '%d %B %Y', '%d %B, %Y')


class SolarcalculatorFormInput(forms.Form):
    model = forms.ChoiceField(
        widget=forms.Select(attrs={
           'title': 'Calculate for a year or day.'
        }),
        label='Model',
        choices=(('year', 'year'), ('day', 'day')),
        initial='year'
    )
    latitude = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'title': 'Latitude value for area of interest.'
        }),
        label='Latitude',
        initial=33.925575,
        required=False
    )
    longitude = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'title': 'Longitude value for area of interest.'
        }),
        label='Longitude',
        initial=-83.356893,
        required=False
    )
    timezone = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'title': 'Timezone for the specified location.'
        }),
        label='Time Zone',
        initial=-7,
        required=False
    )
    local_time = forms.CharField(
        widget=forms.TextInput(attrs={
            'title': 'Local time in hh:mm:ss format for the local time to use in the solar calculator.',
        }),
        label='Local Time',
        initial='12:00:00',
        required=False
    )
    year = forms.CharField(
        widget=forms.TextInput(attrs={
            'title': 'Year to run solar calculator.'
        }),
        label='Year',
        initial='2010',
        required=False
    )
    date = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'datepicker'
        }),
        label='Date',
        input_formats=DATE_INPUT_FORMATS,
        initial='2010-06-10'
    )

#did not add temperature or precipitation because they use the hydrology FormInput -js