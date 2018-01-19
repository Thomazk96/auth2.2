# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('date_ini', models.DateField()),
                ('date_term', models.DateField()),
                ('observations', models.TextField()),
            ],
            options={
                'verbose_name': 'Atividade',
                'verbose_name_plural': 'Atividades',
            },
        ),
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('wk_week', models.IntegerField()),
                ('wk_limit', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Tipo de Atividade',
                'verbose_name_plural': 'Tipos de Atividade',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '\xc1rea',
                'verbose_name_plural': '\xc1reas',
            },
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('short_name', models.CharField(max_length=30)),
                ('add_street', models.CharField(max_length=50)),
                ('add_no', models.IntegerField()),
                ('add_neighbor', models.CharField(max_length=50)),
                ('add_city', models.CharField(max_length=50)),
                ('add_uf', models.CharField(max_length=2)),
                ('add_zip', models.CharField(max_length=50)),
                ('phone1', models.CharField(max_length=14)),
                ('phone2', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('site', models.URLField()),
                ('active', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Campus',
                'verbose_name_plural': 'Campi',
            },
        ),
        migrations.CreateModel(
            name='ContractType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('wk_teaching', models.IntegerField()),
                ('wk_resext', models.IntegerField()),
                ('wk_compl', models.IntegerField()),
                ('active', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Tipo de Contrato',
                'verbose_name_plural': 'Tipos de Contrato',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('short_name', models.CharField(max_length=20)),
                ('active', models.BooleanField()),
                ('campus', models.ForeignKey(to='core.Campus')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='CourseGrid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('date_ini', models.DateField(null=True)),
                ('date_term', models.DateField(null=True)),
                ('active', models.BooleanField()),
                ('course', models.ForeignKey(to='core.Course')),
            ],
            options={
                'verbose_name': 'Matriz',
                'verbose_name_plural': 'Matrizes',
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('short_name', models.CharField(max_length=20)),
                ('ementa', models.TextField()),
                ('block', models.SmallIntegerField()),
                ('work_load', models.SmallIntegerField()),
                ('area', models.ForeignKey(to='core.Area')),
                ('grid', models.ForeignKey(to='core.CourseGrid')),
            ],
            options={
                'verbose_name': 'Disciplina',
                'verbose_name_plural': 'Disciplinas',
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('discipline', models.ForeignKey(to='core.Discipline')),
            ],
            options={
                'verbose_name': 'Encargo',
                'verbose_name_plural': 'Encargos',
            },
        ),
        migrations.CreateModel(
            name='Nature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Natureza da Atividade',
                'verbose_name_plural': 'Naturezas das Atividades',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('date_ini', models.DateField()),
                ('date_term', models.DateField()),
                ('course', models.ForeignKey(to='core.Course')),
            ],
            options={
                'verbose_name': 'Oferta',
                'verbose_name_plural': 'Ofertas',
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('date_ini', models.DateField()),
                ('date_term', models.DateField()),
            ],
            options={
                'verbose_name': 'Semestre',
                'verbose_name_plural': 'Semestres',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('phone1', models.CharField(max_length=14)),
                ('phone2', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('active', models.BooleanField()),
                ('effective', models.BooleanField()),
                ('area', models.ForeignKey(to='core.Area')),
                ('contract_type', models.ForeignKey(to='core.ContractType')),
                ('course', models.ForeignKey(to='core.Course')),
            ],
            options={
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professores',
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'T\xedtulo',
                'verbose_name_plural': 'T\xedtulos',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('campus', models.ForeignKey(to='core.Campus')),
                ('course', models.ForeignKey(to='core.Course')),
            ],
            options={
                'verbose_name': 'Usu\xe1rio',
                'verbose_name_plural': 'Usu\xe1rios',
            },
        ),
        migrations.AddField(
            model_name='teacher',
            name='title',
            field=models.ForeignKey(to='core.Title'),
        ),
        migrations.AddField(
            model_name='offer',
            name='semester',
            field=models.ForeignKey(to='core.Semester'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='offer',
            field=models.ForeignKey(to='core.Offer'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='teacher',
            field=models.ForeignKey(to='core.Teacher'),
        ),
        migrations.AddField(
            model_name='activitytype',
            name='nature',
            field=models.ForeignKey(to='core.Nature'),
        ),
        migrations.AddField(
            model_name='activity',
            name='act_type',
            field=models.ForeignKey(to='core.ActivityType'),
        ),
        migrations.AddField(
            model_name='activity',
            name='teacher',
            field=models.ForeignKey(to='core.Teacher'),
        ),
    ]
