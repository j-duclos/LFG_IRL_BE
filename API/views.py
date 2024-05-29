from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, ProfileSerializer, NoteSerializer, LFGAlertSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note, Profile, LFGAlert


#from django.contrib import messages
#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth.decorators import login_required
#rom .forms import UserRegistrationForm, ProfileForm

#from django.shortcuts import get_object_or_404


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class CreateProfileView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny]

class UpdateProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

class ProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

class CreateLFGAlertView(generics.CreateAPIView):
    queryset = LFGAlert.objects.all()
    serializer_class = LFGAlertSerializer
    permission_classes = [AllowAny] #[IsAuthenticated]









class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)


