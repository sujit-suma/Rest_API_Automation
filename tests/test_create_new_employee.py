from api.base_api import BaseAPI
from api.employee_api import EmployeeAPI
from config.test_data import CREATE_EMPLOYEE_PAYLOAD


def test_create_new_employee(request_context):

    employee = EmployeeAPI(request_context)
    response = employee.create_employee(CREATE_EMPLOYEE_PAYLOAD)
    assert response.status == 200

    body = response.json()
    print(body)

    assert body['status'] == 'success'
    assert body['data']['name'] == CREATE_EMPLOYEE_PAYLOAD['name']