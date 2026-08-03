from urllib import response

from api.employee_api import EmployeeAPI
from config.test_data import UPDATE_EMPLOYEE_ID, UPDATE_EMPLOYEE_PAYLOAD


def test_update_employee(request_context):
    employee = EmployeeAPI(request_context)
    response = employee.put(UPDATE_EMPLOYEE_ID,UPDATE_EMPLOYEE_PAYLOAD)

    assert response.status == 200
    body = response.json()

    assert body['status'] == 'success'
