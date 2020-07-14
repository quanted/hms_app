"""
HMS Workflow submodule Input form parameters
"""

from django import forms

# Sources for Precipitation
PRECIP_SOURCE_OPTIONS = (
('nldas', 'nldas'), ('gldas', 'gldas'), ('daymet', 'daymet'), ('prism', 'prism'), ('ncei', 'ncei'), ('trmm', 'trmm'))

# Sources for Temperature
TEMP_SOURCE_OPTIONS = (('nldas', 'nldas'), ('gldas', 'gldas'), ('daymet', 'daymet'), ('prism', 'prism'), ("ncei", "ncei"))

# Sources for Wind
WIND_SOURCE_OPTIONS = (('nldas', 'nldas'), ('gldas', 'gldas'), ('ncei', 'ncei'))

# Sources for Radiation
RAD_SOURCE_OPTIONS = (('nldas', 'nldas'), ('gldas', 'gldas'), ('daymet', 'daymet'))

# Sources for Humidity
HUMID_SOURCE_OPTIONS = (('prism', 'prism'),)

# Standard List of sources
STANDARD_SOURCE_OPTIONS = (('nldas', 'nldas'), ('gldas', 'gldas'))

# Allowed Date formats for django form
DATE_INPUT_FORMATS = ('%Y-%m-%d', '%m-%d-%Y', '%m-%d-%y', '%m/%d/%Y', '%m/%d/%y', '%b %d %Y', '%b %d, %Y',
                      '%d %b %Y', '%d %b, %Y', '%B %d %Y', '%B %d, %Y', '%d %B %Y', '%d %B, %Y')

DATA_OUTPUT_FORMATS = (
    ("E", "E"), ("E0", "E0"), ("E1", "E1"), ("E2", "E2"), ("E3", "E3"),
    ("e", "e"), ("e0", "e0"), ("e1", "e1"), ("e2", "e2"), ("e3", "e3"),
    ("F", "F"), ("F0", "F0"), ("F1", "F1"), ("F2", "F2"), ("F3", "F3"),
    ("G", "G"), ("G0", "G0"), ("G1", "G1"), ("G2", "G2"), ("G3", "G3"),
    ("N", "N"), ("N0", "N0"), ("N1", "N1"), ("N2", "N2"), ("N3", "N3"),
    ("R", "R")
)


class MeteorologyFormInput(forms.Form):
    source = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Data source of the dataset.'
        }),
        label='Source',
        choices=STANDARD_SOURCE_OPTIONS,
        initial='NLDAS',
        help_text='SOURCE TEMP HELP TEXT'
    )
    startDate = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'datepicker'
        }),
        label='Start Date',
        input_formats=DATE_INPUT_FORMATS,
        initial='01/01/2010',
        help_text='START DATE TEMP HELP TEXT'
    )
    endDate = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'datepicker'
        }),
        label='End Date',
        input_formats=DATE_INPUT_FORMATS,
        initial='12/31/2010',
        help_text='END DATE TEMP HELP TEXT'
    )
    latitude = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'title': 'Latitude value for area of interest.'
        }),
        label='Latitude',
        initial=33.925575,
        required=False,
        help_text='LATITUDE TEMP HELP TEXT'
    )
    longitude = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'title': 'Longitude value for area of interest.'
        }),
        label='Longitude',
        initial=-83.356893,
        required=False,
        help_text='LONGITUDE TEMP HELP TEXT'
    )
    # geometrymetadata = forms.CharField(
    #     widget=forms.Textarea(attrs={
    #         'title': 'Metadata for the area of interest. Provide key-value "," separated list using ":" to separate key'
    #                  ' and value.',
    #     }),
    #     label='Geometry Metadata',
    #     required=False
    # )
    timelocalized = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'If yes, set date/time timezone to local to the spatial area of interest or if no, to GMT.'
        }),
        label='Local Time',
        choices=(('false', 'GMT'), ('true', 'yes')),
        initial='true'
    )
    temporalresolution = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Temporal resolution of the output time series data.'
        }),
        label='Temporal Resolution',
        choices=(
            ("hourly", "hourly"), ("3hourly", "3hourly"), ("daily", "daily"), ("monthly", "monthly")
        ),
        initial="default",
        help_text='TEMPORAL RESOLUTION TEMP HELP TEXT'
    )
    # datetimeformat = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #         'title': 'Valid date format strings can be found here https://docs.microsoft.com/en-us/dotnet/standard/'
    #                  'base-types/custom-date-and-time-format-strings'
    #     }),
    #     label='Output Date Format',
    #     initial="yyyy-MM-dd HH",
    #     help_text='DATE TIME FORMAT TEMP HELP TEXT'
    # )
    outputformat = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Valid data format string can be found here https://docs.microsoft.com/en-us/dotnet/standard/'
                     'base-types/standard-numeric-format-strings'
        }),
        label='Output Data Format',
        choices=DATA_OUTPUT_FORMATS,
        initial="E3",
        help_text='OUTPUT FORMAT TEMP HELP TEXT'
    )


