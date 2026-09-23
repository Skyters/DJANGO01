from django.db import models

# Create your models here.


class Booking(models.Model):
        date = models.DateField('Дата бронирования')
        start_time = models.TimeField('Время начала')
        end_time = models.TimeField('Время окончания')
        price = models.IntegerField('Общая стоимость')
        status = models.TextField('Статус брони')
        client = models.ForeignKey("Client", on_delete=models.CASCADE, null=True)
        lane = models.ForeignKey("Lane", on_delete=models.CASCADE, null=True)

        class Meta:
                verbose_name="Бронь"
                verbose_name_plural="Бронь"

        def __str__(self) -> str:
                return self.status
        
class Client(models.Model):
        name = models.TextField("ФИО")
        telephone=models.IntegerField("Телефон")
        Date_birth=models.DateField("Дата рождения")
        Loyalty_status=models.TextField("Статус лояльности")
        
        class Meta:
                verbose_name="Клиент"
                verbose_name_plural="Клиенты" 

        def __str__(self) -> str:
                return self.name

class Lane(models.Model):
        number = models.IntegerField('Номер дорожки')
        kind = models.TextField('Тип дорожки')
        status = models.TextField('Статус')
        price = models.IntegerField('Стоимость часа')

        class Meta:
                verbose_name = "Дорожка"
                verbose_name_plural = "Дорожки"

        def __str__(self) -> str:
                return str(self.number)

class Service(models.Model):
        name = models.TextField('Название')
        сategory = models.TextField('Категория')
        price = models.IntegerField('Стоимость')
        unit_measurement = models.TextField('Единица измерения')

        class Meta:
                verbose_name = "Услуга"
                verbose_name_plural = "Услуги"

        def __str__(self) -> str:
                return self.name

class BookinAndService(models.Model):
        quantity = models.IntegerField('Количество')
        price_moment_order = models.IntegerField('Цена_на_момент_заказа')
        sum = models.IntegerField('Сумма') #Кол-во * цена
        booking = models.ForeignKey("Booking", on_delete=models.CASCADE, null=True)
        service = models.ForeignKey("Service", on_delete=models.CASCADE, null=True)

        class Meta:
                verbose_name="Услуга в бронировании"
                verbose_name_plural="Услуги в бронировании"
