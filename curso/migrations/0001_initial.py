# Generated by Django 2.1.7 on 2019-12-07 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
                ('text', models.CharField(max_length=100)),
            ],
            options={
                'permissions': [('publish_article', 'can publish Articles.')],
            },
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('birth_date', models.DateField(verbose_name='Birth Date')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF Number')),
            ],
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('numkber', models.CharField(max_length=100, verbose_name='Passport Number')),
                ('issue_date', models.DateField(verbose_name='Issue Date')),
                ('expiration_date', models.DateField(verbose_name='Expiration Date')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='curso.Person')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='magazines',
            field=models.ManyToManyField(to='curso.Magazine'),
        ),
        migrations.AddField(
            model_name='article',
            name='reporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curso.Reporter'),
        ),
    ]
