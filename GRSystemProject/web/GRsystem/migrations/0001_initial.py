from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('collegename', models.CharField(choices=[('College1', 'College1'), ('College2', 'College2')], max_length=29)),
                ('contactnumber', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format:Up to 10 digits allowed.', regex='^\\d{10,10}$')])),
                ('type_user', models.CharField(choices=[('student', 'student'), ('grievance', 'grievance')], default='student', max_length=20)),
                ('Branch', models.CharField(choices=[('ComputerScience', 'ComputerScience'), ('InformationScience', 'InformationScience'), ('Electronics and Communication', 'Electronics and Communication'), ('Mechanical', 'Mechanical')], default='ComputerScience', max_length=29)),
            ],
        ),
        migrations.CreateModel(
            name='Grievance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guser', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(max_length=200, null=True)),
                ('Type_of_complaint', models.CharField(choices=[('ClassRoom', 'ClassRoom'), ('Teacher', 'Teacher'), ('Management', 'Management'), ('College', 'College'), ('Other', 'Other')], max_length=200, null=True)),
                ('Description', models.TextField(max_length=4000, null=True)),
                ('Time', models.DateField(auto_now=True)),
                ('status', models.IntegerField(choices=[(1, 'Solved'), (2, 'InProgress'), (3, 'Pending')], default=3)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
