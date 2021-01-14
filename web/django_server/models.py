from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel):
    name = models.CharField(max_length=128)
    level = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.name}\t{self.level}'
