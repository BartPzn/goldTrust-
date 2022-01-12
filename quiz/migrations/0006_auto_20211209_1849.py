

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20201209_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(choices=[('Option1', 'Odpowiedź1'), ('Option2', 'Odpowiedź2'), ('Option3', 'Odpowiedź3'), ('Option4', 'Odpowiedź4')], max_length=200),
        ),
    ]
