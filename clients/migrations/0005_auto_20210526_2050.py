# Generated by Django 2.2.14 on 2021-05-26 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_remove_client_reference_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='fillup_onsite',
        ),
        migrations.AlterField(
            model_name='client',
            name='age',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='civil_status',
            field=models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed'), ('Annulled', 'Annulled'), ('Legally Separated', 'Legally Separated')], default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='middle_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='nationality',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
