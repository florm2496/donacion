from django.db import models


class FavoritosManager(models.Manager):
    def entradas_user(self , user):
        return self.filter(
            entry__public=True,
            user=user
        ).order_by('-created')