from django_tables2 import SingleTableMixin
from .models import Employee
from .tables import EmployeeTable
from django_filters.views import FilterView


class Employees(SingleTableMixin, FilterView):
    model = Employee
    table_class = EmployeeTable
    template_name = 'employees.html'
    filterset_fields = ['first_name']
