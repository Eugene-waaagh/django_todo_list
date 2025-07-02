from django.db import models

class Task(models.Model):
    title_text = models.CharField(max_length=100)
    description_text = models.CharField(max_length=100)
    due_date = models.DateField(null=True, blank=True)
    completed_boolean = models.BooleanField(default=False)

    def __str__(self):
        return self.title_text