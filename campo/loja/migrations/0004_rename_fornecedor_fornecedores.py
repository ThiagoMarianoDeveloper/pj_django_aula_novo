# Generated by Django 5.0.6 on 2024-07-11 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("loja", "0003_fornecedor"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Fornecedor",
            new_name="Fornecedores",
        ),
    ]
