from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)


	#Optional here - perhaps a newer version of Python/Django?
	def __str__(self):
		return self.title


	