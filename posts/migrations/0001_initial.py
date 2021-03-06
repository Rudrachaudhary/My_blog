# Generated by Django 2.1.dev20180313180640 on 2018-04-18 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=240)),
                ('content', models.TextField(null=True, verbose_name='content')),
                ('featured', models.FileField(upload_to='documents/')),
                ('timestamps', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
                ('tags', models.ManyToManyField(to='tags.Tag')),
            ],
        ),
    ]
