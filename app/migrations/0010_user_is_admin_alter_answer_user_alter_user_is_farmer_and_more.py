# Generated by Django 4.0.5 on 2022-06-23 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_answer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Is admin'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_farmer',
            field=models.BooleanField(default=False, verbose_name='Is farmer'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_officer',
            field=models.BooleanField(default=False, verbose_name='Is officer'),
        ),
    ]