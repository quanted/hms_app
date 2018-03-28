"""
HMS Hydrodynamic Submodule Input form parameters
"""

from django import forms

# Sources for Precipitation
PRECIP_SOURCE_OPTIONS = (('nldas', 'nldas'), ('gldas', 'gldas'), ('daymet', 'daymet'), ('wgen', 'wgen'), ('prism', 'prism'), ('ncdc', 'ncdc'))

# Standard List of sources
STANDARD_SOURCE_OPTIONS = (('nldas', 'nldas'), ('gldas', 'gldas'))

# Allowed Date formats for django form
DATE_INPUT_FORMATS = ('%Y-%m-%d', '%m-%d-%Y', '%m-%d-%y', '%m/%d/%Y', '%m/%d/%y', '%b %d %Y', '%b %d, %Y',
                      '%d %b %Y', '%d %b, %Y', '%B %d %Y', '%B %d, %Y', '%d %B %Y', '%d %B, %Y')


class HydrodynamicFormInput(forms.Form):
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
    deltaT = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'title': 'Enter the timestep [hours].'
        }),
        label='Delta t',
        initial=1
    )
    datetimeformat = forms.CharField(
        widget=forms.TextInput(attrs={
            'title': 'Valid date format strings can be found here https://docs.microsoft.com/en-us/dotnet/standard/'
                     'base-types/custom-date-and-time-format-strings'
        }),
        label='Output Date Format',
        initial="yyyy-MM-dd HH"
    )
    outputformat = forms.CharField(
        widget=forms.TextInput(attrs={
            'title': 'Valid data format string can be found here https://docs.microsoft.com/en-us/dotnet/standard/'
                     'base-types/standard-numeric-format-strings'
        }),
        label='Output Data Format',
        initial="E3"
    )


class ConstantvolumeFormInput(HydrodynamicFormInput):
    """
    Input form fields for flow routing data.
    default fields taken from HydrodynamicFormInput
    """
    volume = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'title': 'Enter the volume [m3].'
        }),
        label='Volume',
        initial=1
    )
    modeldomain = forms.CharField(
        widget=forms.Textarea(attrs={
            'title': 'Boundary conditions for each segment. Provide "," separated list of the Boundary Flow [m3/s]  '
                     '  for each day. Order first segment to last.',
        }),
        label='Boundary Flow',
        required=True
    )

class ChangingvolumeFormInput(HydrodynamicFormInput):
    """
    Input form fields for flow routing data.
    default fields taken from HydrodynamicFormInput
    """

    modeldomain = forms.CharField(
        widget=forms.Textarea(attrs={
            'title': 'Channel geometry and boundary conditions for each segment. Provide "," separated list with a '
                     'new line for each segment. List should be ordered: Segment Length [m], Segment Bottom Width [m], '
                     'Segment Depth [m], and Boundary Flow [m3/s], Z-slope*, Depth Multiplier, and Depth Exponent. Order first segment to last.',
        }),
        label='Model Domain',
        required=True
    )


class KinematicwaveFormInput(HydrodynamicFormInput):
    """
    Input form fields for flow routing data.
    default fields taken from HydrodynamicFormInput
    """
    modeldomain = forms.CharField(
        widget=forms.Textarea(attrs={
            'title': 'Channel geometry and boundary conditions for each segment. Provide "," separated list with a '
                     'new line for each segment. List should be ordered: Segment Length [m], Segment Bottom Width [m], '
                     'Segment Depth [m], and Boundary Flow [m3/s], Z-slope*, Manning\'s Roughness, and Channel Slope. '
                     'Order first segment to last.',
        }),
        label='Model Domain',
        required=True
    )
