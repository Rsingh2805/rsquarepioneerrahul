# Generated by Django 2.2.7 on 2019-12-15 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20191215_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singlebusexpense',
            name='expense',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='single_expenses', to='website.DayExpense'),
        ),
    ]
