"""
HMS Water Quality submodule Input form parameters
"""

from django import forms

WQ_OPTIONS = (
('nldas', 'nldas'), ('ncei', 'ncei'), ('nwm', 'nwm'))


class WaterQualityFormInput(forms.Form):
    source = forms.ChoiceField(
        widget=forms.Select(attrs={
            'title': 'Data source of the dataset.'
        }),
        label='Source',
        choices=WQ_OPTIONS,
        initial='NLDAS'
    )
