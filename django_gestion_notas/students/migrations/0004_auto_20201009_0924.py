# Generated by Django 2.2.13 on 2020-10-09 09:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0001_initial'),
        ('teachers', '0001_initial'),
        ('students', '0003_auto_20201006_0207'),
    ]

    operations = [
        migrations.AddField(
            model_name='admissionstudent',
            name='admitted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='admissionstudent',
            name='choosen_department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chosen_depts', to='academics.Department'),
        ),
        migrations.AddField(
            model_name='admissionstudent',
            name='counsel_comment',
            field=models.ManyToManyField(null=True, to='teachers.Teacher'),
        ),
        migrations.AddField(
            model_name='admissionstudent',
            name='counseling_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='counselors', to='teachers.Teacher'),
        ),
        migrations.CreateModel(
            name='CounselingComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('comment', models.CharField(max_length=150)),
                ('counselor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher')),
                ('registrant_student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.AdmissionStudent')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
