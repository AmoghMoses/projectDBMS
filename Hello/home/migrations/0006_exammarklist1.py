# Generated by Django 4.0.4 on 2022-04-26 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_delete_exammarklist1'),
    ]

    operations = [
        migrations.CreateModel(
            name='exammarklist1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examid', models.CharField(max_length=20)),
                ('marks', models.IntegerField()),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.student3')),
            ],
            options={
                'unique_together': {('studentid', 'examid')},
            },
        ),
    ]
