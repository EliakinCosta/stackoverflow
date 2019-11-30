from .models import Employee
import django_filters


class EmployeeFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Employee
        fields = ["emp_id", "first_name", "last_name", "job_title", "dept_name", "hire_date"]
