from django.db import models


class Agent(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=64)

    def __str__(self):
        return f'Имя Фамилия: {self.name} {self.surname} | Телефон: {self.phone_number}'


class Client(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=64)

    def __str__(self):
        return f'Имя Фамилия: {self.name} {self.surname} | Телефон: {self.phone_number}'


class Property(models.Model):
    property_type = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    rooms = models.IntegerField()
    area = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f'Тип:{self.property_type} | Адрес: {self.address} | Цена: {self.price}'


class Deal(models.Model):
    agent_id = models.ForeignKey(to=Agent, on_delete=models.CASCADE)
    client_id = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    property_id = models.ForeignKey(to=Property, on_delete=models.CASCADE)
    deal_date = models.DateField()
    deal_amount = models.IntegerField()
    status = models.CharField(max_length=32, default="Завершен")

    def __str__(self):
        return f'Сделка Агента:{self.agent_id} | Клиент:{self.client_id} | Недвижимость: {self.property_id} | Дата ' \
               f'сделки : {self.deal_date} | Сумма сделки : {self.deal_amount} | Статус - {self.status}'


class Status_deal(models.Model):
    status = models.CharField(max_length=32)

    def __str__(self):
        return self.status
