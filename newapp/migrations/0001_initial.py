# Generated by Django 4.1.3 on 2023-08-02 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('correct_answer', models.CharField(choices=[('option1', 'Option One'), ('option2', 'Option Two'), ('option3', 'Option Three'), ('option4', 'Option Four')], max_length=8)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.category')),
            ],
        ),
    ]
