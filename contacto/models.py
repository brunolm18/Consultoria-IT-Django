from django.db import models

# Create your models here.
class Contacto(models.Model):
    correo_electronico = models.EmailField(max_length=100,verbose_name="correo_electronico")
    nombre = models.CharField(max_length=50,verbose_name="Nombre")
    asunto = models.TextField(max_length=400)

    class Meta:
        db_table = "Contacto_table"
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return self.nombre
