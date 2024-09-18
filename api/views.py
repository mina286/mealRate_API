from django.shortcuts import render
from .serializer import MealSerializer,RatingSerializer,UserSerializer,ProfileSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import Meal,Rating,Profile
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import generics,mixins
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated,BasePermission
# Create your views here.
# 1.1 GET POST viewsets Meal
class Viewsets_Meal(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]
# 1.2 GET POST viewsets Ratinf
class Viewsets_Rating(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

##################################################

# 2.1 GET POST Generics meal
class Generics_Meal(generics.ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]

# 2.2 GET PUT DELETE Generics meal
class Generics_Meal_PK(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]

# 2.3 GET POST Generics rating
class Generics_Rating(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

# 2.4 GET PUT DELETE Generics rating
class Generics_Rating_PK(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer  
    permission_classes = [IsAuthenticated]

######################################################

# 3.1 GET POST Mixins Meal
class Mixins_Meal(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset =Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return self.list(request)  
    def post(self,request):
        return self.create(request)  

# 3.2 GET PUT DELETE Mixins Meal
class Mixins_Meal_PK(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset =Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        return self.retrieve(request)  
    
    def put(self,request,pk):
        return self.update(request)  
    
    def delete(self,request,pk):
        return self.destroy(request)  
    
# 3.3 GET POST Mixins Rating
class Mixins_Rating(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset =Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return self.list(request)  
    def post(self,request):
        return self.create(request)  

# 3.4 GET PUT DELETE Mixins Rating
class Mixins_Rating_PK(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset =Rating.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        return self.retrieve(request)  
    
    def put(self,request,pk):
        return self.update(request)  
    
    def delete(self,request,pk):
        return self.destroy(request)  
##################################################
# 4.1 GET POST fbv Meals

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def meals(request):
    if request.method == 'GET':
        try:
            meal =Meal.objects.all()
            serializer = MealSerializer(meal,many =True)

            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as ex :
            return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        try:
            data = request.data
            print('data==',data)
            # part 1 create meal with rating together
            if 'stars' in request.data or 'user' in request.data or 'meal' in request.data:
                serializer_meal = MealSerializer(data = data)
                if serializer_meal.is_valid() :
                    print('inside valide two')
                    serializer_meal.save()

                    last_meal = Meal.objects.all().last()
                    print('lasttt=',last_meal.id)
                    serializer_rating = RatingSerializer(data = data)
                    data['meal'] =last_meal.id
                    if serializer_rating.is_valid():
                        serializer_rating.save()
                        return Response(serializer_meal.data,status=status.HTTP_201_CREATED)       

                    else:
                        return Response({'error':f'error happend {serializer_rating.errors}'},status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'error':f'error happend {serializer_meal.errors}'},status=status.HTTP_400_BAD_REQUEST)
            # part 2 create meal only
            else :
                serializer_meal = MealSerializer(data = data)
                if serializer_meal.is_valid() :
                    print('inside valide  only 1')
                    serializer_meal.save()
                    return Response(serializer_meal.data,status=status.HTTP_201_CREATED)       
                else:
                    return Response({'error':f'error happend {serializer_meal.errors}'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex :
            return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)

# 4.2 GET PUT DELETE fbv Meals
@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])

def meals_pk(request,pk):
    if request.method == 'GET':
        try:
            meal =Meal.objects.get(id=pk)
            serializer = MealSerializer(meal)
         
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Meal.DoesNotExist  :
            return Response({'error':'meal not found '},status=status.HTTP_404_NOT_FOUND)
        except Exception as ex :
            return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        try:
            data = request.data
            print('data==',data)
            # part 1 create meal with rating together
            if 'stars' in request.data or 'user' in request.data or 'meal' in request.data:
                print('inside two ')
                meal =Meal.objects.get(id=pk)
                serializer_meal = MealSerializer(data =data,instance = meal,partial=True)
                if serializer_meal.is_valid():
                    print('ibvlid 1 ')
                    serializer_meal.save()
                
                    rating =Rating.objects.get(id=request.data['id'])
                    serializer_rating = RatingSerializer(data =data,instance = rating,partial=True)
                    if serializer_rating.is_valid():
                        print('ibvlid 2 ')
                        serializer_rating.save()
                    else:
                        return Response({'error':f'error happend {serializer_rating.errors}'},status=status.HTTP_400_BAD_REQUEST)
                    return Response(serializer_meal.data,status=status.HTTP_202_ACCEPTED)
                    print('not open vilid 2')
            # part 2 update meal only
            else :
                data = request.data
                print('data==',data)
                meal =Meal.objects.get(id=pk)
                serializer_meal = MealSerializer(data =data,instance = meal,partial=True)
                if serializer_meal.is_valid():
                    serializer_meal.save()
                    return Response(serializer_meal.data,status=status.HTTP_202_ACCEPTED)
                else:
                    return Response({'error':f'error happend {serializer_meal.errors}'},status=status.HTTP_400_BAD_REQUEST)
        except Meal.DoesNotExist  :
            return Response({'error':'meal not found '},status=status.HTTP_404_NOT_FOUND)
        except Exception as ex :
            return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        try:
            meal =Meal.objects.get(id=pk)
            meal.delete()
            return Response({'message':'meal is deleted '},status=status.HTTP_204_NO_CONTENT)
        except Meal.DoesNotExist  :
            return Response({'error':'meal not found '},status=status.HTTP_404_NOT_FOUND)

        except Exception as ex :
            return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)

# 4.3 GET POST fbv Meals
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])

def rating(request):
    if request.method == 'GET':
        try:
            rating =Rating.objects.all()
            serializer = RatingSerializer(rating,many =True)
         
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as ex :
            return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        try:
            data = request.data
            serializer = RatingSerializer(data =data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response({'error':f'error happend {serializer.errors}'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex :
            return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)

# 4.4 GET PUT DELETE fbv Meals
@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])

def rating_pk(request,pk):
    if request.method == 'GET':
        try:
            rating =Rating.objects.get(id=pk)
            serializer = RatingSerializer(rating)
         
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Rating.DoesNotExist  :
            return Response({'error':'rating not found '},status=status.HTTP_404_NOT_FOUND)
        except Exception as ex :
            return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        try:
            data = request.data
            rating =Rating.objects.get(id=pk)
            serializer = RatingSerializer(data =data,instance = rating,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'error':f'error happend {serializer.errors}'},status=status.HTTP_400_BAD_REQUEST)
        except Rating.DoesNotExist  :
            return Response({'error':'rating not found '},status=status.HTTP_404_NOT_FOUND)
        except Exception as ex :
            return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        try:
            rating =Rating.objects.get(id=pk)
            rating.delete()
            return Response({'message':'rating is deleted '},status=status.HTTP_204_NO_CONTENT)
        except Rating.DoesNotExist  :
            return Response({'error':'rating not found '},status=status.HTTP_404_NOT_FOUND)

        except Exception as ex :
            return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)

# 5.1 GET POST viewset user
class Viewsets_User(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# 5.2 GET POST viewset profile
class Viewsets_Profile(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# 5.3 GET POST fbv user
@api_view(['POST'])
def register_user(request):
    try :
        data = request.data
        serializer = UserSerializer(data =data)
        if serializer.is_valid():
           
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)

# 5.4 GET PUT DELETE fbv user
@api_view(['GET','PUT','DELETE'])
def update_user(request,pk):
    try :
        if request.method == 'GET':
            user = User.objects.get(id =pk)
            serializer = UserSerializer(user)
            return Response(serializer.data,status=status.HTTP_200_OK)

        if request.method == 'PUT':
            data = request.data
            user = User.objects.get(id =pk)
            serializer = UserSerializer(data =data,instance =user,partial =True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response({'error':f'error happend {serializer.errors}'},status=status.HTTP_400_BAD_REQUEST)
            
        if request.method == 'DELETE':
            user = User.objects.get(id =pk)
            user.delete()
            return Response({'message':'user is deleted'},status=status.HTTP_204_NO_CONTENT)
    
    except User.DoesNotExist :
        return Response({'error':f'user not found '},status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)

