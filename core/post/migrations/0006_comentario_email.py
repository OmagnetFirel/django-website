# Generated by Django 3.2 on 2021-05-19 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='email',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
