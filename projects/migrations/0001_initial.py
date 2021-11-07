# Generated by Django 3.2.8 on 2021-10-30 22:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('demo_link', models.CharField(max_length=200)),
                ('source_link', models.CharField(max_length=200)),
                ('vote_total', models.IntegerField(default=0)),
                ('vote_rati0', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
