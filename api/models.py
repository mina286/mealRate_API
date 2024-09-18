from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator,MaxLengthValidator,MinLengthValidator
# Create your models here.
class Meal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        db_table = 'Meal'
        verbose_name = 'meal'
        verbose_name_plural = 'meals'

class Rating(models.Model):
    meal = models.ForeignKey(Meal,on_delete=models.CASCADE,related_name='rating_meal')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='rating_user')
    stars = models.IntegerField(validators =[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return f"{self.meal}--{self.user}"
    class Meta:
        db_table = 'Rating'
        verbose_name = 'rating'
        verbose_name_plural = 'ratings'
        constraints =[
            models.UniqueConstraint(fields=['meal','user'],name='meal_user_unique'),
        ]

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile_user')
    image = models.ImageField(upload_to='user/images/',default='/user/defaultuser/defuser.png',null=True,blank=True)
    age = models.IntegerField(default=0)