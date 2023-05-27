from django.db import models

# Create your models here.

#modelo para la base de datos, campos , usamos "verbose_name para cambiar el titulo en la representacion"
class Contact (models.Model):
    avatar = models.ImageField(upload_to='contact_pics',null=True, blank=True)
    name = models.CharField(max_length=200, verbose_name='Nombre')
    email = models.EmailField(max_length=70, verbose_name='Correo')
    birth = models.DateField(null=True, blank=True, verbose_name='Nacimiento')
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Telefono')
    created = models.DateTimeField(auto_now_add=True)

# metodo str para mostar en el admin el campo nombre en lugar del objeto
    def __str__(self) -> str:
        return self.name
    