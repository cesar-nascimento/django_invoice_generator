# Generated by Django 3.2 on 2021-04-18 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100)),
                ('business_email', models.EmailField(max_length=254)),
                ('business_address', models.CharField(max_length=100)),
                ('client_name', models.CharField(max_length=100)),
                ('client_email', models.EmailField(max_length=254)),
                ('client_address', models.CharField(max_length=100)),
                ('invoice_number', models.CharField(max_length=100)),
                ('invoice_date', models.DateField()),
                ('invoice_due_date', models.DateField()),
                ('invoice_description', models.CharField(max_length=100)),
                ('invoice_logo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=1)),
                ('unit_price', models.FloatField(default=0)),
                ('details', models.TextField(max_length=300)),
            ],
        ),
    ]