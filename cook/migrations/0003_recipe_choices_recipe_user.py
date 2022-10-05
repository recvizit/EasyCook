# Generated by Django 4.1.1 on 2022-09-21 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cook', '0002_alter_recipe_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='choices',
            field=models.ManyToManyField(to='cook.ingredient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]