from django.conf.urls import url, include
from webapp import views


urlpatterns = [
    # url(r'^allsubmissions/(?P<user_id>[A-Za-z0-9_.-]+)/$', views.AllTestSubmissions.as_view()),
    url(r'^streak/(?P<student_id>[A-Za-z0-9_.-]+)/$', views.streak.as_view(), name='streak'),
]
