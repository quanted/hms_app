"""
HMS Hydrology Submodule Input form parameters

form setup has not been merged to allow for ease of changes for specific submodules as needed.
"""

from django import forms

# Sources for Precipitation
PRECIP_SOURCE_OPTIONS = (('NLDAS','NLDAS'),('GLDAS','GLDAS'),('DAYMET','DAYMET'))

# Standard List of sources
STANDARD_SOURCE_OPTIONS = (('NLDAS','NLDAS'),('GLDAS','GLDAS'))

# Allowed Date formats for django form
DATE_INPUT_FORMATS = ('%Y-%m-%d', '%m-%d-%Y', '%m-%d-%y','%m/%d/%Y', '%m/%d/%y', '%b %d %Y', '%b %d, %Y',
                      '%d %b %Y', '%d %b, %Y', '%B %d %Y', '%B %d, %Y', '%d %B %Y', '%d %B, %Y' )


class SubsurfaceflowFormInput(forms.Form):
    """
    Input form fields for subsurface flow data.
    """
    source = forms.ChoiceField(
        label='Source',
        choices=STANDARD_SOURCE_OPTIONS,
        initial='NLDAS',
        required=True
    )
    startDate = forms.DateField(
        label='Start Date',
        input_formats=DATE_INPUT_FORMATS,
        required=True
    )
    endDate = forms.DateField(
        label='End Date',
        input_formats=DATE_INPUT_FORMATS,
        required=True
    )
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
    localTime = forms.ChoiceField(
        label='Local Time',
        choices=(('false', 'no'), ('true', 'yes'))
    )


class EvapotranspirationFormInput(forms.Form):
    """
    Input form fields for evapotranspiration data.
    """
    source = forms.ChoiceField(
        label='Source',
        choices=STANDARD_SOURCE_OPTIONS,
        initial='NLDAS',
        required=True
    )
    startDate = forms.DateField(
        label='Start Date',
        input_formats=DATE_INPUT_FORMATS,
        required=True
    )
    endDate = forms.DateField(
        label='End Date',
        input_formats=DATE_INPUT_FORMATS,
        required=True
    )
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
    localTime = forms.ChoiceField(
        label='Local Time',
        choices=(('false', 'no'), ('true', 'yes'))
    )


class PrecipitationFormInput(forms.Form):
    """
    Input form fields for precipitation data.
    """
    source = forms.ChoiceField(
        label='Source',
        choices=PRECIP_SOURCE_OPTIONS,
        initial='NLDAS',
        required=True
    )
    startDate = forms.DateField(
        label='Start Date',
        input_formats=DATE_INPUT_FORMATS,
        required=True
    )
    endDate = forms.DateField(
        label='End Date',
        input_formats=DATE_INPUT_FORMATS,
        required=True
    )
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
    localTime = forms.ChoiceField(
        label='Local Time',
        choices=(('false', 'no'), ('true', 'yes'))
    )


class SoilmoistureFormInput(forms.Form):
    """
    Input form fields for soil moisture data.
    """
    source = forms.ChoiceField(
        label='Source',
        choices=STANDARD_SOURCE_OPTIONS,
        initial='NLDAS',
        required=True
    )
    startDate = forms.DateField(
        label='Start Date',
        input_formats=DATE_INPUT_FORMATS,
        required=True
    )
    endDate = forms.DateField(
        label='End Date',
        input_formats=DATE_INPUT_FORMATS,
        required=True
    )
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
    """
    Input form fields for surface runoff data.
    """
    source = forms.ChoiceField(
        label='Source',
        choices=STANDARD_SOURCE_OPTIONS,
        initial='NLDAS',
        required=True
    )
    startDate = forms.DateField(
        label='Start Date',
        input_formats=DATE_INPUT_FORMATS,
        required=True
    )
    endDate = forms.DateField(
        label='End Date',
        input_formats=DATE_INPUT_FORMATS,
        required=True
    )
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
    localTime = forms.ChoiceField(
        label='Local Time',
        choices=(('false', 'no'), ('true', 'yes'))
    )


class TemperatureFormInput(forms.Form):
    """
    Input form fields for temperature data.
    """
    source = forms.ChoiceField(
        label='Source',
        choices=STANDARD_SOURCE_OPTIONS,
        initial='NLDAS',
        required=True
    )
    startDate = forms.DateField(
        label='Start Date',
        input_formats=DATE_INPUT_FORMATS,
        required=True
    )
    endDate = forms.DateField(
        label='End Date',
        input_formats=DATE_INPUT_FORMATS,
        required=True
    )
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
    localTime = forms.ChoiceField(
        label='Local Time',
        choices=(('false', 'no'), ('true', 'yes'))
    )
