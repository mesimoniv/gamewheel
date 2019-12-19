from django.core.management.base import BaseCommand
from main.models import Wheel, Segment

class Command(BaseCommand):
    def handle(self, *args, **options):
        Wheel.objects.all().delete()
        Segment.objects.all().delete()