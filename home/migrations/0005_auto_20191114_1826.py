
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_logininfo_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logininfo',
            name='link',
            field=models.CharField(max_length=225, unique=True),
        ),
    ]
