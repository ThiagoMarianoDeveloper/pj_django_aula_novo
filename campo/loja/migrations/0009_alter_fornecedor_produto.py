# Generated by Django 5.0.6 on 2024-08-29 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loja", "0008_remove_fornecedor_produto_fornecedor_produto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fornecedor",
            name="produto",
            field=models.ManyToManyField(to="loja.produto"),
        ),
    ]
