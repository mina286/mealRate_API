from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('meal_crud',views.Viewsets_Meal)
router.register('rating_crud',views.Viewsets_Rating)
router.register('user_crud',views.Viewsets_User)
router.register('profile_crud',views.Viewsets_Profile)
app_name ='api'
urlpatterns = [

    # 1.2 GET POST viewsets 
    path('Viewsets_Meal/',include(router.urls),name='Viewsets_Meal'),
    path('Viewsets_Rating/',include(router.urls),name='Viewsets_Rating'),
    # 2.1 GET POST Generics meal
    path('Generics_Meal/',views.Generics_Meal.as_view(),name='Generics_Meal'),
    # 2.2 GET PUT DELETE Generics meal
    path('Generics_Meal_PK/<int:pk>/',views.Generics_Meal_PK.as_view(),name='Generics_Meal_PK'),
    # 2.3 GET POST Generics rating
    path('Generics_Rating/',views.Generics_Rating.as_view(),name='Generics_Rating'),
    # 2.4 GET PUT DELETE Generics rating
    path('Generics_Rating_PK/<int:pk>/',views.Generics_Rating_PK.as_view(),name='Generics_Rating_PK'),
    # 3.1 GET POST Mixins Meal
    path('Mixins_Meal/',views.Mixins_Meal.as_view(),name='Mixins_Meal'),
    # 3.2 GET PUT DELETE Mixins Meal
    path('Mixins_Meal_PK/<int:pk>/',views.Mixins_Meal_PK.as_view(),name='Mixins_Meal_PK'),
    # 3.3 GET POST Mixins Rating
    path('Mixins_Rating/',views.Mixins_Rating.as_view(),name='Mixins_Rating'),
    # 3.4 GET PUT DELETE Mixins Rating
    path('Mixins_Rating_PK/<int:pk>/',views.Mixins_Rating_PK.as_view(),name='Mixins_Rating_PK'),
    # 4.1 GET POST fbv Meals
    path('meals/',views.meals,name='meals'),
    # 4.2 GET PUR DELETE fbv Meals
    path('meals_pk/<int:pk>/',views.meals_pk,name='meals_pk'),
    # 4.3 GET POST fbv rating
    path('rating/',views.rating,name='rating'),
    # 4.4 GET PUT DELETE fbv Meals
    path('rating_pk/<int:pk>/',views.rating_pk,name='rating_pk'),
    # 5.1 GET POST viewset user
    path('Viewsets_User/',include(router.urls),name='Viewsets_User'),
    # 5.2 GET POST viewset profile
    path('Viewsets_Profile/',include(router.urls),name='Viewsets_Profile'),
    # 5.3 GET POST fbv user
    path('register_user/',views.register_user,name='register_user'),
    # 5.4 GET PUT DELETE fbv user
    path('update_user/<int:pk>/',views.update_user,name='update_user'),





]
