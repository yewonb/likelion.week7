from django.db import models

class Post(models.Model):  
  title=models.CharField(max_length=100)
  body=models.TextField(default="")
  created_at=models.DateField(auto_now_add=True)

  def __str__(self):
    return self.title

class Comment(models.Model):
  post=models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
  created_at=models.DateField(auto_now_add=True)
  comment=models.TextField(default="")

  def __str__(self):
    return self.comment