class PrecipitationFormInput(MeteorologyFormInput):
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
        initial='NLDAS',
        help_text='SOURCE TEMP HELP TEXT'
    )
    stationID = forms.CharField(
        widget=forms.TextInput(attrs={
            'title': 'NCEI station ID.'
        }
        ),
        label='NCEI StationID',
        initial='GHCND:USW00013874',
        help_text='STATIONID TEMP HELP TEXT'
    )
    area_of_interest = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Type of area of interest selection option'
        }),
        label='Area of Interest Options',
        choices=(("Latitude/Longitude", "Latitude/Longitude"), ("Catchment Centroid", "Catchment Centroid")),
        initial="Latitude/Longitude"
    )
    catchment_comid = forms.CharField(
        widget=forms.TextInput(attrs={
            'title': 'NHDPlus V2.1 Catchment COMID'
        }),
        label="Catchment COMID"
    )
    field_order = ['source', 'startDate', 'endDate', 'area_of_interest', 'latitude', 'longitude', "catchment_comid", 'stationID',
                   'geometrymetadata', 'timelocalized', 'temporalresolution', 'datetimeformat', 'outputformat']


class WindFormInput(MeteorologyFormInput):
    """
    Input form fields for wind data.
    default fields taken from HydrologyFormInput
    """
    source = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Data source of the dataset.'
        }),
        label='Source',
        choices=WIND_SOURCE_OPTIONS,
        initial='NLDAS',
        help_text='SOURCE TEMP HELP TEXT'
    )
    stationID = forms.CharField(
        widget=forms.TextInput(attrs={
            'title': 'NCEI station ID.'
        }
        ),
        label='NCEI StationID',
        initial='GHCND:USW00013874',
        help_text='STATIONID TEMP HELP TEXT'
    )
    # component = forms.ChoiceField(
    #     widget=forms.Select(attrs={
    #         'title': 'Desired component of wind.'
    #     }),
    #     label='Component',
    #     choices=(('u/v', 'u/v'), ('vel/deg', 'vel/deg'), ('all', 'all')),
    #     initial='all',
    #     help_text='COMPONENT TEMP HELP TEXT'
    # )
    area_of_interest = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Type of area of interest selection option'
        }),
        label='Area of Interest Options',
        choices=(("Latitude/Longitude", "Latitude/Longitude"), ("Catchment Centroid", "Catchment Centroid")),
        initial="Latitude/Longitude"
    )
    catchment_comid = forms.CharField(
        widget=forms.TextInput(attrs={
            'title': 'NHDPlus V2.1 Catchment COMID'
        }),
        label="Catchment COMID"
    )
    field_order = ['source', 'startDate', 'endDate', 'area_of_interest', 'latitude', 'longitude', "catchment_comid",
                   'stationID',
                   'geometrymetadata', 'timelocalized', 'temporalresolution', 'datetimeformat', 'outputformat']


class TemperatureFormInput(MeteorologyFormInput):
    """
    Input form fields for temperature data.
    default fields taken from HydrologyFormInput
    """
    source = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Data source of the dataset.'
        }),
        label='Source',
        choices=TEMP_SOURCE_OPTIONS,
        initial='NLDAS',
        help_text='SOURCE TEMP HELP TEXT'
    )
    stationID = forms.CharField(
        widget=forms.TextInput(attrs={
            'title': 'NCEI station ID.'
        }
        ),
        label='NCEI StationID',
        initial='GHCND:USW00013874',
        help_text='STATIONID TEMP HELP TEXT'
    )
    area_of_interest = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Type of area of interest selection option'
        }),
        label='Area of Interest Options',
        choices=(("Latitude/Longitude", "Latitude/Longitude"), ("Catchment Centroid", "Catchment Centroid")),
        initial="Latitude/Longitude"
    )
    catchment_comid = forms.CharField(
        widget=forms.TextInput(attrs={
            'title': 'NHDPlus V2.1 Catchment COMID'
        }),
        label="Catchment COMID"
    )
    field_order = ['source', 'startDate', 'endDate', 'area_of_interest', 'latitude', 'longitude', "catchment_comid", 'stationID',
                   'geometrymetadata', 'timelocalized', 'temporalresolution', 'datetimeformat', 'outputformat']


