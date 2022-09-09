# Generated by Django 4.1 on 2022-09-09 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('number_of_tables', models.IntegerField(default=1)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=255, null=True)),
                ('gstn', models.CharField(max_length=100, null=True)),
                ('pan', models.CharField(max_length=100, null=True)),
                ('instagram', models.CharField(max_length=100, null=True)),
                ('facebook', models.CharField(max_length=100, null=True)),
                ('website', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='TaxSlab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_slab', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='category', to='restapp.productcategory')),
                ('slab', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='slab', to='restapp.taxslab')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.UUIDField(auto_created=True, primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restapp.product')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapp.restaurantprofile')),
            ],
        ),
    ]
