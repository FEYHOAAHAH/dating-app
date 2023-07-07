from django.db import models


# Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()

    STATUS = (
        ('st', 'Учусь'),
        ('wk', 'Работаю'),
        ('sd', 'Туплю'),
        ('md', 'Мамкин миллиардер'),
        ('rf', 'Ищу мамика'),
    )

    status = models.CharField(max_length=50, choices=STATUS)
    description = models.TextField(null=True)
    salary = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.name} {self.surname} {self.age} лет" \
               f"{self.description}" \
               f"{self.salary} $ в месяц"

    def get_absolute_url(self):
        return f"/{self.pk}"


