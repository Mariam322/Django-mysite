# Generated by Django 3.2 on 2021-04-26 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emballage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matiere', models.CharField(max_length=20)),
                ('couleur', models.CharField(choices=[('bl', 'blanc'), ('rg', 'rouge'), ('ble', 'bleu'), ('vr', 'vert'), ('muli', 'multicolore')], default='transparant', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='img',
            field=models.ImageField(blank=True, default='aliment.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='produit',
            name='emballage',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='magasin.emballage'),
        ),
        migrations.AddField(
            model_name='produit',
            name='fournisseur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='magasin.fournisseur'),
        ),
    ]
