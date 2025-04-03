# Generated by Django 5.1.7 on 2025-04-03 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoviesWeb', '0008_alter_moreinfo_genre_cast'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cast',
            name='character',
        ),
        migrations.AlterField(
            model_name='moreinfo',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Sci-Fi'), (2, 'Komedia'), (6, 'Fantasy'), (3, 'Horror'), (0, 'Inne'), (5, 'Akcja'), (1, 'Dramat')], default=0),
        ),
    ]
