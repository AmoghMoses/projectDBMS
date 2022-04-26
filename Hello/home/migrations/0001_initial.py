# Generated by Django 4.0.4 on 2022-04-26 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin1',
            fields=[
                ('adminemail', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('adminfirstname', models.CharField(max_length=255)),
                ('adminlastname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='admin2',
            fields=[
                ('adminid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('adminemail', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('desc1', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='exammarklist2',
            fields=[
                ('examid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('examdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='student1',
            fields=[
                ('studentphone', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('studentfirstname', models.CharField(max_length=255)),
                ('studentlastname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='student2',
            fields=[
                ('studentemail', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('studentphone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='student3',
            fields=[
                ('studentid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('studentdob', models.DateField()),
                ('studentemail', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='examinationtype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examid', models.CharField(max_length=20)),
                ('studentdate', models.CharField(max_length=50)),
            ],
            options={
                'unique_together': {('examid', 'studentdate')},
            },
        ),
        migrations.CreateModel(
            name='student4',
            fields=[
                ('studentid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('adminid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.admin2')),
            ],
            options={
                'unique_together': {('studentid', 'adminid')},
            },
        ),
        migrations.CreateModel(
            name='exammarklist3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examid', models.CharField(max_length=20)),
                ('adminid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.admin2')),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.student3')),
            ],
            options={
                'unique_together': {('studentid', 'examid', 'adminid')},
            },
        ),
        migrations.CreateModel(
            name='exammarklist1',
            fields=[
                ('examid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('marks', models.IntegerField()),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.student3')),
            ],
            options={
                'unique_together': {('studentid', 'examid')},
            },
        ),
        migrations.CreateModel(
            name='attempts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attemptnumber', models.IntegerField()),
                ('examid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.exammarklist2')),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.student3')),
            ],
            options={
                'unique_together': {('studentid', 'examid')},
            },
        ),
        migrations.CreateModel(
            name='adminmobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminmobile', models.CharField(max_length=20)),
                ('adminid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.admin2')),
            ],
            options={
                'unique_together': {('adminid', 'adminmobile')},
            },
        ),
        migrations.CreateModel(
            name='adminidpassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminpassword', models.CharField(max_length=255)),
                ('adminid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.admin2')),
            ],
            options={
                'unique_together': {('adminid', 'adminpassword')},
            },
        ),
    ]
