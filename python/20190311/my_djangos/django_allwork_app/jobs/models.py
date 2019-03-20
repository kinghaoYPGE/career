from django.db import models
from taggit.managers import TaggableManager


class Job(models.Model):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='job_owner')
    freelancer = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='job_freelancer')

    job_title = models.CharField(max_length=300)
    job_description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    tags = TaggableManager()

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    # 上传附件
    document = models.FileField(upload_to='attachment/%Y%m%d', blank=True, null=True)

    ACTIVE = 'active'
    WORKING = 'working'
    ENDED = 'ended'
    STATUS_CHOICES = (
        (ACTIVE, 'active'),
        (WORKING, 'working'),
        (ENDED, 'ended'),
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=ACTIVE,
    )

    @property
    def freelancers(self):
        # select freelancer_id from job_proposal where job_id = self.id
        return [proposal.freelancer for proposal in self.job_proposal.all()]


class JobProposal(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job_proposal')
    freelancer = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='job_proposal')
    proposal = models.TextField()

    class Meta:
        unique_together = ('job', 'freelancer')
