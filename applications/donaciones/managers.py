from django.db import models

class DonacionManager(models.Manager):
  
  def crear_donacion(self ,contacto,detalle,categoria,usuario_donador):
      donacion=self.model(
        contacto=contacto,
        detalle=detalle,
        categoria=categoria,
  
      )
      donacion.save(using=self.db)
      return donacion
 
    
