# Generated by Django 4.0.4 on 2022-05-09 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Icreat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(verbose_name='과제명')),
                ('sub_num', models.CharField(max_length=100, unique=True, verbose_name='과제번호')),
                ('period', models.CharField(blank=True, max_length=20, null=True, verbose_name='연구기간')),
                ('boundary', models.CharField(max_length=50, verbose_name='연구범위')),
                ('remark', models.CharField(max_length=100, verbose_name='연구종류')),
                ('institute', models.CharField(max_length=100, verbose_name='연구책임기관')),
                ('trial', models.CharField(blank=True, max_length=100, null=True, verbose_name='임상시험단계(연구모형)')),
                ('goal_research', models.IntegerField(blank=True, null=True, verbose_name='전체목표연구대상자수')),
                ('meddept', models.CharField(max_length=100, verbose_name='진료과')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'icreat',
            },
        ),
        migrations.AddIndex(
            model_name='icreat',
            index=models.Index(fields=['sub_num'], name='sub_num_idx'),
        ),
    ]
