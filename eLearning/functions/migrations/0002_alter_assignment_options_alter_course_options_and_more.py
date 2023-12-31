# Generated by Django 4.2.7 on 2023-11-25 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assignment',
            options={'managed': True, 'ordering': ['title'], 'verbose_name': 'Assignment', 'verbose_name_plural': 'Assignments'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'managed': True, 'ordering': ['title'], 'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelOptions(
            name='enrollment',
            options={'managed': True, 'ordering': ['enrollment_date'], 'verbose_name': 'Enrollment', 'verbose_name_plural': 'Enrollments'},
        ),
        migrations.AlterModelOptions(
            name='grade',
            options={'managed': True, 'ordering': ['grade'], 'verbose_name': 'Grade', 'verbose_name_plural': 'Grades'},
        ),
        migrations.AlterModelOptions(
            name='interactionhistory',
            options={'managed': True, 'ordering': ['interaction_date'], 'verbose_name': 'Interaction', 'verbose_name_plural': 'Interactions'},
        ),
        migrations.AlterModelOptions(
            name='material',
            options={'managed': True, 'ordering': ['title'], 'verbose_name': 'Material', 'verbose_name_plural': 'Materials'},
        ),
        migrations.AlterModelOptions(
            name='readingstate',
            options={'managed': True, 'ordering': ['last_read_date'], 'verbose_name': 'State', 'verbose_name_plural': 'States'},
        ),
        migrations.AlterModelOptions(
            name='submission',
            options={'managed': True, 'ordering': ['submission_date'], 'verbose_name': 'submission', 'verbose_name_plural': 'submissions'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'managed': True, 'ordering': ['date_joined'], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterField(
            model_name='grade',
            name='assignment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.assignment'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='assignment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.assignment'),
        ),
        migrations.AlterModelTable(
            name='assignment',
            table='',
        ),
        migrations.AlterModelTable(
            name='course',
            table='',
        ),
        migrations.AlterModelTable(
            name='enrollment',
            table='',
        ),
        migrations.AlterModelTable(
            name='grade',
            table='',
        ),
        migrations.AlterModelTable(
            name='interactionhistory',
            table='',
        ),
        migrations.AlterModelTable(
            name='material',
            table='',
        ),
        migrations.AlterModelTable(
            name='readingstate',
            table='',
        ),
        migrations.AlterModelTable(
            name='submission',
            table='',
        ),
        migrations.AlterModelTable(
            name='user',
            table='',
        ),
        migrations.CreateModel(
            name='Reclamation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reclam', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reclamation', to='app.user')),
            ],
            options={
                'verbose_name': 'reclamation',
                'verbose_name_plural': 'reclamations',
                'db_table': '',
                'ordering': ['date_reclam'],
                'managed': True,
            },
        ),
    ]
