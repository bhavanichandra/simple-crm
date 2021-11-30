from django.db import models


class UserAudit(models.Model):
    """
    UserAudit model.
    """
    id = models.AutoField(primary_key=True, blank=False, null=False)
    user_id = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    request_type = models.CharField(max_length=50)
    request_body = models.JSONField()
    request_url = models.TextField()
    request_success = models.BooleanField(default=False)
    error_message = models.TextField()
