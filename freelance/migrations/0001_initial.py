# Generated by Django 4.2.11 on 2024-04-25 17:56

from django.db import migrations, models
import django.db.models.deletion
import freelance.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('firstname', models.TextField(verbose_name='firstname')),
                ('surname', models.TextField(verbose_name='surname')),
                ('position', models.TextField(validators=[freelance.models.check_position_exists], verbose_name='position')),
            ],
            options={
                'verbose_name': 'developer',
                'verbose_name_plural': 'developers',
                'db_table': '"freelance"."developer"',
                'ordering': ['surname', 'firstname'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('status', models.TextField(validators=[freelance.models.check_status_exists], verbose_name='status')),
            ],
            options={
                'verbose_name': 'task',
                'verbose_name_plural': 'tasks',
                'db_table': '"freelance"."task"',
                'ordering': ['name', 'status'],
            },
        ),
        migrations.CreateModel(
            name='TaskDeveloper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelance.developer', verbose_name='developer')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelance.task', verbose_name='task')),
            ],
            options={
                'verbose_name': 'relationship task developer',
                'verbose_name_plural': 'relationships task developer',
                'db_table': '"freelance"."task_developer"',
                'unique_together': {('task', 'developer')},
            },
        ),
        migrations.AddField(
            model_name='task',
            name='developers',
            field=models.ManyToManyField(through='freelance.TaskDeveloper', to='freelance.developer', verbose_name='developers'),
        ),
        migrations.AddField(
            model_name='developer',
            name='tasks',
            field=models.ManyToManyField(through='freelance.TaskDeveloper', to='freelance.task', verbose_name='tasks'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField(verbose_name='content')),
                ('publication_date', models.DateField(verbose_name='publication date')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelance.task', verbose_name='task')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'db_table': '"freelance"."comment"',
                'ordering': ['content'],
            },
        ),
    ]