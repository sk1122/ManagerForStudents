from django.shortcuts import render
from rest_framework.generics import UpdateAPIView, DestroyAPIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Expense
from .serializers import ExpenseSerializer



def index(request):
	return render(request, "index.html")


@api_view(['POST'])
def postData(request):
	if request.method == "POST":
		data = {
			"expense_name": request.data.get("name"),
			"expense_money": request.data.get("money")
		}
		serializer = ExpenseSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getData(request):
	if request.method == "GET":
		expenses = Expense.objects.all()
		serializer = ExpenseSerializer(expenses, many=True)
		return Response(serializer.data)


@api_view(['GET'])
def getSpecificData(request, id):
	if request.method == "GET":
		expenses = Expense.objects.get(pk=id)
		serializer = ExpenseSerializer(expenses)
		return Response(serializer.data)


class UpdateData(UpdateAPIView):
	queryset = Expense.objects.all()
	serializer_class = ExpenseSerializer


class DeleteData(DestroyAPIView):
	queryset = Expense.objects.all()
	serializer_class = ExpenseSerializer