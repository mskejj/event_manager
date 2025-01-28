from django.core.management.base import BaseCommand
from events.models import Event, Category

class Command(BaseCommand):
    help = 'Fixes invalid category values in Event model'

    def handle(self, *args, **kwargs):
        default_category, created = Category.objects.get_or_create(name='Domyślna kategoria', defaults={'description': 'Default category'})
        for event in Event.objects.all():
            if isinstance(event.category, str):
                event.category = default_category
                event.save()
        self.stdout.write(self.style.SUCCESS('Successfully fixed event categories'))