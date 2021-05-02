# Generated by Django 3.1.7 on 2021-04-25 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_attribute_attribute_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubConcept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_concept_name', models.CharField(max_length=30)),
                ('individuals', models.ManyToManyField(to='mainpage.Individual')),
            ],
        ),
        migrations.AddField(
            model_name='concept',
            name='sub_concepts',
            field=models.ManyToManyField(to='mainpage.SubConcept'),
        ),
    ]