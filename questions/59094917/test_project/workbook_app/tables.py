import django_tables2 as tables

from .models import Employee

class EmployeeTable(tables.Table):

    class Meta:
        model = Employee
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("emp_id", "first_name", "last_name", "job_title", "dept_name", "hire_date")
        export_formats = ['csv', 'xlsx']
