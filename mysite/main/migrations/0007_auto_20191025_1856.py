# Generated by Django 2.2.5 on 2019-10-25 18:56

from django.db import migrations
from main.models import Wheel, Segment

def create_wof():
    wheel = Wheel.objects.create(name='Wheel of Fortune',
            description='Customize this Wheel of Fortune inspired game to your own',
            showDescription=True,
            numSegments=24,
            innerRadius=75,
            outerRadius=212)

# create 24 segments
    Segment.objects.create(wheel=Wheel.objects.get(pk=wheel.pk),
                        name="300",
                        fillStyle="#ee1c24",
                        textFillStyle="#000000",
                        textFontSize="24")
    Segment.objects.create(wheel=Wheel.objects.get(pk=wheel.pk),
                        name="450",
                        fillStyle="#3cb878",
                        textFillStyle="#000000",
                        textFontSize="25")

# Minute to win it definition
def create_minwin():
    wheel = Wheel.objects.create(name='Minute to Win It',
            description='Spin the wheel to find out what game you are playing',
            showDescription=True,
            numSegments=12,
            innerRadius=75,
            outerRadius=212)

    Segment.objects.create(wheel=Wheel.objects.get(pk=wheel.pk),
                        name="NUTSTACKER",
                        fillStyle="#C72833",
                        textFillStyle="#000000",
                        textFontSize="16")

    Segment.objects.create(wheel=Wheel.objects.get(pk=wheel.pk),
                        name="JUNK IN THE TRUNK",
                        fillStyle="#FFFC96",
                        textFillStyle="#000000",
                        textFontSize="16")

    Segment.objects.create(wheel=Wheel.objects.get(pk=wheel.pk),
                        name="THIS BLOWS",
                        fillStyle="#50A0CC",
                        textFillStyle="#000000",
                        textFontSize="16")

    Segment.objects.create(wheel=Wheel.objects.get(pk=wheel.pk),
                        name="DEFY GRAVITY",
                        fillStyle="#39CC51",
                        textFillStyle="#000000",
                        textFontSize="16")

    Segment.objects.create(wheel=Wheel.objects.get(pk=wheel.pk),
                        name="MOVIN ON UP",
                        fillStyle="#C72833",
                        textFillStyle="#000000",
                        textFontSize="16")

    Segment.objects.create(wheel=Wheel.objects.get(pk=wheel.pk),
                        name="STACK ATTACK",
                        fillStyle="#FFFC96",
                        textFillStyle="#000000",
                        textFontSize="16")

    Segment.objects.create(wheel=Wheel.objects.get(pk=wheel.pk),
                        name="SUCK IT UP",
                        fillStyle="#50A0CC",
                        textFillStyle="#000000",
                        textFontSize="16")

    Segment.objects.create(wheel=Wheel.objects.get(pk=wheel.pk),
                        name="COOKIE FACE",
                        fillStyle="#39CC51",
                        textFillStyle="#000000",
                        textFontSize="16")

    Segment.objects.create(wheel=Wheel.objects.get(pk=wheel.pk),
                        name="CHANDELIER",
                        fillStyle="#C72833",
                        textFillStyle="#000000",
                        textFontSize="16")

    Segment.objects.create(wheel=Wheel.objects.get(pk=wheel.pk),
                        name="PENNY HOSE",
                        fillStyle="#FFFC96",
                        textFillStyle="#000000",
                        textFontSize="16")

    Segment.objects.create(wheel=Wheel.objects.get(pk=wheel.pk),
                        name="ON THE HOOK",
                        fillStyle="#50A0CC",
                        textFillStyle="#000000",
                        textFontSize="16")

    Segment.objects.create(wheel=Wheel.objects.get(pk=wheel.pk),
                        name="MAD DOG",
                        fillStyle="#39CC51",
                        textFillStyle="#000000",
                        textFontSize="16")

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20191010_1818'),
    ]

    operations = [
    migrations.RunPython(create_wof),
    ]
