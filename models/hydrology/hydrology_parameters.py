"""
HMS Hydrology Submodule Input form parameters
"""

from django import forms

# Sources for Precipitation
PRECIP_SOURCE_OPTIONS = (
('nldas', 'nldas'), ('gldas', 'gldas'), ('daymet', 'daymet'), ('wgen', 'wgen'), ('prism', 'prism'), ('ncdc', 'ncdc'))

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


class HydrologyFormInput(forms.Form):
    source = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Data source of the dataset.'
        }),
        label='Source',
        choices=STANDARD_SOURCE_OPTIONS,
        initial='nldas'
    )
    startDate = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'datepicker'
        }),
        label='Start Date',
        input_formats=DATE_INPUT_FORMATS,
        initial='2010-01-01'
    )
    endDate = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'datepicker'
        }),
        label='End Date',
        input_formats=DATE_INPUT_FORMATS,
        initial='2010-12-31'
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
    timelocalized = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Set date/time timezone to local, specified by latitude and longitude values, or to GMT.'
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
            ("hourly", "hourly"), ("3hourly", "3hourly"),
            ("daily", "daily"), ("weekly", "weekly"), ("monthly", "monthly")
        ),
        initial="default"
    )
    outputformat = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Valid data format string can be found here https://docs.microsoft.com/en-us/dotnet/standard/'
                     'base-types/standard-numeric-format-strings'
        }),
        label='Output Data Format',
        choices=DATA_OUTPUT_FORMATS,
        initial="E3"
    )


class SubsurfaceflowFormInput(HydrologyFormInput):
    """
    Input form fields for subsurface flow data.
    default fields taken from HydrologyFormInput
    """


class MonthlyWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = [
            forms.NumberInput(attrs={'class': 'monthly', 'title': 'January'}),
            forms.NumberInput(attrs={'class': 'monthly', 'title': 'February'}),
            forms.NumberInput(attrs={'class': 'monthly', 'title': 'March'}),
            forms.NumberInput(attrs={'class': 'monthly', 'title': 'April'}),
            forms.NumberInput(attrs={'class': 'monthly', 'title': 'May'}),
            forms.NumberInput(attrs={'class': 'monthly', 'title': 'June'}),
            forms.NumberInput(attrs={'class': 'monthly', 'title': 'July'}),
            forms.NumberInput(attrs={'class': 'monthly', 'title': 'August'}),
            forms.NumberInput(attrs={'class': 'monthly', 'title': 'September'}),
            forms.NumberInput(attrs={'class': 'monthly', 'title': 'October'}),
            forms.NumberInput(attrs={'class': 'monthly', 'title': 'November'}),
            forms.NumberInput(attrs={'class': 'monthly', 'title': 'December'}),
        ]
        super(MonthlyWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split(' ')
        return [None, None, None, None, None, None, None, None, None, None, None, None]


class Monthly(forms.MultiValueField):
    widget = MonthlyWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.DecimalField(required=False),
            forms.DecimalField(required=False),
            forms.DecimalField(required=False),
            forms.DecimalField(required=False),
            forms.DecimalField(required=False),
            forms.DecimalField(required=False),
            forms.DecimalField(required=False),
            forms.DecimalField(required=False),
            forms.DecimalField(required=False),
            forms.DecimalField(required=False),
            forms.DecimalField(required=False),
            forms.DecimalField(required=False),
        )
        super(Monthly, self).__init__(fields, require_all_fields=False, *args, **kwargs)

    def compress(self, data_list):
        return data_list


