
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20191114_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logininfo',
            name='failed_attempts',
        ),
        migrations.RemoveField(
            model_name='logininfo',
            name='success_attempts',
        ),
        migrations.AddField(
            model_name='logininfo',
            name='fails',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
