from django.db import models

# Create your models here.
class Regis_stu(models.Model):
    stu_name=models.CharField(max_length=90)
    mobile=models.BigIntegerField(unique=True)
    age=models.IntegerField()
    address=models.CharField(max_length=90)
    course=models.CharField(max_length=10)
    fees=models.IntegerField()
    paid_fees=models.IntegerField()
    trainer_name=models.CharField(max_length=20)


class Enq(models.Model):
    first_name=models.CharField(max_length=30)
    mobile=models.BigIntegerField()
    course=models.CharField(max_length=40)
    fees=models.IntegerField()


class PendingFee(models.Model):
    stu_name = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    course = models.CharField(max_length=40)
    fees = models.IntegerField()
    pendingfee = models.IntegerField()
    trainer_name = models.CharField(max_length=40)
    paid_fees = models.IntegerField()
