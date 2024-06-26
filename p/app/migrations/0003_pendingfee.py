# Generated by Django 5.0.3 on 2024-03-19 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_enq'),
    ]

    operations = [
        migrations.CreateModel(
            name='PendingFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('course', models.CharField(max_length=40)),
                ('fees', models.IntegerField()),
                ('pendingfee', models.IntegerField()),
                ('trainer_name', models.CharField(max_length=40)),
                ('first_installment', models.IntegerField()),
            ],
        ),
    ]
