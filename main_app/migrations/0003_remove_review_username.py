# Generated by Django 4.2.11 on 2024-05-02 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_review_barber_id_review_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='username',
        ),
    ]
