from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class XrayManager(models.Manager):

    def get_queryset(self):
        return super(XrayManager, self).get_queryset()\
                   .filter(status='complete')


class Dpl(models.Model):
    dpl_number = models.CharField(max_length=50)
    pipe_size = models.CharField(max_length=50)
    wall_size = models.CharField(max_length=50)

    def __str__(self):
        return self.dpl_number


class WeldNumber(models.Model):
    xray_status_choices = (
        ('incomplete', 'Incomplete'),
        ('complete', 'Complete')
    )
    qc_person = models.ForeignKey(User,
                                  related_name='pipeline_dpl')
    dpl = models.ForeignKey(Dpl)
    weld_number = models.CharField(max_length=50)
    xray_status = models.CharField(max_length=50,
                                   choices=xray_status_choices,
                                   default='incomplete')
    xray_completed = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,
                              choices=xray_status_choices,
                              default='incomplete')
    weld_notes = models.TextField(blank=True)

    objects = models.Manager()
    published = XrayManager()

    def get_date(self):
        month = self.publish.strftime('%b')
        day = self.publish.strftime('%d')
        year = self.publish.year
        message = str(month) + ' ' + str(day) + ' ' + str(year)
        return message

    class Meta:
        ordering = ('-xray_completed',)

    def __str__(self):
        return self.weld_number
