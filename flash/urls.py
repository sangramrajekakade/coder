from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from flash import views
# from django.conf import settings
urlpatterns = [

    path('',views.HomePage.as_view(),name='homepage'),
    path('blog/',views.PostPage.as_view(),name='blog'),
    path('Contact/',views.Contact.as_view(),name='Contact'),
    path('detail-blog/<pk>', views.BlogDetailView.as_view(), name="detail-blog"),
    path('ProjectsPage/',views.ProjectsPage.as_view(),name='ProjectsPage'),

]
