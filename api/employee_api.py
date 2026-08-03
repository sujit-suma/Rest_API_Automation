from api.base_api import BaseAPI

class EmployeeAPI(BaseAPI):

    def get_all_employees(self):
        return self.get("employees")


    def get_employee(self, emp_id):
        return self.get(f"employee/{emp_id}")


    def create_employee(self, payload):
        return self.post(
            "create",
            payload
        )


    def update_employee(self, emp_id, payload):
        return self.put(
            f"update/{emp_id}",
            payload
        )


    def delete_employee(self, emp_id):
        return self.delete(f"delete/{emp_id}")