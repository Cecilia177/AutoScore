"""AutoScore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as drf_views
from rest_framework_jwt import views as jwt_views
from apps.exams import views as exams_views
from apps.questions import views as questions_views
from apps.users import views as users_views
from apps.students import views as students_views
# from apps.answers import views as answers_views


router = DefaultRouter()
router.register(r'exams', exams_views.ExamsListViewSet)
router.register(r'questions', questions_views.QuestionsViewSet)
# router.register(r'references', questions_views.ReferenceViewSet)
router.register(r'users', users_views.UserViewSet)
router.register(r'students', students_views.StudentViewSet)
router.register(r'autoscoring', students_views.ScoringViewSet)
router.register(r'answers', students_views.AnswerViewSet)
router.register(r'scores', students_views.ScoresViewSet)

# router_front = DefaultRouter()
# router_front.register(r'login', users_views.LoginViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('docs/', include_docs_urls(title="AutoScore")),

    path('api/', include(router.urls)),
    # path('api/', include(router_front.urls))
    path('api-token-auth/', drf_views.obtain_auth_token),

    path('api/login/', jwt_views.obtain_jwt_token),
]
