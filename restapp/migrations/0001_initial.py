# Generated by Django 4.1 on 2022-09-03 06:44

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
                ('name', models.CharField(blank=True, max_length=100, primary_key=True, serialize=False)),
                ('number_of_tables', models.IntegerField(default=1)),
                ('contact', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('gstn', models.CharField(max_length=100, null=True)),
                ('pan', models.CharField(max_length=100, null=True)),
                ('instagram', models.CharField(max_length=100, null=True)),
                ('facebook', models.CharField(max_length=100, null=True)),
                ('website', models.CharField(max_length=100, null=True)),
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
    ]