class RadiationFormInput(MeteorologyFormInput):
    """
    Input form fields for radiation data.
    default fields taken from HydrologyFormInput
    """
    source = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Data source of the dataset.'
        }),
        label='Source',
        choices=RAD_SOURCE_OPTIONS,
        initial='NLDAS',
        help_text='SOURCE TEMP HELP TEXT'
    )
    area_of_interest = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Type of area of interest selection option'
        }),
        label='Area of Interest Options',
        choices=(("Latitude/Longitude", "Latitude/Longitude"), ("Catchment Centroid", "Catchment Centroid")),
        initial="Latitude/Longitude"
    )
    catchment_comid = forms.CharField(
        widget=forms.TextInput(attrs={
            'title': 'NHDPlus V2.1 Catchment COMID'
        }),
        label="Catchment COMID"
    )
    field_order = ['source', 'startDate', 'endDate', 'area_of_interest', 'latitude', 'longitude', "catchment_comid",
                   'timelocalized', 'temporalresolution', 'datetimeformat', 'outputformat']



class HumidityFormInput(MeteorologyFormInput):
    """
    Input form fields for humidity data.
    default fields taken from HydrologyFormInput
    """
    source = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Data source of the dataset.'
        }),
        label='Source',
        choices=HUMID_SOURCE_OPTIONS,
        initial='prism',
        help_text='SOURCE TEMP HELP TEXT'
    )
    component = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Parameter: Relative Humidity/Dew Point Temperature'
        }),
        choices=(('relative', 'relative  humidity'), ('dewpoint', 'dew point')),
        initial='relative',
        label='Parameter',
        help_text='COMPONENT TEMP HELP TEXT'
    )
    area_of_interest = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Type of area of interest selection option'
        }),
        label='Area of Interest Options',
        choices=(("Latitude/Longitude", "Latitude/Longitude"), ("Catchment Centroid", "Catchment Centroid")),
        initial="Latitude/Longitude"
    )
    catchment_comid = forms.CharField(
        widget=forms.TextInput(attrs={
            'title': 'NHDPlus V2.1 Catchment COMID'
        }),
        label="Catchment COMID"
    )
    field_order = ['source', 'component', 'startDate', 'endDate', 'area_of_interest', 'latitude', 'longitude', "catchment_comid",
                   'timelocalized', 'temporalresolution', 'datetimeformat', 'outputformat']


class SolarcalculatorFormInput(forms.Form):
    model = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Calculate for a year or day.'
        }),
        label='Model',
        choices=(('year', 'year'), ('day', 'day')),
        initial='year',
        help_text='MODEL TEMP HELP TEXT'
    )
    area_of_interest = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Type of area of interest selection option'
        }),
        label='Area of Interest Options',
        choices=(("Latitude/Longitude", "Latitude/Longitude"), ("Catchment Centroid", "Catchment Centroid")),
        initial="Latitude/Longitude"
    )
    catchment_comid = forms.CharField(
        widget=forms.TextInput(attrs={
            'title': 'NHDPlus V2.1 Catchment COMID'
        }),
        label="Catchment COMID"
    )
    latitude = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'title': 'Latitude value for area of interest.'
        }),
        label='Latitude',
        initial=33.925575,
        required=False,
        help_text='LATITUDE TEMP HELP TEXT'
    )
    longitude = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'title': 'Longitude value for area of interest.'
        }),
        label='Longitude',
        initial=-83.356893,
        required=False,
        help_text='LONGITUDE TEMP HELP TEXT'
    )
    timezone = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'title': 'Timezone for the specified location.'
        }),
        label='Time Zone',
        initial=-7,
        required=False,
        help_text='TIMEZONE TEMP HELP TEXT'
    )
    local_time = forms.CharField(
        widget=forms.TextInput(attrs={
            'title': 'Local time in hh:mm:ss format for the local time to use in the solar calculator.',
        }),
        label='Local Time',
        initial='12:00:00',
        required=False,
        help_text='LOCALTIME TEMP HELP TEXT'
    )
    year = forms.CharField(
        widget=forms.TextInput(attrs={
            'title': 'Year to run solar calculator.'
        }),
        label='Year',
        initial='2010',
        required=False,
        help_text='YEAR TEMP HELP TEXT'
    )
    date = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'datepicker'
        }),
        label='Date',
        input_formats=DATE_INPUT_FORMATS,
        initial='2010-06-10',
        help_text='DATE TEMP HELP TEXT'
    )

