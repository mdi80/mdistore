# Generated by Django 4.0.6 on 2023-05-29 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productCategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.category'),
        ),
    ]