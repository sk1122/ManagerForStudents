from django.urls import path
from . import views


app_name = "ExpenseManager"

urlpatterns = [
	path('', views.index, name="Home"),
	
	# API ROUTES

	path('api/v1/post', views.postData, name="postData"),
	path('api/v1/get', views.getData, name="getData"),
	path('api/v1/get/<int:id>', views.getSpecificData, name="getData"),
	# path('api/v1/update/<int:id>', views.updateData, name="updateData"),
	# path('api/v1/delete/<int:id>', views.deleteData, name="deleteData"),


	path('api/v1/update/<int:pk>', views.UpdateData.as_view(), name="update"),
	path('api/v1/delete/<int:pk>', views.DeleteData.as_view(), name="delete")
]