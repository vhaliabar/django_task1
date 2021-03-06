# Generated by Django 3.1.1 on 2022-07-14 08:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feeditem',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='feeditem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
