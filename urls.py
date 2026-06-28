from django.urls import path
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    path(route='', view=views.CourseListView.as_view(), name='index'),
    path(route='register/', view=views.registration_request, name='register'),
    path(route='login/', view=views.login_request, name='login'),
    path(route='logout/', view=views.logout_request, name='logout'),
    path(route='<int:pk>/', view=views.CourseDetailView.as_view(), name='course_details'),
    path(route='<int:course_id>/enroll/', view=views.enroll, name='enroll'),
    path(route='<int:course_id>/submit/', view=views.submit, name='submit'),
    path(
        route='<int:course_id>/submission/<int:submission_id>/result/',
        view=views.show_exam_result,
        name='show_exam_result'
    ),
]
