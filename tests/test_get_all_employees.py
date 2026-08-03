
from api.employee_api import EmployeeAPI


def test_get_all_employees(request_context):

    employee = EmployeeAPI(request_context)

    response = employee.get_all_employees()

    assert response.status == 200

    body = response.json()

    assert body['status']=='success'

    assert len(body['data'])> 0

    # print(response.status)
    # print(response.headers)
    # print(response.text())

    # body = response.json()
    # #
    # assert body["status"] == "success"
    # #
    # assert len(body["data"]) > 0