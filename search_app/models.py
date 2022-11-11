from django.db import models

class cutoff(models.Model):
    college_code = models.IntegerField()
    college_name = models.CharField(max_length=100)
    branch_code = models.IntegerField()
    branch_name = models.CharField(max_length=100)
    status_category = models.CharField(max_length=50)
    open_percentile = models.FloatField(max_length=20)


    def __str__(self):
        return self.college_name
        