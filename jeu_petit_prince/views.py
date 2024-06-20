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
        games = request.data.get("games", ""),
        fav_color = request.data.get("fav_color", ""),
        birds_collected = request.data.get("birds_collected", 0),
        score_little_prince = request.data.get("score_little_prince", 0),
        score_king = request.data.get("score_king", 0),
        score_conceited_man = request.data.get("score_conceited_man", 0),
        score_drunkard = request.data.get("score_drunkard", 0),
        score_business_man = request.data.get("score_business_man", 0),
        score_lamplighter = request.data.get("score_lamplighter", 0),
        score_geographer = request.data.get("score_geographer", 0),
        score_earth = request.data.get("score_earth", 0),
        total_score = request.data.get("total_score", 0),
        item_1 = request.data.get("item_1", 0),
        item_2 = request.data.get("item_2", 0),
        item_3 = request.data.get("item_3", 0)
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
        if request.user.profile.id !=pk:
            print('profile.id: ',request.user.profile.id)
            return Response(status=status.HTTP_403_FORBIDDEN)
        print(request.user.profile)
        profile = get_object_or_404(Profile, pk=pk)
    else:
        profile = request.user.profile 
    serialized_profile = ProfileSerializer(profile)
    return Response(serialized_profile.data)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_profile(request, pk=None):
    if pk:
        if request.user.profile.id != pk:
            return Response(status=status.HTTP_403_FORBIDDEN)
        profile = get_object_or_404(Profile, pk=pk)
    else:
        profile = request.user.profile
    
    profile.name = request.data.get("name", profile.name)
    profile.profile_image = request.data.get("profile_image", profile.profile_image)
    profile.butterflies = request.data.get("butterflies", profile.butterflies)
    profile.elephants = request.data.get("elephants", profile.elephants)
    profile.games = request.data.get("games", profile.games)
    profile.fav_color = request.data.get("fav_color", profile.fav_color)
    profile.birds_collected = request.data.get("birds_collected", profile.birds_collected)
    profile.score_little_prince = request.data.get("score_little_prince", profile.score_little_prince)
    profile.score_king = request.data.get("score_king", profile.score_king)
    profile.score_conceited_man = request.data.get("score_conceited_man", profile.score_conceited_man)
    profile.score_drunkard = request.data.get("score_drunkard", profile.score_drunkard)
    profile.score_business_man = request.data.get("score_business_man", profile.score_business_man)
    profile.score_lamplighter = request.data.get("score_lamplighter", profile.score_lamplighter)
    profile.score_geographer = request.data.get("score_geographer", profile.score_geographer)
    profile.score_earth = request.data.get("score_earth", profile.score_earth)
    profile.total_score = request.data.get("total_score", profile.total_score)
    profile.item_1 = request.data.get("item_1", profile.item_1)
    profile.item_2 = request.data.get("item_2", profile.item_2)
    profile.item_3 = request.data.get("item_3", profile.item_3)

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