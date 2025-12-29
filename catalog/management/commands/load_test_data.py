from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Очистка базы и загрузка тестовых данных из фикстур'

    def handle(self, *args, **kwargs):
        # Удаляем все существующие данные
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Загружаем фикстуры
        call_command('loaddata', 'catalog/fixtures/categories.json')
        call_command('loaddata', 'catalog/fixtures/products.json')

        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно загружены из фикстур'))