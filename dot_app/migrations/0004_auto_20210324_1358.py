# Generated by Django 3.1.7 on 2021-03-24 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dot_app', '0003_auto_20210324_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.CharField(max_length=3, primary_key=True, serialize=False),
        ),
    ]
