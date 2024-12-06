# 

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulos',
            name='cantidad',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
