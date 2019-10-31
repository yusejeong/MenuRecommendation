# Generated by Django 2.2.6 on 2019-10-31 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('ingre_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YTMT.Ingredient')),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YTMT.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.IntegerField(choices=[(1, '남자'), (2, '여자')])),
                ('birth', models.DateField()),
                ('reli_id', models.IntegerField(choices=[(1, '힌두교'), (2, '불교'), (3, '기독교'), (4, '천주교'), (5, '이슬람교'), (6, '유대교'), (7, '회교도'), (8, '시크교도'), (9, '무교')])),
                ('vege_id', models.IntegerField(choices=[(1, '비건'), (2, '락토 베지테리언'), (3, '오보 베지테리언'), (4, '락토 오보 베지테리언'), (5, '페스코 베지테리언'), (6, '플로 베지테리언'), (7, '플렉시테리언'), (8, '해당사항없음')])),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hate_menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YTMT.Menu')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hate_ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YTMT.Ingredient')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
