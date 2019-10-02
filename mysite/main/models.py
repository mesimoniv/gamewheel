from django.db import models

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
    numSegments = models.IntegerField(default=6)
    innerRadius = models.IntegerField(default=25)
    outerRadius = models.IntegerField(default=125)
    fillStyle = models.CharField(max_length=200, default='text')
    textFontFamily = models.CharField(max_length=200, default='Verdana')
    textFontSize = models.IntegerField(default=24)
    textOrientation = models.CharField(max_length=10, default='vertical') # vertical, horizontal
    textAlignment = models.CharField(max_length=50, default='outer')
    animation = models.ForeignKey(Animation, null=True, on_delete=models.SET_NULL)

    def __str__(self):
      return self.name


class Segment(models.Model):
    wheel = models.ForeignKey(Wheel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400, default="You have won")
    fillStyle = models.CharField(max_length=7) # store hexadecimal color code including #
    textFillStyle = models.CharField(max_length=7) # hexadecimal text color
    textFontSize = models.IntegerField(default=12)

    def __str__(self):
      return self.name
