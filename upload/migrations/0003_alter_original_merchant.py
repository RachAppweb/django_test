# Generated by Django 3.2 on 2023-08-24 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_alter_original_trans_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='original',
            name='merchant',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
