# Generated by Django 3.2 on 2021-04-28 02:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categoria',
        ),
        migrations.RenameModel(
            old_name='Post',
            new_name='Publicacao',
        ),
    ]