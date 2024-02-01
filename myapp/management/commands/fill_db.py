import random

from django.core.management.base import BaseCommand
from myapp.models import User, Product

products = ['Стиральный порошок', 'Мыло', 'Гель для душа', 'Пена для бритья', 'Гель после бритья', 'Соль для ванны', 'Зубная щетка',
            'Зубная паста', 'Маска для лица', 'Духи', 'Одиколон', 'Тапочки', 'Носки', 'Джемпер', 'Куртка', 'Шапка',
            'Бейсболка', 'Джоггеры', 'Трусы', 'Телогрейка', 'Ботинки', 'Шаль', 'Вуаль', 'Крекеры', 'Печенье', 'Гречневая крупа',
            'Манная крупа', 'Макароны', 'Курица', 'Рыба', 'Груши', 'Яблоки', 'Бананы', 'Авокадо', 'Семечки']

user = ['Михайлов Дамир Фёдорович', 'Логинова Анна Константиновна', 'Тихонова Мария Глебовна', 'Овчинникова Ангелина Кирилловна',
        'Кудряшов Платон Максимович', 'Семенов Александр Михайлович', 'Сухарев Константин Тимурович', 'Мартынова Мария Дмитриевна',
        'Шестакова Виктория Всеволодовна', 'Кузин Роман Леонидович', 'Громова Лия Максимовна', 'Петров Давид Иванович',
        'Чернов Александр Дмитриевич', 'Маркова Екатерина Кирилловна']

city = ['Москва', 'Пермь', 'Самара', 'Нижний новогород', 'Куеда', 'Архангельск', 'Екатеринбург']

class Command(BaseCommand):
    help = "Generate fake User, Product"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of user')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            year = ''
            if len(str(i)) == 1:
                year = f'200{i}'
            elif len(str(i)) == 2:
                year = f'20{i}'
            create_user = User(name=user[random.randint(0, len(user)-1)],
                               email=f'mail_{i}@gmail.com',
                               phone=f'89{i}19{i}62485',
                               address=f'г.{city[random.randint(0, len(city)-1)]}, ул. Мира, д.{i}',
                               date_registry=f'{year}-01-01')
            create_user.save()
            create_product = Product(name=products[random.randint(0, len(products)-1)],
                                     price=f'13{i}.{i}69',
                                     description=f'{products[random.randint(0, len(products) - 1)]}, класса: {i}, лучшая покупка предлагать всем!',
                                     how_many=f'{i + 3}',
                                     date_create=f'{year}-01-01')
            create_product.save()