# Generated by Django 3.0.3 on 2020-06-18 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SweetOffer', '0010_auto_20200612_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100)),
            ],
        ),
    ]
