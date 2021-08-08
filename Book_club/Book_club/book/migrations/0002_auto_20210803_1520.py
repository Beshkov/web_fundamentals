# Generated by Django 3.2.5 on 2021-08-03 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='private',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='mark',
            field=models.CharField(choices=[('1', 'dislike'), ('2', 'did not like'), ('3', 'neutral'), ('4', 'liked'), ('5', 'loved it')], max_length=1),
        ),
    ]
