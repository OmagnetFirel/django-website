# Generated by Django 3.2 on 2021-04-28 16:32

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_publicacao_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacao',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
