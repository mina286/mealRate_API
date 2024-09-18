from rest_framework import serializers
from .models import Meal,Rating,Profile
from django.contrib.auth.models import User

 #1 
class MealSerializer(serializers.ModelSerializer):
    number_rating = serializers.SerializerMethodField(read_only =True)
    def get_number_rating(self,obj):
        number_rating = obj.rating_meal.all().count()
        return f"{number_rating}"
    
    average_rating = serializers.SerializerMethodField(read_only =True)
    def get_average_rating(self,obj):
        number_rating = obj.rating_meal.all().count()
        ratings = obj.rating_meal.all()
        list_rate = []
        for rate in ratings:
            list_rate.append(rate.stars)
        sum_ratings = sum(list_rate)
        try :
            average_rating = sum_ratings / number_rating
            return f"{average_rating}"
        except :
            return f""
    

    rating = serializers.SerializerMethodField(read_only =True)
    def get_rating(self,obj):
        ratings = obj.rating_meal.all()
        serializer = RatingSerializer(ratings,many =True)

        return serializer.data
    
    class Meta:
        model = Meal
        fields = "__all__"
 # 2
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"

# 3
class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"

# 4
class UserSerializer(serializers.ModelSerializer):
    password =serializers.CharField(write_only =True)
    def create(self,data):
        print('data===',data)
        user = User(**data)
        password = data.pop('password')
        user.set_password(password)
        user.save()
        return user
    
    def update(self,instance,data):
        print('data update====',data)
        print('data instance====',instance,type(instance))
        password = data.pop('password')
        user = instance
        user.set_password(password)
        return super().update(instance,data)
    
    profile = serializers.SerializerMethodField(read_only =True)
    def get_profile(self,obj):
        print('profile_name insideeeeee')
        if hasattr(obj,'profile_user'):
            profile = obj.profile_user
            print('profile_name====',profile)
            serializer = ProfileSerializer(profile)
            return serializer.data
        else:
            return {}
    
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','email','profile']


