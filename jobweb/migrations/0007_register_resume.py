# Generated by Django 4.1.2 on 2022-10-25 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobweb', '0006_rename_current_or_last_orginization_register_current_or_last_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='resume',
            field=models.FileField(default=None, max_length=500, null=True, upload_to=''),
        ),
    ]
