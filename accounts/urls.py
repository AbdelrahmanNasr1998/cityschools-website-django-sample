from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PasswordsChangeView

urlpatterns = [
    path('application/', views.Application.as_view(), name='application'),
    path('application/application_success/', views.ApplicationSuccess, name='application_success'),

    path('register/', views.register, name='register'),
    path('register/specialist_register/', views.specialist_register.as_view(), name='specialist_register'),
    path('register/teacher_register/', views.teacher_register.as_view(), name='teacher_register'),
    path('register/choose_student_class/', views.choose_student_class, name='choose_student_class'),

    path('register/choose_student_class/A_0_student_register/', views.A_0_register.as_view(),
         name='A_0_student_register'),
    path('register/choose_student_class/A_1_student_register/', views.A_1_register.as_view(),
         name='A_1_student_register'),
    path('register/choose_student_class/A_2_student_register/', views.A_2_register.as_view(),
         name='A_2_student_register'),
    path('register/choose_student_class/B_1_student_register/', views.B_1_register.as_view(),
         name='B_1_student_register'),
    path('register/choose_student_class/B_2_student_register/', views.B_2_register.as_view(),
         name='B_2_student_register'),
    path('register/choose_student_class/B_3_student_register/', views.B_3_register.as_view(),
         name='B_3_student_register'),
    path('register/choose_student_class/B_4_student_register/', views.B_4_register.as_view(),
         name='B_4_student_register'),
    path('register/choose_student_class/B_5_student_register/', views.B_5_register.as_view(),
         name='B_5_student_register'),
    path('register/choose_student_class/B_6_student_register/', views.B_6_register.as_view(),
         name='B_6_student_register'),
    path('register/choose_student_class/C_1_student_register/', views.C_1_register.as_view(),
         name='C_1_student_register'),
    path('register/choose_student_class/C_2_student_register/', views.C_2_register.as_view(),
         name='C_2_student_register'),
    path('register/choose_student_class/C_3_student_register/', views.C_3_register.as_view(),
         name='C_3_student_register'),
    path('register/choose_student_class/D_1_student_register/', views.D_1_register.as_view(),
         name='D_1_student_register'),
    path('register/choose_student_class/D_2_student_register/', views.D_2_register.as_view(),
         name='D_2_student_register'),
    path('register/choose_student_class/D_3_student_register/', views.D_3_register.as_view(),
         name='D_3_student_register'),

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/<username>', views.profile, name='profile'),
    path('show_profile/<username>', views.profileadmin, name='show_profile'),
    path('update_profile/<username>', views.profile_update, name='update_profile'),

    # path('show_update_profile/<username>', views.updateprofileadmin, name='show_update_profile'),

    # path('password/',auth_views.PasswordChangeView.as_view(template_name='accounts/change_password.html'),),
    path('password/', PasswordsChangeView.as_view(template_name='accounts/change_password.html'), ),
    path('password_change_successfully/', views.password_success, name='pass_success'),

    path('students/', views.students, name='students_list'),

    path('students/a0', views.students_list_A0, name='students_list_a0'),
    path('students/a1', views.students_list_A1, name='students_list_a1'),
    path('students/a2', views.students_list_A2, name='students_list_a2'),
    path('students/b1', views.students_list_B1, name='students_list_b1'),
    path('students/b2', views.students_list_B2, name='students_list_b2'),
    path('students/b3', views.students_list_B3, name='students_list_b3'),
    path('students/b4', views.students_list_B4, name='students_list_b4'),
    path('students/b5', views.students_list_B5, name='students_list_b5'),
    path('students/b6', views.students_list_B6, name='students_list_b6'),
    path('students/c1', views.students_list_C1, name='students_list_c1'),
    path('students/c2', views.students_list_C2, name='students_list_c2'),
    path('students/c3', views.students_list_C3, name='students_list_c3'),
    path('students/d1', views.students_list_D1, name='students_list_d1'),
    path('students/d2', views.students_list_D2, name='students_list_d2'),
    path('students/d3', views.students_list_D3, name='students_list_d3'),
]
