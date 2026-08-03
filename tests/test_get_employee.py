
from api.employee_api import EmployeeAPI
from config.test_data import EMPLOYEE_ID


def test_get_employees(request_context):

    employee = EmployeeAPI(request_context)

    response = employee.get_employee(EMPLOYEE_ID)

    assert response.status == 200

    body = response.json()

    assert body['status']=='success'

    assert body['data']['id'] == EMPLOYEE_ID

    print(response.status)
    print(response.text())
