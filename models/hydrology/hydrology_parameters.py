"""
Precipitation parameters.
"""

from django import forms

PRECIP_SOURCE_OPTIONS = (('NLDAS','NLDAS'),('GLDAS','GLDAS'),('DAYMET','DAYMET'))
STANDARD_SOURCE_OPTIONS = (('NLDAS','NLDAS'),('GLDAS','GLDAS'))

# the names of the fields for the form must match those of for the HMS input parameters
class BaseflowFormInput(forms.Form):
    source = forms.ChoiceField(
        label='Source',
        choices=STANDARD_SOURCE_OPTIONS,
        #intial='NLDAS',
    )
    startDate = forms.DateField(
        label='Start Date',
    )
    endDate = forms.DateField(
        label='End Date',
    )
    latitude = forms.DecimalField(
        label='Latitude',
        #intial=33.925575
    )
    longitude = forms.DecimalField(
        label='Longitude',
        #intial=-83.356893
    )
    localTime = forms.ChoiceField(
        label='Local Time',
        choices=(('true','yes'),('false', 'no'))
    )


class EvapotranspirationFormInput(forms.Form):
    source = forms.ChoiceField(
        label='Source',
        choices=STANDARD_SOURCE_OPTIONS,
        #intial='NLDAS',
    )
    startDate = forms.DateField(
        label='Start Date',
    )
    endDate = forms.DateField(
        label='End Date',
    )
    latitude = forms.DecimalField(
        label='Latitude',
        #intial=33.925575
    )
    longitude = forms.DecimalField(
        label='Longitude',
        #intial=-83.356893
    )
    localTime = forms.ChoiceField(
        label='Local Time',
        choices=(('true','yes'),('false', 'no'))
    )


class PrecipitationFormInput(forms.Form):
    source = forms.ChoiceField(
        label='Source',
        choices=PRECIP_SOURCE_OPTIONS,
        #intial='NLDAS',
    )
    startDate = forms.DateField(
        label='Start Date',
    )
    endDate = forms.DateField(
        label='End Date',
    )
    latitude = forms.DecimalField(
        label='Latitude',
        #intial=33.925575
    )
    longitude = forms.DecimalField(
        label='Longitude',
        #intial=-83.356893
    )
    localTime = forms.ChoiceField(
        label='Local Time',
        choices=(('true','yes'),('false', 'no'))
    )


class SoilMoistureFormInput(forms.Form):
    source = forms.ChoiceField(
        label='Source',
        choices=STANDARD_SOURCE_OPTIONS,
        #intial='NLDAS',
    )
    startDate = forms.DateField(
        label='Start Date',
    )
    endDate = forms.DateField(
        label='End Date',
    )
    latitude = forms.DecimalField(
        label='Latitude',
        #intial=33.925575
    )
    longitude = forms.DecimalField(
        label='Longitude',
        #intial=-83.356893
    )
    localTime = forms.ChoiceField(
        label='Local Time',
        choices=(('true','yes'),('false', 'no'))
    )
    layers = forms.ChoiceField(
        label='Layer Depth',
        choices=((0, '0-10cm'), (1, '10-40cm'),
                 (2, '40-100cm'), (3, '100-200cm'),
                 (4, '0-100cm'), (5, '0-200cm'))
    )


class SurfacerunoffFormInput(forms.Form):
    source = forms.ChoiceField(
        label='Source',
        choices=STANDARD_SOURCE_OPTIONS,
        #intial='NLDAS',
    )
    startDate = forms.DateField(
        label='Start Date',
    )
    endDate = forms.DateField(
        label='End Date',
    )
    latitude = forms.DecimalField(
        label='Latitude',
        #intial=33.925575
    )
    longitude = forms.DecimalField(
        label='Longitude',
        #intial=-83.356893
    )
    localTime = forms.ChoiceField(
        label='Local Time',
        choices=(('true','yes'),('false', 'no'))
    )

class TemperatureFormInput(forms.Form):
    source = forms.ChoiceField(
        label='Source',
        choices=STANDARD_SOURCE_OPTIONS,
        #intial='NLDAS',
    )
    startDate = forms.DateField(
        label='Start Date',
    )
    endDate = forms.DateField(
        label='End Date',
    )
    latitude = forms.DecimalField(
        label='Latitude',
        #intial=33.925575
    )
    longitude = forms.DecimalField(
        label='Longitude',
        #intial=-83.356893
    )
    localTime = forms.ChoiceField(
        label='Local Time',
        choices=(('true','yes'),('false', 'no'))
    )