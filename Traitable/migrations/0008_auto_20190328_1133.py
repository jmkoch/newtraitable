# Generated by Django 2.1.7 on 2019-03-28 16:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Traitable', '0007_auto_20190328_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='pub',
            name='firstName',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Error: only alphabetic characters are allowed.')]),
        ),
        migrations.AddField(
            model_name='pub',
            name='lastName',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Error: only alphabetic characters are allowed.')]),
        ),
        migrations.AddField(
            model_name='pub',
            name='middleName',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Error: only alphabetic characters are allowed.')]),
        ),
        migrations.AddField(
            model_name='pub',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pub',
            name='citekey',
            field=models.CharField(max_length=50, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Error: only alphanumeric characters are allowed.')]),
        ),
    ]
