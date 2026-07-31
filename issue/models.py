from django.db import models

# Create your models here.
class Application(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Issue(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    steps_to_reproduce = models.TextField()
    result_expected = models.TextField()
    result_obtained = models.TextField()
    priority = models.CharField(max_length=10, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    severity = models.CharField(max_length=10, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    application = models.ForeignKey(Application, on_delete=models.PROTECT, related_name='issues')
    affected_version = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title