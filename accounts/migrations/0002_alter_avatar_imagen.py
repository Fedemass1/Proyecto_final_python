# Generated by Django 5.0 on 2023-12-10 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, default='media/avatares/Captura_de_pantalla_2023-06-26_213713.png', null=True, upload_to='avatares'),
        ),
    ]