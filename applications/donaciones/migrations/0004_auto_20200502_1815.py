# Generated by Django 3.0.3 on 2020-05-02 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donaciones', '0003_auto_20200502_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donacion',
            old_name='usuario_donador',
            new_name='user',
        ),
    ]
