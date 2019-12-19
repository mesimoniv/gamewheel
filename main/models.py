from django.db import models
from django.contrib.auth.models import User

class Animation(models.Model):
    name = models.CharField(max_length=200, default='spinToStop') # animation type,
    duration = models.IntegerField(default=10)
    spins = models.IntegerField(default=3)

    def __str__(self):
      return self.name


class Wheel(models.Model):
    name = models.CharField(max_length=100, default='Wheel of Fun')
    description = models.CharField(max_length=400)
    showDescription = models.BooleanField(default=False)
    numSegments = models.IntegerField(default=6, verbose_name='number of prizes', help_text='number of prizes on game wheel')
    innerRadius = models.IntegerField(default=0, verbose_name='inside radius', help_text='inside radius for donut wheel')
    outerRadius = models.IntegerField(default=200)
    fillStyle = models.CharField(max_length=200, default='text', help_text='image or text')
    textFontFamily = models.CharField(max_length=200, default='Verdana', verbose_name='font family')
    textFontSize = models.IntegerField(default=24, verbose_name='font size')
    textOrientation = models.CharField(max_length=10, default='vertical', help_text='vertical or horizontal')
    textAlignment = models.CharField(max_length=50, default='outer')
    animation = models.ForeignKey(Animation, null=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, unique=False, default=1, on_delete=models.CASCADE)

    def __str__(self):
      return self.name


class Segment(models.Model):
    wheel = models.ForeignKey(Wheel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='prize', verbose_name='prize name')
    description = models.CharField(max_length=400, default="You have won")
    fillStyle = models.CharField(max_length=7, verbose_name='background color', help_text='background color for prize on wheel') # store hexadecimal color code including #
    textFillStyle = models.CharField(max_length=7, verbose_name='text color') # hexadecimal text color
    textFontSize = models.IntegerField(default=12, verbose_name='font size', help_text='prize text size on wheel')

    def __str__(self):
      return self.name
