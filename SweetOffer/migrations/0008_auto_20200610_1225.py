# Generated by Django 3.0.3 on 2020-06-10 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SweetOffer', '0007_auto_20200610_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='img'),
        ),
    ]