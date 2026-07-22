from issue import models


class IssueConfig(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.booleanField(default=False)
    title = models.CharField(max_length=100)
    steps_to_reproduce = models.TextField()
    result_expected = models.TextField()
    result_obtained = models.TextField()
    priority = models.CharField(max_length=10, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    severity = models.CharField(max_length=10, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    affected_application = models.CharField(max_length=100)
    affected_version = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
