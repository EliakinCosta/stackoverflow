from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django_tables2 import RequestConfig
from django_tables2.export import TableExport

from .models import Employee
from .filters import EmployeeFilter
from .tables import EmployeeTable


@login_required()
def employees(request):
    filter = EmployeeFilter(request.GET, queryset=Employee.objects.all())
    table = EmployeeTable(filter.qs)
    RequestConfig(request).configure(table)

    export_format = request.GET.get("_export", None)

    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response("table.{}".format("csv", "xlsx"))

    return render(request, "employees.html", {
        "table": table,
        "filter": filter
    })
