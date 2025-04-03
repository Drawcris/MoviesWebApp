# Generated by Django 5.1.7 on 2025-04-03 17:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoviesWeb', '0005_movie_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoreInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('running_time', models.PositiveSmallIntegerField(default=0)),
                ('genre', models.PositiveSmallIntegerField(choices=[(6, 'Fantasy'), (3, 'Horror'), (5, 'Akcja'), (4, 'Sci-Fi'), (1, 'Dramat'), (2, 'Komedia'), (0, 'Inne')], default=0)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='more_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MoviesWeb.moreinfo'),
        ),
    ]
