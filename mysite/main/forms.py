from django import forms
from .models import Wheel, Segment

class WheelForm(forms.ModelForm):
    numSegments = forms.IntegerField(label='Number of Prizes', min_value=1, max_value=99)
    innerRadius = forms.IntegerField(label='Inside Radius', min_value=0, max_value=100)

    class Meta:
      model = Wheel
      fields = ('name', 'description','numSegments','innerRadius',)

class SegmentForm(forms.ModelForm):
    class Meta:
      model = Segment
      exclude = ['wheel']