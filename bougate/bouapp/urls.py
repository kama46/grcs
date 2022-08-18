from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # path form registration
    path('badge', views.badge, name='badge'),
    path('register_item', views.register_item, name='register_item'),
    path('person', views.person, name='person'),
    # path for view data in database
    path('view_person', views.view_person, name='view_person'),
    path('view_items', views.view_items, name='view_items'),
    path('view_badge', views.view_badge, name='view_badge'),
    # Path for updating data in database
    path('update_person/<int:pk>/', views.update_person, name='update_person'),
    path('update_item/<int:pk>/', views.update_item, name='update_item'),
    path('update_badgein_nonstaff/<int:pk>/', views.update_badgein_nonstaff, name='update_badgein_nonstaff'),
    path('update_badge_out/<int:pk>/', views.update_badge_out, name='update_badge_out'),
    # Path for Deleting data in database
    path('delete_badge/<int:pk>/', views.delete_badge, name='delete_badge'),
    path('delete_bin_nonstaff/<int:pk>/', views.delete_bin_nonstaff, name='delete_bin_nonstaff'),
    path('delete_item/<int:pk>/', views.delete_item, name='delete_item'),
    # Path for Searching data in database
    path('search_person', views.person_search_bar, name='search_person'),
    path('search_item', views.item_search_bar, name='search_item'),
    path('search_badge', views.badge_search_bar, name='search_badge'),
    path('badgeIn', views.badgeIn, name='badgeIn'),
    path('badgeout_staff', views.badgeout_staff, name='badgeout_staff'),
    path('badgeIn_nonstaff', views.badgeIn_nonstaff, name='badgeIn_nonstaff'),
    path('badgeout_nonstaff', views.badgeout_nonstaff, name='badgeout_nonstaff'),
    path('badgedoutnonstaff', views.badgedoutnonstaff, name='badgedoutnonstaff'),
    path('badgedoutstaff', views.badgedoutstaff, name='badgedoutstaff'),
    path('badgedinnonstaff', views.badgedinnonstaff, name='badgedinnonstaff'),
    path('badgedinstaff', views.badgedinstaff, name='badgedinstaff'),
    # path('connect', views.connect, name='connect'),
    


]
