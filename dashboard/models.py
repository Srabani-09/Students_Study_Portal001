from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description=models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "notes"
        verbose_name_plural = "notes"
class Homework(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due = models.DateTimeField()
    is_finished=models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_finished=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
# class User(AbstractUser):
#     groups = models.ManyToManyField('auth.Group',related_name="dashboard_user_groups",blank=True)
#     user_permissions = models.ManyToManyField('auth.Permission',related_name="dashboard_user_permissions",blank=True)
#     user = None
#     email = models.EmailField(unique=True)
#     is_verifird = models.CharField(max_length=4, null=True, blank=True)
    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     # objects = UserManager()
#     def __str__(self):
#         return self.email
    
# # class ForgetPassword(models.Model):
# #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# #     forget_password_token = models.CharField(max_length=200,null=True,blank=True)
    
    