class EvapotranspirationFormInput(HydrologyFormInput):
    """
    Input form fields for evapotranspiration data.
    default fields taken from HydrologyFormInput
    """
    """
    old choices=(('nldas', 'nldas'), ('gldas', 'gldas'), ('hamon', 'hamon'), ('priestlytaylor', 'priestlytaylor'),
                 ('grangergray', 'grangergray'),
                 ('penpan', 'penpan'), ('mcjannett', 'mcjannett'), ('penmanopenwater', 'penmanopenwater'),
                 ('penmandaily', 'penmandaily'),
                 ('penmanhourly', 'penmanhourly'), ('mortoncrae', 'mortoncrae'), ('mortoncrwe', 'mortoncrwe'),
                 ('shuttleworthwallace', 'shuttleworthwallace'),
                 ('hspf', 'hspf'))
    """
    source = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Evapotranspiration data source.'
        }),
        label='Source',
        choices=(('nldas', 'nldas'), ('gldas', 'gldas'), ('daymet', 'daymet')),
        initial='NLDAS'
    )
    algorithm = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Evapotranspiration algorithm.'
        }),
        label='Algorithm',
        choices=(('nldas', 'nldas'), ('gldas', 'gldas'), ('hamon', 'hamon'), ('penmandaily', 'penmandaily'), ('hargreaves', 'hargreaves')),
        initial='NLDAS'
    )
    userdata = forms.FileField(
        widget=forms.ClearableFileInput(attrs={
            'title': 'Must contain following parameters: year, julianday, daylight(hours), solar radiation(W/m^2), max temperature(deg c), min temperature(deg c), vapor pressure(Pa).',
            'accept': '.csv'
        }),
        label='Custom data file upload (.csv)',
        required=False
    )
    # stationID = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #         'title': 'NCDC station ID.'
    #     }
    #     ),
    #     label='NCDC StationID',
    #     initial='GHCND:USW00013874'
    # )
    albedo = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'title': 'Albedo coefficient.'
        }),
        label='Albedo',
        initial=0.23,
        required=False
    )
    centlong = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'title': 'Central Longitude of Time Zone in degrees.'
        }),
        label='Central Longitude',
        initial=75.0,
        required=False
    )
    sunangle = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'title': 'Angle of the sun in degrees.'
        }),
        label='Sun Angle',
        initial=17.2,
        required=False
    )
    emissivity = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'title': 'Ratio representing radiant energy emission.'
        }),
        label='Emissivity',
        initial=0.92,
        required=False
    )
    model = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Specifies if potential, actual, or wet environment evaporation model is used.'
        }),
        label='Model',
        choices=(('ETP', 'ETP'), ('ETW', 'ETW'), ('ETA', 'ETA')),
        initial='ETP',
        required=False
    )
    zenith = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'title': 'Zenith Albedo coefficient.'
        }),
        label='Zenith',
        initial=0.05,
        required=False
    )
    lakesurfarea = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'title': 'Surface area of lake in square kilometers.'
        }),
        label='Lake Surface Area',
        initial=0.005,
        required=False
    )
    lakedepth = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'title': 'Average depth of lake in meters.'
        }),
        label='Lake Depth',
        initial=0.2,
        required=False
    )
    subsurfres = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'title': 'Subsurface Resistance.'
        }),
        label='Subsurface Resistance',
        initial=500.0,
        required=False
    )
    stomres = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'title': 'Stomatal Resistance.'
        }),
        label='Stomatal Resistance',
        initial=400.0,
        required=False
    )
    leafwidth = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'title': 'Leaf Width in meters.'
        }),
        label='Leaf Width',
        initial=0.02,
        required=False
    )
    roughlength = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'title': 'Roughness Length in meters.'
        }),
        label='Roughness Length',
        initial=0.02,
        required=False
    )
    vegheight = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'title': 'Vegetation Height in meters.'
        }),
        label='Vegetation Height',
        initial=0.12,
        required=False
    )
    leafarea = Monthly(label="Monthly Leaf Area Indices", required=False)
    airtemps = Monthly(label="Monthly Air Temperature Coefficients", required=False)
    field_order = ['algorithm', 'source', 'startDate', 'endDate', 'area_of_interest', 'latitude', 'longitude', "catchment_comid",
                   'timelocalized', 'temporalresolution', 'outputformat']


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
    stationID = forms.CharField(
        widget=forms.TextInput(attrs={
            'title': 'NCDC station ID.'
        }
        ),
        label='NCDC StationID',
        initial='GHCND:USW00013874'
    )
    field_order = ['source', 'startDate', 'endDate', 'latitude', 'longitude', 'stationID',
                   'geometrymetadata', 'timelocalized', 'temporalresolution', 'datetimeformat', 'outputformat']


class SoilmoistureFormInput(HydrologyFormInput):
    """
    Input form fields for soil moisture data.
    default fields taken from HydrologyFormInput
    """
    layers = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={
            'title': 'Please select the desired soil moisture depth.'
        }),
        label='Layer Depth',
        choices=(('0-10', '0-10cm'), ('10-40', '10-40cm'),
                 ('40-100', '40-100cm'), ('100-200', '100-200cm'),
                 ('0-100', '0-100cm'), ('0-200', '0-200cm'))
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
        choices=(('nldas', 'nldas'), ('gldas', 'gldas'), ('curvenumber', 'Curve Number')),
        initial='nldas'
    )


class TemperatureFormInput(HydrologyFormInput):
    """
    Input form fields for temperature data.
    default fields taken from HydrologyFormInput
    """
