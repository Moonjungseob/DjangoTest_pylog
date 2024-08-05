from django.db import models

# Create your models here.
class LunchMenu(models.Model):
    # name , 필드, 데이터 타입으로 문자열 , 길이 100자
    name = models.CharField(max_length=100)
    # price , 가격 , 데이터 타입 정수로 , 기본값 0
    price = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)

    # 해당 인스턴스를 출력시 나타나는 이름.
    def __str__(self):
        return self.name