from django.db import models

class AnalysisResult(models.Model):
    RESULT_TYPES = [
        ('change_detection', 'Change Detection'),
        ('overview_statistics', 'Overview Statistics'),
        ('transition_matrix', 'Transition Matrix'),
        ('accuracy_assessment', 'Accuracy Assessment'),  # ← add this
    ]
    name = models.CharField(max_length=255)
    result_type = models.CharField(max_length=50, choices=RESULT_TYPES)
    data = models.JSONField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.result_type})"