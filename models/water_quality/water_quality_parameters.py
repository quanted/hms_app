"""
HMS Water Quality Submodule Input form parameters
"""
import json
from django import forms

json_input_initial = {"input": {
    "contaminant name": "Methoxyclor",
    "contaminant type": "Chemical",
    "water type name": "Pure Water",
    "min wavelength": 297.5,
    "max wavelength": 330,
    "longitude": "83.2",
    "latitude(s)": [
      40,
      -99,
      -99,
      -99,
      -99,
      -99,
      -99,
      -99,
      -99,
      -99
    ],
    "season(s)": [
      "Spring",
      "  ",
      "  ",
      "  "
    ],
    "atmospheric ozone layer": 0.3,
    "initial depth (cm)": "0.001",
    "final depth (cm)": "5",
    "depth increment (cm)": "10",
    "quantum yield": "0.32",
    "refractive index": "1.34",
    "elevation": "0",
    "wavelength table": {
      "297.50": {
        "water attenuation coefficients (m**-1)": "0.069000",
        "chemical absorption coefficients (L/(mole cm))": "11.100000"
      },
      "300.00": {
        "water attenuation coefficients (m**-1)": "0.061000",
        "chemical absorption coefficients (L/(mole cm))": "4.6700000"
      },
      "302.50": {
        "water attenuation coefficients (m**-1)": "0.057000",
        "chemical absorption coefficients (L/(mole cm))": "1.900000"
      },
      "305.00": {
        "water attenuation coefficients (m**-1)": "0.053000",
        "chemical absorption coefficients (L/(mole cm))": "1.100000"
      },
      "307.50": {
        "water attenuation coefficients (m**-1)": "0.049000",
        "chemical absorption coefficients (L/(mole cm))": "0.800000"
      },
      "310.00": {
        "water attenuation coefficients (m**-1)": "0.045000",
        "chemical absorption coefficients (L/(mole cm))": "0.5300000"
      },
      "312.50": {
        "water attenuation coefficients (m**-1)": "0.043000",
        "chemical absorption coefficients (L/(mole cm))": "0.330000"
      },
      "315.00": {
        "water attenuation coefficients (m**-1)": "0.041000",
        "chemical absorption coefficients (L/(mole cm))": "0.270000"
      },
      "317.50": {
        "water attenuation coefficients (m**-1)": "0.039000",
        "chemical absorption coefficients (L/(mole cm))": "0.1600000"
      },
      "320.00": {
        "water attenuation coefficients (m**-1)": "0.037000",
        "chemical absorption coefficients (L/(mole cm))": "0.100000"
      },
      "323.10": {
        "water attenuation coefficients (m**-1)": "0.035000",
        "chemical absorption coefficients (L/(mole cm))": "0.060000"
      },
      "330.00": {
        "water attenuation coefficients (m**-1)": "0.029000",
        "chemical absorption coefficients (L/(mole cm))": "0.020000"
      }
    }
  }}


class DegreeMinuteSecondWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = [
            forms.TextInput(attrs={'class': 'ephemeride_0 deg_min_sec', 'title': 'Degrees'}),
            forms.TextInput(attrs={'class': 'ephemeride_0 deg_min_sec', 'title': 'Minutes'}),
            forms.TextInput(attrs={'class': 'ephemeride_0 deg_min_sec', 'title': 'Seconds'}),
        ]
        super(DegreeMinuteSecondWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split(' ')
        return [None, None, None]


class DegreeMinuteSecond(forms.MultiValueField, ):
    widget = DegreeMinuteSecondWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.CharField(required=False),
            forms.CharField(required=False),
            forms.CharField(required=False),
        )
        super(DegreeMinuteSecond, self).__init__(fields, require_all_fields=False, *args, **kwargs)

    def compress(self, data_list):
        return ' '.join(data_list)


class PhotolysisFormInput(forms.Form):
    # Contaminant Information
    contaminant_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Methoxyclor'}),
        label="Contaminant Name",
        # initial="Methoxyclor",
        required=False
    )
    contaminant_type = forms.TypedChoiceField(
        widget=forms.Select(),
        label="Contaminant Type",
        choices=(("chemical", "Chemical"), ("biological", "Biological")),
        required=False
    )
    wavelength_table = forms.CharField(
        widget=forms.HiddenInput(),
        label="Wavelength Coefficients",
        required=False
    )

    # Ephemeride Information
    typical_ephemeride_values = forms.ChoiceField(
        # widget=forms.RadioSelect(),
        choices=(("yes", "Yes"), ("no", "No")),
        label="Typical Ephemeride Values",
        # initial="Yes",
        required=False
    )
    longitude = forms.CharField(
        widget=forms.TextInput(attrs={'class': ['ephemeride_0', 'ephemeride_1'], 'placeholder': 83.2}),
        label="Longitude",
        # initial=83.2,
        required=False
    )
    latitude = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'ephemeride_0', 'placeholder': 40}),
        label="Latitude",
        # initial=40,
        required=False
    )
    no_latitude = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'ephemeride_1', 'placeholder': 1}),
        label="Number of Latitudes",
        # initial=1,
        required=False
    )
    list_latitude = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'ephemeride_1', 'placeholder': 40}),
        label="Latitudes",
        required=False
    )
    seasons = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'ephemeride_1'}),
        label="Seasons",
        choices=(("spring", "Spring"), ("summer", "Summer"), ("fall", "Fall"), ("winter", "Winter")),
        initial="spring",
        required=False
    )
    ozone_layer = forms.CharField(
        widget=forms.TextInput(attrs={'class': ['ephemeride_0', 'ephemeride_1'], 'placeholder': 0.003}),
        label="Ozone Layer Depth",
        # initial=0.003,
        required=False
    )
    solar_declination = DegreeMinuteSecond(label="Solar Declination")
    print(solar_declination.widget)
    right_ascension = DegreeMinuteSecond(label="Right Ascension")
    sidereal_time = DegreeMinuteSecond(label="Sidereal Time")

    # Depth Related Parameters
    initial_depth = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 0.001}),
        label="Initial Depth (cm)",
        # initial=0.001,
        required=False
    )
    final_depth = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 5}),
        label="Final Depth (cm)",
        # initial=5,
        required=False
    )
    depth_increment = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 10}),
        label="Depth Increment (cm)",
        # initial=10,
        required=False
    )
    depth_point = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 0.001}),
        label="Depth Point(cm)",
        # initial=0.001,
        required=False
    )

    # miscellaneous parameters
    quantum_yield = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 0.32}),
        label="Quantum Yield of Contaminant",
        # initial=0.32,
        required=False,
    )
    refractive_index = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 1.34}),
        label="Refractive Index of Water",
        # initial=1.34,
        required=False,
    )
    elevation = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 0.0}),
        label="Elevation (km)",
        # initial=0.0,
        required=False
    )
    json_input = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'json_input_data'}),
        label="Json Input",
        initial=json.dumps(json_input_initial),
        required=False
    )
