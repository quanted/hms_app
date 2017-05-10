"""
HMS Hydrology Submodule Input form parameters

form setup has not been merged to allow for ease of changes for specific submodules as needed.
"""

from django import forms

# Sources for Precipitation
PRECIP_SOURCE_OPTIONS = (('NLDAS','NLDAS'),('GLDAS','GLDAS'),('DAYMET','DAYMET'), ('WGEN', 'WGEN'))

# Standard List of sources
STANDARD_SOURCE_OPTIONS = (('NLDAS','NLDAS'),('GLDAS','GLDAS'))

# Allowed Date formats for django form
DATE_INPUT_FORMATS = ('%Y-%m-%d', '%m-%d-%Y', '%m-%d-%y','%m/%d/%Y', '%m/%d/%y', '%b %d %Y', '%b %d, %Y',
                      '%d %b %Y', '%d %b, %Y', '%B %d %Y', '%B %d, %Y', '%d %B %Y', '%d %B, %Y' )


class HydrologyFormInput(forms.Form):
    source = forms.ChoiceField(
        label='Source',
        choices=STANDARD_SOURCE_OPTIONS,
        initial='NLDAS'
    )
    startDate = forms.DateField(
        label='Start Date',
        input_formats=DATE_INPUT_FORMATS
    )
    endDate = forms.DateField(
        label='End Date',
        input_formats=DATE_INPUT_FORMATS
    )
    spatial_input = forms.ChoiceField(
        label='Spatial Input',
        choices=(('coordinates', 'coordinates'), ('geojson', 'geojson'), ('geojson_file', 'geojson file')),
        initial='coordinates'
    )
    latitude = forms.DecimalField(
        label='Latitude',
        initial=33.925575,
        required=False
    )
    longitude = forms.DecimalField(
        label='Longitude',
        initial=-83.356893,
        required=False
    )
    geojson = forms.CharField(
        label='GeoJSON',
        required=False
    )
    geojson_file = forms.FileField(
        required=False
    )
    localTime = forms.ChoiceField(
        label='Local Time',
        choices=(('false', 'no'), ('true', 'yes'))
    )


class SubsurfaceflowFormInput(HydrologyFormInput):
    """
    Input form fields for subsurface flow data.
    default fields taken from HydrologyFormInput
    """



class EvapotranspirationFormInput(HydrologyFormInput):
    """
    Input form fields for evapotranspiration data.
    default fields taken from HydrologyFormInput
    """



class PrecipitationFormInput(HydrologyFormInput):
    """
    Input form fields for precipitation data.
    default fields taken from HydrologyFormInput
    """
    source = forms.ChoiceField(
        label='Source',
        choices=PRECIP_SOURCE_OPTIONS,
        initial='NLDAS'
    )

class SoilmoistureFormInput(HydrologyFormInput):
    """
    Input form fields for soil moisture data.
    default fields taken from HydrologyFormInput
    """
    layers = forms.ChoiceField(
        label='Layer Depth',
        choices=((0, '0-10cm'), (1, '10-40cm'),
                 (2, '40-100cm'), (3, '100-200cm'),
                 (4, '0-100cm'), (5, '0-200cm'))
    )


class SurfacerunoffFormInput(HydrologyFormInput):
    """
    Input form fields for surface runoff data.
    default fields taken from HydrologyFormInput
    """
    source = forms.ChoiceField(
        label='Source',
        choices= (('NLDAS','NLDAS'),('GLDAS','GLDAS'), ('curvenumber', 'Curve Number')),
        initial='NLDAS'
    )


class TemperatureFormInput(HydrologyFormInput):
    """
    Input form fields for temperature data.
    default fields taken from HydrologyFormInput
    """