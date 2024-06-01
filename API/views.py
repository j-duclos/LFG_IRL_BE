from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSerializer, ProfileSerializer, LFGAlertSerializer, NotificationSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Profile, LFGAlert, Notification
from django_filters import rest_framework as filters


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
    permission_classes = [AllowAny] #[IsAuthenticated]

class ProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny] #[IsAuthenticated]

class CreateLFGAlertView(generics.CreateAPIView):
    queryset = LFGAlert.objects.all()
    serializer_class = LFGAlertSerializer
    permission_classes = [AllowAny] #[IsAuthenticated]

class UpdateLFGAlertView(generics.RetrieveUpdateAPIView):
    queryset = LFGAlert.objects.all()
    serializer_class = LFGAlertSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny] #[IsAuthenticated]

class ListLFGAlertView(generics.ListAPIView):
    queryset = LFGAlert.objects.all()
    serializer_class = LFGAlertSerializer
    permission_classes = [AllowAny] #[IsAuthenticated]    

class DeleteLFGAlert(generics.DestroyAPIView):
    queryset = LFGAlert.objects.all()
    serializer_class = LFGAlertSerializer
    permission_classes = [AllowAny] #[IsAuthenticated]  
    lookup_field = 'pk'

    """ def get_queryset(self):
        user = self.request.user
        return LFGAlert.objects.filter(pLeader=user) """

class LFGAlertFilter(filters.FilterSet):
    interest = filters.CharFilter(field_name="interest", lookup_expr='icontains')

    locationsCity = filters.CharFilter(field_name="locationsCity", lookup_expr='icontains')
    locationState = filters.CharFilter(field_name="locationState", lookup_expr='icontains')
    #locationZip = filters.CharFilter(field_name="locationZip", lookup_expr='icontains')
    # radius = filters.CharFilter(field_name="radius", lookup_expr='icontains')
    # Add more filters as needed

    class Meta:
        model = LFGAlert
        fields = ["interest", "locationCity", "locationState"]
        #fields = ['interest', 'locationsCity', 'locationState', 'locationZip']

class SearchLFGAlert(generics.ListAPIView):
    queryset = LFGAlert.objects.all()
    serializer_class = LFGAlertSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LFGAlertFilter
    #permission_classes = [AllowAny] #[IsAuthenticated]   

class SendMatchNotificationView(generics.GenericAPIView):
    serializer_class = NotificationSerializer

    def post(self, request, *args, **kwargs):
        event_id = request.data.get('event_id')
        user_id = request.data.get('user_id')
        user = User.objects.get(id=user_id)

        try:
            event = LFGAlert.objects.get(id=event_id)
            user = User.objects.get(id=user_id)
            

            message = f"You have been matched with a group: {event.title}"

            notification = Notification.objects.create(user=user, message=message)
            serializer = self.get_serializer(notification)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except LFGAlert.DoesNotExist:
            return Response({"error": "Group not found!"}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({"error": "Party leader not found!"}, status=status.HTTP_404_NOT_FOUND)

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [AllowAny] #[IsAuthenticated] 

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(user=user).order_by('-created_at')
    
class SendMessagesView(generics.CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [AllowAny] #[IsAuthenticated] 

    def perform_create(self, serializer):
        message = serializer.save(sender=self.request.user)
        Notification.objects.create(
            user=message.recipient,
            message=f"You have a new message from {message.sender.username}"
        )