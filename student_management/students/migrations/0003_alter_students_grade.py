# Generated by Django 3.2.10 on 2021-12-09 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20211209_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='students.grade'),
        ),
    ]
