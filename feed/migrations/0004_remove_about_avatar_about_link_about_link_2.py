# Generated by Django 4.1.2 on 2022-10-26 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_alter_experience_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='avatar',
        ),
        migrations.AddField(
            model_name='about',
            name='link',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='about',
            name='link_2',
            field=models.URLField(default=''),
        ),
    ]