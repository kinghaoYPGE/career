from django.db import models
from django.utils import timezone


class Upload(models.Model):
    """
    文件上传对象
    """
    file_name = models.CharField(max_length=32)
    file_size = models.CharField(max_length=10)
    download_count = models.IntegerField(default=0)
    upload_time = models.DateTimeField(default=timezone.now)
    file_path = models.CharField(max_length=32)
    ip_addr = models.CharField(max_length=32)

    def __str__(self):
        return self.file_name

    def to_dict(self):
        return {
            'file_name': self.file_name,
            'file_size': self.file_size,
            'ip_addr': self.ip_addr,
            'upload_time': str(self.upload_time),
            'file_path': self.file_path,
        }


