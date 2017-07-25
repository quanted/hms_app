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
        widget=forms.Select(attrs={
           'title': 'Data source of the dataset.'
        }),
        label='Source',
        choices=STANDARD_SOURCE_OPTIONS,
        initial='NLDAS'
    )
    startDate = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'datepicker'
        }),
        label='Start Date',
        input_formats=DATE_INPUT_FORMATS
    )
    endDate = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'datepicker'
        }),
        label='End Date',
        input_formats=DATE_INPUT_FORMATS
    )
    # spatial_input = forms.ChoiceField(
    #     label='Spatial Input',
    #     choices=(('coordinates', 'coordinates'), ('geojson', 'geojson'), ('geojson_file', 'geojson file')),
    #     initial='coordinates'
    # )
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
    spatial_metadata = forms.CharField(
        widget=forms.Textarea(attrs={
            'title': 'Metadata for the area of interest. Provide key-value "," separated list using ":" to separate key'
                     ' and value.',
        }),
        required=False
    )
    localTime = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Set date/time timezone to local, specified by latitude and longitude values, or to GMT.'
        }),
        label='Local Time',
        choices=(('false', 'no'), ('true', 'yes')),
        initial='true'
    )
    temporalresolution = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Temporal resolution of the output time series data.'
        }),
        label='Temporal Resolution',
        choices=(("default", "default"), ("daily", "daily"), ("weekly", "weekly"), ("monthly", "monthly")),
        initial="default"
    )
    output_date_format = forms.CharField(
        widget=forms.TextInput(attrs={
            'title': 'Valid date format strings can be found here https://docs.microsoft.com/en-us/dotnet/standard/'
                     'base-types/custom-date-and-time-format-strings'
        }),
        label='Output Date Format',
        initial="yyyy-MM-dd HH"
    )
    output_data_format = forms.CharField(
        widget=forms.TextInput(attrs={
            'title': 'Valid data format string can be found here https://docs.microsoft.com/en-us/dotnet/standard/'
                     'base-types/standard-numeric-format-strings'
        }),
        label='Output Data Format',
        initial="E3"
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
        widget=forms.Select(attrs={
           'title': 'Data source of the dataset.'
        }),
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
        widget=forms.Select(attrs={
            'title': 'Please select the desired soil moisture depth.'
        }),
        label='Layer Depth',
        choices=(('0_10', '0-10cm'), ('10_40', '10-40cm'),
                 ('40_100', '40-100cm'), ('100_200', '100-200cm'),
                 ('0_100', '0-100cm'), ('0_200', '0-200cm'))
    )


class SurfacerunoffFormInput(HydrologyFormInput):
    """
    Input form fields for surface runoff data.
    default fields taken from HydrologyFormInput
    """
    source = forms.ChoiceField(
        widget=forms.Select(attrs={
           'title': 'Data source of the dataset.'
        }),
        label='Source',
        choices= (('NLDAS','NLDAS'),('GLDAS','GLDAS'), ('curvenumber', 'Curve Number')),
        initial='NLDAS'
    )


class TemperatureFormInput(HydrologyFormInput):
    """
    Input form fields for temperature data.
    default fields taken from HydrologyFormInput
    """