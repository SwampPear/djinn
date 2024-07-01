from django.db import models


class Project(models.Model):
    project_id = models.AutoField(primary_key=True, null=False)
    project_name = models.CharField(max_length=64)


class Sprint(models.Model):
    sprint_id = models.AutoField(primary_key=True, null=False)
    sprint_prompt = models.CharField(max_length=128)
    project_id = models.ForeignKey(Project, on_delete=models.PROTECT)


class Iteration(models.Model):
    iteration_id = models.AutoField(primary_key=True, null=False)
    sprint_id = models.ForeignKey(Sprint, on_delete=models.PROTECT)


class Log(models.Model):
    log_id = models.AutoField(primary_key=True, null=False)
    log_type = models.CharField(max_length=2, null=False)
    contents = models.TextField()
    sprint_id = models.ForeignKey(Iteration, on_delete=models.PROTECT)
