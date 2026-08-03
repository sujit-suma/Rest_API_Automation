from api.employee_api import EmployeeAPI
from config.test_data import DELETE_EMPLOYEE_ID


def test_delete_employee(request_context):
    emp = EmployeeAPI(request_context)
    response = emp.delete_employee(DELETE_EMPLOYEE_ID)

    assert response.status ==  200

    body = response.json()
    print(body)
    assert body["employee_id"] == DELETE_EMPLOYEE_ID


