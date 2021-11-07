from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('projects/', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),
    path('create-project/', views.createProject, name="create-form"),
    path('update-project/<str:pk>/', views.updateProject, name="update-project"),

    path('delete-project/<str:pk>/', views.deleteProject, name="delete-project"),
    # path('project2/<str:pk>', views.project2),
    # path('project3/<str:pk>', views.project3),
    # path('project4/<str:pk>', views.project4),
    # path('project5/<str:pk>', views.project5),
    # path('project6/<str:pk>', views.project6),
    # path('project7/<str:pk>', views.project7),

]
