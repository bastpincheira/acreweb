# Generated by Django 3.2.4 on 2021-07-20 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acre', '0002_alter_wiki_idwiki'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wiki',
            name='idwiki',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id wiki'),
        ),
    ]