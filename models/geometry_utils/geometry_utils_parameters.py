"""
HMS Geometry Input form

"""

from django import forms


class GeometryUtilsFormInput(forms.Form):
    geojson = forms.CharField(
        label='GeoJSON String',
        required=True
    )


