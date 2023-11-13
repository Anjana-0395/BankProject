# Generated by Django 4.2.6 on 2023-11-07 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0003_newmember_materials_alter_newmember_account_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newmember',
            name='materials',
            field=models.CharField(choices=[('cheque', 'Cheque Book'), ('credit', 'Credit Card'), ('debit', 'Debit Card')], default=None, max_length=100),
        ),
    ]
