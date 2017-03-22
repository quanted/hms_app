"""
Precipitation parameters.
"""
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms
from datetime import datetime, timedelta


PRECIP_SOURCE_OPTIONS = (('NLDAS','NLDAS'),('GLDAS','GLDAS'),('DAYMET','DAYMET'))
STANDARD_SOURCE_OPTIONS = (('NLDAS','NLDAS'),('GLDAS','GLDAS'))

# the names of the fields for the form must match those of for the HMS input parameters
class BaseflowFormInput(forms.Form):
    source = forms.ChoiceField(
        label='Source',
        choices=STANDARD_SOURCE_OPTIONS,
        initial='NLDAS',
    )
    startDate = forms.DateField(
        label='Start Date'
    )
    endDate = forms.DateField(
        label='End Date'
    )
    latitude = forms.DecimalField(
        label='Latitude',
        initial=33.925575
    )
    longitude = forms.DecimalField(
        label='Longitude',
        initial=-83.356893
    )
    localTime = forms.ChoiceField(
        label='Local Time',
        choices=(('false', 'no'), ('true', 'yes'))
    )

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     startDate = cleaned_data.get("startDate")
    #     endDate = cleaned_data.get("endDate")
    #     source = cleaned_data.get("source")
    #     latitude = cleaned_data.get("latitude")
    #     longitude = cleaned_data.get("longitude")
    #
    #     print'source: ', source
    #     if type(startDate) is not datetime.date:
    #         print 'startDate: ', startDate
    #         raise forms.ValidationError("Start date must be a valid date")
    #     if type(endDate) is not datetime.date:
    #         print 'endDate: ', endDate
    #         raise forms.ValidationError("End date must be a valid date")
    #     if startDate > endDate:
    #         raise forms.ValidationError("Start date must be before end date.")
    #     if source == "NLDAS":
    #         nldas_start = datetime.today() - timedelta(days=5)
    #         #print(type(endDate))
    #         #print(endDate)
    #         if endDate > nldas_start:
    #             raise forms.ValidationError("End date must be before %s", nldas_start)
    #     elif source == "GLDAS":
    #         gldas_start = datetime.today() - timedelta(days=65)
    #         if endDate > gldas_start:
    #             raise forms.ValidationError("End date must be before %s", gldas_start)
    #     if latitude > 90 or latitude < -90:
    #         raise forms.ValidationError("Invalid latitude value, must be less than 90 and greater than -90.")
    #     if longitude > 180 or longitude < -180:
    #         raise forms.ValidationError("Invalid longitude value, must be less than 180 and greater than -90")
    #     return cleaned_data


class EvapotranspirationFormInput(forms.Form):
    source = forms.ChoiceField(
        label='Source',
        choices=STANDARD_SOURCE_OPTIONS,
        initial='NLDAS',
    )
    startDate = forms.DateField(
        label='Start Date',
    )
    endDate = forms.DateField(
        label='End Date',
    )
    latitude = forms.DecimalField(
        label='Latitude',
        initial=33.925575,
    )
    longitude = forms.DecimalField(
        label='Longitude',
        initial=-83.356893,
    )
    localTime = forms.ChoiceField(
        label='Local Time',
        choices=(('false', 'no'), ('true', 'yes'))
    )


class PrecipitationFormInput(forms.Form):
    source = forms.ChoiceField(
        label='Source',
        choices=PRECIP_SOURCE_OPTIONS,
        initial='NLDAS',
    )
    startDate = forms.DateField(
        label='Start Date',
    )
    endDate = forms.DateField(
        label='End Date',
    )
    latitude = forms.DecimalField(
        label='Latitude',
        initial=33.925575,
    )
    longitude = forms.DecimalField(
        label='Longitude',
        initial=-83.356893,
    )
    localTime = forms.ChoiceField(
        label='Local Time',
        choices=(('false', 'no'), ('true', 'yes'))
    )


class SoilmoistureFormInput(forms.Form):
    source = forms.ChoiceField(
        label='Source',
        choices=STANDARD_SOURCE_OPTIONS,
        initial='NLDAS',
    )
    startDate = forms.DateField(
        label='Start Date',
    )
    endDate = forms.DateField(
        label='End Date',
    )
    latitude = forms.DecimalField(
        label='Latitude',
        initial=33.925575,
    )
    longitude = forms.DecimalField(
        label='Longitude',
        initial=-83.356893,
    )
    localTime = forms.ChoiceField(
        label='Local Time',
        choices=(('false', 'no'), ('true', 'yes'))
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
        initial='NLDAS',
    )
    startDate = forms.DateField(
        label='Start Date',
    )
    endDate = forms.DateField(
        label='End Date',
    )
    latitude = forms.DecimalField(
        label='Latitude',
        initial=33.925575,
    )
    longitude = forms.DecimalField(
        label='Longitude',
        initial=-83.356893,
    )
    localTime = forms.ChoiceField(
        label='Local Time',
        choices=(('false', 'no'), ('true', 'yes'))
    )


class TemperatureFormInput(forms.Form):
    source = forms.ChoiceField(
        label='Source',
        choices=STANDARD_SOURCE_OPTIONS,
        initial='NLDAS',
    )
    startDate = forms.DateField(
        label='Start Date',
    )
    endDate = forms.DateField(
        label='End Date',
    )
    latitude = forms.DecimalField(
        label='Latitude',
        initial=33.925575,
    )
    longitude = forms.DecimalField(
        label='Longitude',
        initial=-83.356893,
    )
    localTime = forms.ChoiceField(
        label='Local Time',
        choices=(('false', 'no'), ('true', 'yes'))
    )
