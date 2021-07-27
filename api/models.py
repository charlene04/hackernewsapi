from django.db import models

# Create your models here.
class Item(models.Model):
    item_id = models.IntegerField(blank= True, null=True)
    by = models.CharField(max_length=255, blank= True)
    time = models.IntegerField(null=True, blank= True)
    kids = models.JSONField(blank=True, null=True)
    parts = models.JSONField(null=True, blank=True)
    descendants = models.IntegerField(null=True, blank= True)
    score = models.IntegerField(null=True, blank= True)
    title = models.CharField(max_length=255, blank= True, null=True)
    url = models.URLField(max_length=255, blank= True, null=True)
    type = models.CharField(max_length=100, blank= False, null=True)
    parent = models.IntegerField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    deleted= models.BooleanField(blank=True, null=True)
    dead = models.BooleanField(blank=True, null=True)
    custom = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.title or self.text or self.by

    #Return a value on save()
    def save(self, *args, **kwargs):
        super(Item, self).save(*args, **kwargs)
        return self

    #Ensure only allowed fields are present in JSON request
    def update_fields(self, key, value):
        getattr(self, key)
        setattr(self, key, value)


   