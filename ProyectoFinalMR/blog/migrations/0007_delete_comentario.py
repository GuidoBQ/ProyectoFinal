# Generated by Django 4.2.2 on 2023-07-15 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comentario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]