from django.urls import path
from . import views

app_name = 'food' #namespace {put the namespace in the dynamic url in html templte}
urlpatterns = [
    path('', views.mainpage, name = 'mainpage'),
    
    # Food list page
    # path('food/', views.index, name='index'), # url for function based view 
    path('food/', views.Index_ClassBased.as_view(), name='index'), # url for class based view
    
    # Food details page
    # path('food/<item_id>/', views.details, name = 'details'), # url for function based view 
    path('food/<int:pk>/', views.Detail_ClassBased.as_view(), name = 'details'), # url for Class based view 
    
    # Add food page
    # path('food/add', views.add_item, name='addItem'), # url for function based view 
    path('food/add', views.CreateItem.as_view(), name='addItem'), # url for class based view 
    
    path('food/update/<id>', views.update_item, name= 'update_item'),
    path('food/delete/<id>', views.delete_item, name = 'delete_item'),
]
