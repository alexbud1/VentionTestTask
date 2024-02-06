from django.db import models
from shortuuid.django_fields import ShortUUIDField


class Category(models.Model):
    id = ShortUUIDField(length=10, prefix="id_", primary_key=True, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Task(models.Model):
    id = ShortUUIDField(length=10, prefix="id_", primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    # SET_NULL was chosen as I would like to keep my tasks even if the category is deleted
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False)
    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["completed"]
