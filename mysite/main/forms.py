from django import forms
from .models import Wheel, Segment

class WheelForm(forms.ModelForm):
    name = forms.CharField(label='Game name', max_length=100)
    description = forms.CharField(label='Description', max_length=400)
    numSegments = forms.IntegerField(label='Number of Prizes', min_value=1, max_value=99)
    innerRadius = forms.IntegerField(label='Inside Radius', min_value=0, max_value=100)
    outerRadius = forms.IntegerField(label='Outside Radius', min_value=10, max_value=249)

    class Meta:
      model = Wheel
      fields = ('name', 'description','numSegments','innerRadius','outerRadius',)

class SegmentForm(forms.ModelForm):
    class Meta:
      model = Segment
      exclude = ['wheel']