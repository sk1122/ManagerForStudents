from django.urls import path
from . import views


app_name = "ExpenseManager"

urlpatterns = [
	path('', views.index, name="Home"),
	
	# API ROUTES

	#path('api/v1/post', views.postData, name="postData"),
	#path('api/v1/get', views.getData, name="getData"),
	#path('api/v1/update', views.updateData, name="updateData"),
	#path('api/v1/delete', views.deleteData, name="deleteData"),

	path('api/v2/post', views.getPost.as_view(), name="post"),
	path('api/v2/delete/<int:id>', views.updateDelete.as_view(), name="delete")

]