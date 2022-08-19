

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(blank=True, default="user_image.png", max_length=255, null=True),
        ),
    ]
