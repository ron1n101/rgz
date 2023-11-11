# Generated by Django 4.2.7 on 2023-11-11 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_cart_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=128)),
                ('image', models.ImageField(upload_to='blog/cart_shots')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.cart', verbose_name='Карточка')),
            ],
            options={
                'verbose_name': 'Зображення з карточки',
                'verbose_name_plural': 'Зображення з карток',
            },
        ),
    ]
