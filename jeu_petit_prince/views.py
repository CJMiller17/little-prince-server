from rest_framework.decorators import parser_classes, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser


@api_view(["POST"])
@permission_classes([])
@parser_classes([MultiPartParser, FormParser])
def create_profile(request):
    user = User.objects.create(username = request.data["username"])
    user.set_password(request.data["password"])
    user.save()
    butterflies = request.data.get('butterflies', False)
    if butterflies == 'yes':
        butterflies = True
    elif butterflies == 'no':
        butterflies = False
    else:
        butterflies = False
        profile = Profile.objects.create(
        account_name = user,
        name = request.data["name"],
        profile_image = request.data.get("profile_image"),
        butterflies = butterflies,
        elephants = request.data.get("elephants", 0),
        fav_color = request.data.get("fav_color", ""),
        score_little_prince = request.data.get("score_little_prince", 0),
        score_king = request.data.get("score_king", 0),
        score_conceited_man = request.data.get("score_conceited_man", 0),
        score_drunkard = request.data.get("score_drunkard", 0),
        score_business_man = request.data.get("score_business_man", 0),
        score_lamplighter = request.data.get("score_lamplighter", 0),
        score_geographer = request.data.get("score_geographer", 0),
        score_earth = request.data.get("score_earth", 0),
    )
    profile.save()
    serialized_profile = ProfileSerializer(profile)
    return Response(serialized_profile.data, status=status.HTTP_201_CREATED)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
# @permission_classes([])
def get_profile(request, pk=None):
    # user=request.user
    # profile=Profile.objects.get(user=user.pk)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Request: ", request, "Pk: ", pk)
    if pk:
        # if request.user.profile.id !=pk: 
        #     print('profile.id: ',request.user.profile.id)
        #     return Response(status=status.HTTP_403_FORBIDDEN)
        print(request.user.profile)
        profile = get_object_or_404(Profile, pk=pk)
    else:
        profile = request.user.profile 
    serialized_profile = ProfileSerializer(profile)
    return Response(serialized_profile.data)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_profile(request, pk=None):
    print(request)
    print("Request user ID:", request.user.id)
    print("Request user profile ID:", request.user.profile.id)
    print("Provided pk:", pk)
    print("Request data:", request.data)
    if pk:
        if request.user.profile.id != pk:
            print(request)
            return Response(status=status.HTTP_418_IM_A_TEAPOT)
        profile = get_object_or_404(Profile, pk=pk)
    else:
        profile = request.user.profile
    
    profile.name = request.data.get("name", profile.name)
    profile.profile_image = request.data.get("profile_image", profile.profile_image)
    profile.butterflies = request.data.get("butterflies", profile.butterflies)
    profile.elephants = request.data.get("elephants", profile.elephants)
    profile.fav_color = request.data.get("fav_color", profile.fav_color)
    profile.score_little_prince = request.data.get("score_little_prince", profile.score_little_prince)
    profile.score_king = request.data.get("score_king", profile.score_king)
    profile.score_conceited_man = request.data.get("score_conceited_man", profile.score_conceited_man)
    profile.score_drunkard = request.data.get("score_drunkard", profile.score_drunkard)
    profile.score_business_man = request.data.get("score_business_man", profile.score_business_man)
    profile.score_lamplighter = request.data.get("score_lamplighter", profile.score_lamplighter)
    profile.score_geographer = request.data.get("score_geographer", profile.score_geographer)
    profile.score_earth = request.data.get("score_earth", profile.score_earth)

    profile.save()
    serialized_profile = ProfileSerializer(profile)
    return Response(serialized_profile.data)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.user.profile.id != pk:
        return Response(status=status.HTTP_403_FORBIDDEN)
    profile.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)