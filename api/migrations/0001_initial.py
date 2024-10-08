# Generated by Django 5.1.1 on 2024-09-15 17:19

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'meal',
                'verbose_name_plural': 'meals',
                'db_table': 'Meal',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_meal', to='api.meal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'rating',
                'verbose_name_plural': 'ratings',
                'db_table': 'Rating',
                'constraints': [models.UniqueConstraint(fields=('meal', 'user'), name='meal_user_unique')],
            },
        ),
    ]
