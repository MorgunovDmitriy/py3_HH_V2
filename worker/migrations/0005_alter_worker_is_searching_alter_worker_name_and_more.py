# Generated by Django 4.2.2 on 2023-06-30 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0004_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='is_searching',
            field=models.BooleanField(default=True, verbose_name='Ищет работу'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='name',
            field=models.CharField(max_length=100, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='specialization',
            field=models.CharField(max_length=255, verbose_name='Специальность'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='waiting_salary',
            field=models.IntegerField(blank=True, null=True, verbose_name='Ожидаемая зар плата'),
        ),
    ]
