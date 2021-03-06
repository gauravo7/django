# Generated by Django 3.0.6 on 2020-08-18 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_category_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=200)),
                ('pprice', models.IntegerField()),
                ('brand', models.CharField(max_length=200)),
                ('attr1', models.CharField(max_length=200)),
                ('value1', models.CharField(max_length=200)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Category')),
                ('scid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Subcategory')),
            ],
        ),
    ]
