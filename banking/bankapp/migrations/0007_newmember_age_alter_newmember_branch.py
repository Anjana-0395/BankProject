# Generated by Django 4.2.6 on 2023-11-12 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0006_alter_newmember_materials'),
    ]

    operations = [
        migrations.AddField(
            model_name='newmember',
            name='age',
            field=models.CharField(default=28, max_length=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newmember',
            name='branch',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bankapp.branch'),
        ),
    ]
