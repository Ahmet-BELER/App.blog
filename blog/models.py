from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):  
    image = models.ImageField(upload_to="profiles/%Y", default="default.jpg")
    bio = models.TextField(max_length=5000, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):  
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):  
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to="posts/%Y")
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (
        ("active", "active"),
        ("deactive", "deactive"),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    slug = models.SlugField(
        verbose_name='slug',
        allow_unicode=True,
        max_length=255,
        default = title,
        help_text=("The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/") # Slug
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):  
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=2000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')                 #Post
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')        #User

    def __str__(self):
        return self.user.username.title() + ' - ' + self.post.title
    
    
class PostView(models.Model):  
    timestamp = models.TimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username.title()

class Like(models.Model):  # ok
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="likes")
    posts = models.ForeignKey(
        Post, on_delete=models.SET_NULL, null=True, related_name="likes")

    def __str__(self):
        return self.user.username + ' - ' + self.posts.title

    class Meta:
        # db_table = 'likes'
        constraints = [
            models.UniqueConstraint(
                fields=['posts', 'user'], name="unique_like")
        ]
        # unique_together = ('user', 'posts',)

    
