# Generated by Django 3.0.3 on 2020-05-04 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donaciones', '0004_auto_20200502_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donacion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_donador', to=settings.AUTH_USER_MODEL),
        ),
    ]
