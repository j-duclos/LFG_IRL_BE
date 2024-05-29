from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateProfileView.as_view(), name='create-profile'),
    path('update/<str:pk>', views.UpdateProfileView.as_view(), name='update-profile'),
    path('profile/<str:pk>/', views.ProfileView.as_view(), name='user-profile'),

    path('lfg/', views.CreateLFGAlertView.as_view(), name='create-alert'),



    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),

    #path('login/', views.loginView.as_view(), name='login'),
    #path('logout/', views.logoutView.as_view(), name='logout'),
    #path('register/', views.registerView.as_view(), name='register'),
    #
    #
    #

    #path('', views.dashboardView, name='dashboard'),
    #
    #path('update/<str:pk>', views.updateAlertView, name='update-alert'),
    #path('delete/<str:pk>', views.deleteAlertView, name='delete-alert'),
    #path('match/', views.matchNotifyView, name='match-notify'),
    #path('reply/', views.matchReplyView, name='match-reply'),
    #path('host_reply/', views.hostReplyView, name='host-reply'),
    #path('check_credits/', views.checkCreditsView, name='check-credits'),
    #path('buy_credits/', views.buyCreditsView, name='buy-credits'),



]