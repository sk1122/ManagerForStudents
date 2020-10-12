from django.test import TestCase

from rest_framework.test import APITestCase
from .models import Expense
from .serializers import ExpenseSerializer


class ExpenseTests(APITestCase):
	def test_can_get_expense(self):
		expense = Expense.objects.create(expense_name="College Fees", expense_money=20000)
		response = self.client.get(f'/api/v1/get/{expense.id}')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.data, ExpenseSerializer(instance=expense).data)

	def test_can_delete_expense(self):
		expense = Expense.objects.create(expense_name="College Fees", expense_money=20000)
		response = self.client.delete(f'/api/v1/delete/{expense.id}')
		self.assertEqual(response.status_code, 204)
		self.assertEqual(Expense.objects.count(), 0)

	def test_can_update_expense(self):
		expense = Expense.objects.create(expense_name="College Fees", expense_money=20000)
		response = self.client.patch(f'/api/v1/update/{expense.id}', data={"expense_name":"Tution Fees", "expense_money":4555})
		expense.refresh_from_db()
		self.assertEqual(response.status_code, 200)
		self.assertEqual(expense.expense_name, "Tution Fees")
		self.assertEqual(expense.expense_money, 4555)