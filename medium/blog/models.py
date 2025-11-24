from django.db import models

class User(models.Model):
    pass

class Comment(models.Model):
    user = models.ManyToManyField(User, related_name="comments")


# a post can have multiple comments, and person can make multiple posts
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    comments = models.ForeignKey(Comment, null=True, on_delete=models.CASCADE, related_name='posts')