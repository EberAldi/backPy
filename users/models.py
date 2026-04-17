from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'users'   # 👈 nombre exacto de tu tabla en PostgreSQL
        managed = False      # 🚨 clave: Django NO crea ni modifica la tabla
