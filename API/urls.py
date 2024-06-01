from django.urls import path
from . import views

urlpatterns = [
    # User Profile Creation
    path('create/', views.CreateProfileView.as_view(), name='create-profile'),
    path('update/<str:pk>', views.UpdateProfileView.as_view(), name='update-profile'),
    path('profile/<str:pk>/', views.ProfileView.as_view(), name='user-profile'),

    # LFG Alerts
    path('lfg/', views.CreateLFGAlertView.as_view(), name='create-alert'),
    path('update_lfg/<int:id>', views.UpdateLFGAlertView.as_view(), name='update-alert'),
    path('list_lfg/', views.ListLFGAlertView.as_view(), name='view-alerts'),
    path('delete_lfg/<str:pk>', views.DeleteLFGAlert.as_view(), name='delete-alert'),

    path('search_lfg/', views.SearchLFGAlert.as_view(), name='search-lfg'),

    path('send-match-notification/', views.SendMatchNotificationView.as_view(), name='match-notify'),
    path('notifications/', views.NotificationListView.as_view(), name='match-list'),
    
    path('reply/', views.SendMessagesView.as_view(), name='match-reply'),


    #path('login/', views.loginView.as_view(), name='login'),
    #path('logout/', views.logoutView.as_view(), name='logout'),
    #path('register/', views.registerView.as_view(), name='register'),

    #path('', views.dashboardView, name='dashboard'),
    #
    #
    #path('host_reply/', views.hostReplyView, name='host-reply'),
    #path('check_credits/', views.checkCreditsView, name='check-credits'),
    #path('buy_credits/', views.buyCreditsView, name='buy-credits'),

]