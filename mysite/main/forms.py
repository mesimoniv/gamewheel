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
      fields = ('name','fillStyle',)


class SegmentFormCustom(forms.ModelForm):
    wheel = forms.ModelChoiceField(queryset=Wheel.objects.all())
    name = forms.CharField(label='Prize', max_length=200)
    fillStyle = forms.CharField(label='Color', max_length=7) # store hexadecimal color code including #
    textFillStyle = forms.CharField(label='Text color', max_length=7) # hexadecimal text color
    textFontSize = forms.IntegerField(label='Text size', min_value=6, max_value=36)

    class Meta:
      model = Segment
      fields = ('name','fillStyle','textFillStyle','textFontSize',)