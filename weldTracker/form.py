from django import forms
from . models import WeldNumber, Dpl


class DplForm(forms.ModelForm):
    class Meta:
        model = Dpl
        fields = ('dpl_number', 'pipe_size', 'wall_size')


class WeldNumberForm(forms.ModelForm):
    class Meta:
        model = WeldNumber
        fields = ('qc_person', 'dpl', 'weld_number', 'xray_status', 'status')