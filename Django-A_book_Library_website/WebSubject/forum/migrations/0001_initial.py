# Generated by Django 3.2.5 on 2022-07-24 07:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
        ('interface', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_id', models.CharField(max_length=20, unique=True, verbose_name='组织ID')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_tid', models.CharField(max_length=16, verbose_name='帖子id')),
                ('r_uid', models.CharField(max_length=16, verbose_name='发表者id')),
                ('r_time', models.DateField(auto_now_add=True, verbose_name='留言时间')),
                ('r_content', models.CharField(max_length=256, verbose_name='回复内容')),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.IntegerField(verbose_name='板块编号')),
                ('number', models.IntegerField(verbose_name='在该板块的编号')),
                ('r_text', models.TextField(verbose_name='推荐语')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book', verbose_name='书籍ID')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('text', models.CharField(max_length=3000, verbose_name='正文')),
                ('title', models.CharField(max_length=64, verbose_name='标题')),
                ('intro', models.CharField(blank=True, max_length=256, null=True, verbose_name='内容摘要')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('p_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='forum.content', verbose_name='指向内容的id')),
                ('tags', models.ManyToManyField(to='interface.Tag', verbose_name='标签')),
            ],
        ),
    ]