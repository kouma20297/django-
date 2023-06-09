from django.urls import path

from . import views

from polls.views import frontpage

from django.contrib import admin
urlpatterns = [
    path("", views.index, name="index"),
]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]



from django.urls import path

from . import views


urlpatterns = [
    # ex: /polls/
    path('',frontpage),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]