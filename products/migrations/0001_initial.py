# Generated by Django 4.0.4 on 2022-05-18 13:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
