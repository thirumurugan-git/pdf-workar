# Generated by Django 3.1.5 on 2021-02-20 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdfupload', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='path',
        ),
    ]
