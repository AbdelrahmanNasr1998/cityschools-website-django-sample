from django.urls import path
from . import views

urlpatterns = [
    path('notifications/class=0/new_post/', views.PostCreateViewA0.as_view(), name='Notification_A0_New_Post'),
    path('notifications/class=1/new_post/', views.PostCreateViewA1.as_view(), name='Notification_A1_New_Post'),
    path('notifications/class=2/new_post/', views.PostCreateViewA2.as_view(), name='Notification_A2_New_Post'),
    path('notifications/class=3/new_post/', views.PostCreateViewB1.as_view(), name='Notification_B1_New_Post'),
    path('notifications/class=4/new_post/', views.PostCreateViewB2.as_view(), name='Notification_B2_New_Post'),
    path('notifications/class=5/new_post/', views.PostCreateViewB3.as_view(), name='Notification_B3_New_Post'),
    path('notifications/class=6/new_post/', views.PostCreateViewB4.as_view(), name='Notification_B4_New_Post'),
    path('notifications/class=7/new_post/', views.PostCreateViewB5.as_view(), name='Notification_B5_New_Post'),
    path('notifications/class=8/new_post/', views.PostCreateViewB6.as_view(), name='Notification_B6_New_Post'),
    path('notifications/class=9/new_post/', views.PostCreateViewC1.as_view(), name='Notification_C1_New_Post'),
    path('notifications/class=10/new_post/', views.PostCreateViewC2.as_view(), name='Notification_C2_New_Post'),
    path('notifications/class=11/new_post/', views.PostCreateViewC3.as_view(), name='Notification_C3_New_Post'),
    path('notifications/class=12/new_post/', views.PostCreateViewD1.as_view(), name='Notification_D1_New_Post'),
    path('notifications/class=13/new_post/', views.PostCreateViewD2.as_view(), name='Notification_D2_New_Post'),
    path('notifications/class=14/new_post/', views.PostCreateViewD3.as_view(), name='Notification_D3_New_Post'),

    path('all_notifications/', views.All_Notifications, name='All_Notifications'),

    path('notifications/class=0/', views.Notification_A0_News, name='Notification_A0_News'),
    path('notifications/class=1/', views.Notification_A1_News, name='Notification_A1_News'),
    path('notifications/class=2/', views.Notification_A2_News, name='Notification_A2_News'),
    path('notifications/class=3/', views.Notification_B1_News, name='Notification_B1_News'),
    path('notifications/class=4/', views.Notification_B2_News, name='Notification_B2_News'),
    path('notifications/class=5/', views.Notification_B3_News, name='Notification_B3_News'),
    path('notifications/class=6/', views.Notification_B4_News, name='Notification_B4_News'),
    path('notifications/class=7/', views.Notification_B5_News, name='Notification_B5_News'),
    path('notifications/class=8/', views.Notification_B6_News, name='Notification_B6_News'),
    path('notifications/class=9/', views.Notification_C1_News, name='Notification_C1_News'),
    path('notifications/class=10/', views.Notification_C2_News, name='Notification_C2_News'),
    path('notifications/class=11/', views.Notification_C3_News, name='Notification_C3_News'),
    path('notifications/class=12/', views.Notification_D1_News, name='Notification_D1_News'),
    path('notifications/class=13/', views.Notification_D2_News, name='Notification_D2_News'),
    path('notifications/class=14/', views.Notification_D3_News, name='Notification_D3_News'),

    path('notifications/class=0/<int:post_id>', views.Notification_A0_Detail, name='Notification_A0_Detail'),
    path('notifications/class=1/<int:post_id>/', views.Notification_A1_Detail, name='Notification_A1_Detail'),
    path('notifications/class=2/<int:post_id>/', views.Notification_A2_Detail, name='Notification_A2_Detail'),
    path('notifications/class=3/<int:post_id>/', views.Notification_B1_Detail, name='Notification_B1_Detail'),
    path('notifications/class=4/<int:post_id>/', views.Notification_B2_Detail, name='Notification_B2_Detail'),
    path('notifications/class=5/<int:post_id>/', views.Notification_B3_Detail, name='Notification_B3_Detail'),
    path('notifications/class=6/<int:post_id>/', views.Notification_B4_Detail, name='Notification_B4_Detail'),
    path('notifications/class=7/<int:post_id>/', views.Notification_B5_Detail, name='Notification_B5_Detail'),
    path('notifications/class=8/<int:post_id>/', views.Notification_B6_Detail, name='Notification_B6_Detail'),
    path('notifications/class=9/<int:post_id>/', views.Notification_C1_Detail, name='Notification_C1_Detail'),
    path('notifications/class=10/<int:post_id>/', views.Notification_C2_Detail, name='Notification_C2_Detail'),
    path('notifications/class=11/<int:post_id>/', views.Notification_C3_Detail, name='Notification_C3_Detail'),
    path('notifications/class=12/<int:post_id>/', views.Notification_D1_Detail, name='Notification_D1_Detail'),
    path('notifications/class=13/<int:post_id>/', views.Notification_D2_Detail, name='Notification_D2_Detail'),
    path('notifications/class=14/<int:post_id>/', views.Notification_D3_Detail, name='Notification_D3_Detail'),

]