# Generated by Django 4.2.7 on 2023-11-14 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(default='gmail', max_length=70),
        ),
        migrations.AddField(
            model_name='student',
            name='genero',
            field=models.CharField(default='neutre', max_length=10),
        ),
        migrations.AddField(
            model_name='student',
            name='idade',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AddField(
            model_name='student',
            name='matricula',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='turma',
            field=models.CharField(default='0', max_length=50),
        ),
    ]
