# Generated by Django 5.0.7 on 2024-07-19 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resenias', '0007_alter_project_imagen_1_alter_project_imagen_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='imagen_1',
            field=models.ImageField(upload_to='media', verbose_name='imagen 1'),
        ),
        migrations.AlterField(
            model_name='project',
            name='imagen_2',
            field=models.ImageField(upload_to='media', verbose_name='imagen 2'),
        ),
        migrations.AlterField(
            model_name='project',
            name='imagen_caratula',
            field=models.ImageField(upload_to='media', verbose_name='imagen de la caratula'),
        ),
    ]
