from mcp.server.fastmcp import FastMCP
from typing import List, Dict, Any
import httpx
from dotenv import load_dotenv
import os
load_dotenv()

mcp = FastMCP(
    name="QH-OKR-MCP-Server-standalone",
    host="0.0.0.0",
    port=9001
)
OKR_SERVER_URL = os.getenv("OKR_URL")

@mcp.tool()
async def okr_login(
    email: str,
    password: str,
):
    """_summary_
    User login to the OKR system.
    This function allows a user to log in to the OKR system using their email and password.
    It returns a token and user metadata  that includes user_id role_id which can be used for subsequent requests to the system.
    Args:
        email (str): Email address of the user
        password (str): Password of the user
        
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{OKR_SERVER_URL}/login",
            json={
                "email": email,
                "password": password
            }
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Login failed: {response.text}")

@mcp.tool()
async def create_employee(
    name: str,
    email: str,
    password: str,
    role_id: int,
    department_id: int,
    joined_date: str,
):
    """_summary_
    Create a new employee in the OKR system.
    This function allows an admin to create a new employee in the OKR system.
    It requires the employee's name, email, password, role_id, department_id, and joined_date.
    It returns the created employee's metadata.

    Args:
        name (str): name of the employee
        email (str): _email of the employee
        password (str): _password of the employee
        role_id (int): _role_id of the employee
        department_id (int): _department_id of the employee
        joined_date (str): _joined_date of the employee
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{OKR_SERVER_URL}/employees/",
            json={
                "name": name,
                "email": email,
                "password": password,
                "role_id": role_id,
                "department_id": department_id,
                "joined_date": joined_date
            }
        )
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Create employee failed: {response.text}")

@mcp.tool()
async def get_specific_employee_details(
    employee_id: int,
):
    """_summary_
    Get specific employee details.
    This function allows an admin to get specific employee details using their employee_id.
    It returns the employee's metadata.

    Args:
        employee_id (int): _employee_id of the employee
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{OKR_SERVER_URL}/employees/{employee_id}"
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Get employee details failed: {response.text}")
@mcp.tool()
async def update_employee(
    employee_id: int,
    password: str,
    name: str
):
    """_summary_
    Update employee details.
    This function allows an admin to update employee details using their employee_id.
    It requires the employee's name, email, password, role_id, department_id, and joined_date.
    It returns the updated employee's metadata.

    Args:
        employee_id (int): _employee_id of the employee
        name (str): _name of the employee
        password (str): _password of the employee
    """
    async with httpx.AsyncClient() as client:
        response = await client.put(
            f"{OKR_SERVER_URL}/employees/{employee_id}",
            json={
                "name": name,
                "password": password
            }
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Update employee failed: {response.text}")

@mcp.tool()
async def delete_employee(
    employee_id: int,
):
    """_summary_
    Delete an employee.
    This function allows an admin to delete an employee using their employee_id.
    It returns a success message.

    Args:
        employee_id (int): _employee_id of the employee
    """
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            f"{OKR_SERVER_URL}/employees/{employee_id}"
        )
        if response.status_code == 204:
            return {"message": "Employee deleted successfully"}
        else:
            raise Exception(f"Delete employee failed: {response.text}")
@mcp.tool()
async def create_department(
    name: str,
):
    """_summary_
    Create a new department in the OKR system.
    This function allows an admin to create a new department in the OKR system.
    It requires the department's name.
    It returns the created department's metadata.

    Args:
        name (str): _name of the department
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{OKR_SERVER_URL}/departments/",
            json={
                "name": name
            }
        )
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Create department failed: {response.text}")
@mcp.tool()
async def create_role(
    name: str,
):
    """_summary_
    Create a new role in the OKR system.
    This function allows an admin to create a new role in the OKR system.
    It requires the role's name.
    It returns the created role's metadata.

    Args:
        name (str): _name of the role
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{OKR_SERVER_URL}/roles/",
            json={
                "name": name
            }
        )
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Create role failed: {response.text}")
        
@mcp.tool()
async def create_objectives(
    title: str,
    description: str,
    employee_id: int,
    start_date: str,
    end_date: str,
):
    """_summary_
    Create a new objective in the OKR system.
    This function allows an admin to create a new objective in the OKR system.
    It requires the objective's title, description, employee_id, start_date, and end_date.
    It returns the created objective's metadata.

    Args:
        title (str): _title of the objective
        description (str): _description of the objective
        employee_id (int): _employee_id of the objective
        start_date (str): _start_date of the objective
        end_date (str): _end_date of the objective
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{OKR_SERVER_URL}/objectives/",
            json={
                "title": title,
                "description": description,
                "employee_id": employee_id,
                "start_date": start_date,
                "end_date": end_date
            }
        )
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Create objective failed: {response.text}")
@mcp.tool()
async def update_objectives(
    objective_id: int,
    title: str,
    description:str,
    employee_id: int,
    start_date: str,
    end_date: str,
):
    """_summary_
    Update an objective in the OKR system.
    This function allows an admin to update an objective in the OKR system.
    It requires the objective's title, description, employee_id, start_date, and end_date.
    args:
        objective_id (int): _objective_id of the objective
        title (str): _title of the objective
        description (str): _description of the objective
        employee_id (int): _employee_id of the objective
        start_date (str): _start_date of the objective
        end_date (str): _end_date of the objective
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{OKR_SERVER_URL}/objectives/{objective_id}",
            json={
                "title": title,
                "description": description,
                "employee_id": employee_id,
                "start_date": start_date,
                "end_date": end_date
            }
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Update objective failed: {response.text}")
@mcp.tool()
async def delete_objectives(
    employee_id: int,
):
    """_summary_
    Delete an objective in the OKR system.
    This function allows an admin to delete an objective in the OKR system.
    It requires the objective's employee_id.
    It returns a success message.

    Args:
        employee_id (int): _employee_id of the objective
    """
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            f"{OKR_SERVER_URL}/objectives/{employee_id}"
        )
        if response.status_code == 204:
            return {"message": "Objective deleted successfully"}
        else:
            raise Exception(f"Delete objective failed: {response.text}")

@mcp.tool()
async def create_key_result(
    objective_id: int,
    title: str,
    target_value: int,
    current_value: int,
    progress: int,
    
):
    """_summary_
    Create a new key result in the OKR system.
    This function allows an admin to create a new key result in the OKR system.
    It requires the key result's objective_id, title, target_value, current_value, and progress.
    It returns the created key result's metadata.

    Args:
        objective_id (int): _objective_id of the key result
        title (str): _title of the key result
        target_value (int): _target_value of the key result
        current_value (int): _current_value of the key result
        progress (int): _progress of the key result
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{OKR_SERVER_URL}/key_results/",
            json={
                "objective_id": objective_id,
                "title": title,
                "target_value": target_value,
                "current_value": current_value,
                "progress": progress
            }
        )
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Create key result failed: {response.text}")
@mcp.tool()
async def update_key_result(
    key_result_id: int,
    title: str,
    target_value: int,
    current_value: int,
    progress: int,
):
    """_summary_
    Update a key result in the OKR system.
    This function allows an admin to update a key result in the OKR system.
    It requires the key result's objective_id, title, target_value, current_value, and progress.
    args:
        key_result_id (int): _key_result_id of the key result
        title (str): _title of the key result
        target_value (int): _target_value of the key result
        current_value (int): _current_value of the key result
        progress (int): _progress of the key result
    """
    async with httpx.AsyncClient() as client:
        response = await client.put(
            f"{OKR_SERVER_URL}/key_results/{key_result_id}",
            json={
                "title": title,
                "target_value": target_value,
                "current_value": current_value,
                "progress": progress
            }
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Update key result failed: {response.text}")
@mcp.tool()
async def create_time_sheet(
    employee_id: int,
    work_date: str,
    hours_worked: int,
    discription: str
):
    """_summary_
    Create a new time sheet in the OKR system.
    This function allows an admin to create a new time sheet in the OKR system.
    It requires the time sheet's employee_id, work_date, hours_worked, and discription.
    args:
        employee_id (int): _employee_id of the time sheet
        work_date (str): _work_date of the time sheet
        hours_worked (int): _hours_worked of the time sheet
        discription (str): _discription of the time sheet
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{OKR_SERVER_URL}/time_sheets/",
            json={
                "employee_id": employee_id,
                "work_date": work_date,
                "hours_worked": hours_worked,
                "discription": discription
            }
        )
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Create time sheet failed: {response.text}")
@mcp.tool()
async def get_a_specific_user_timesheet(
    employee_id: int,
):
    """_summary_
    Get a specific user's time sheet.
    This function allows an admin to get a specific user's time sheet using their employee_id.
    It returns the user's time sheet metadata.

    Args:
        employee_id (int): _employee_id of the user
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{OKR_SERVER_URL}/time_sheets/{employee_id}"
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Get time sheet failed: {response.text}")
@mcp.tool()
async def create_leave_type(
    name: str,
    max_days_per_year: int
):
    """_summary_
    Create a new leave type in the OKR system.
    This function allows an admin to create a new leave type in the OKR system.
    It requires the leave type's name and max_days_per_year.
    It returns the created leave type's metadata.

    Args:
        name (str): _name of the leave type
        max_days_per_year (int): _max_days_per_year of the leave type
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{OKR_SERVER_URL}/leave_types/",
            json={
                "name": name,
                "max_days_per_year": max_days_per_year
            }
        )
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Create leave type failed: {response.text}")
@mcp.tool()
async def create_leave(
    employee_id: int,
    leave_date: int,
    leave_type_id: str,
    reason: str
):
    """_summary_
    Create a new leave in the OKR system.
    This function allows an admin to create a new leave in the OKR system.
    It requires the leave's employee_id, leave_date, leave_type_id, and reason.
    It returns the created leave's metadata.

    Args:
        employee_id (int): _employee_id of the leave
        leave_date (int): _leave_date of the leave
        leave_type_id (str): _leave_type_id of the leave
        reason (str): _reason of the leave
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{OKR_SERVER_URL}/leaves/",
            json={
                "employee_id": employee_id,
                "leave_date": leave_date,
                "leave_type_id": leave_type_id,
                "reason": reason
            }
        )
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Create leave failed: {response.text}")
@mcp.tool()
async def update_leave(
    leave_id: int,
    status: str,
    approved_by: int,
):
    """_summary_
    Update a leave in the OKR system.
    This function allows an admin to update a leave in the OKR system.
    args:
        leave_id (int): _leave_id of the leave
        status (str): _status of the leave
        approved_by (int): _approved_by of the leave
    """
    async with httpx.AsyncClient() as client:
        response = await client.put(
            f"{OKR_SERVER_URL}/leaves/{leave_id}",
            json={
                "status": status,
                "approved_by": approved_by
            }
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Update leave failed: {response.text}")
@mcp.tool()
async def get_a_specific_user_leave(
    employee_id: int,
):
    """_summary_
    Get a specific user's leave.
    This function allows an admin to get a specific user's leave using their employee_id.
    It returns the user's leave metadata.

    Args:
        employee_id (int): _employee_id of the user
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{OKR_SERVER_URL}/leaves/{employee_id}"
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Get leave failed: {response.text}")
@mcp.resource("leaves://leaveslist")
async def get_leaves():
    """_summary_
    Get all leaves metadata.
    This function allows an admin to get all leaves metadata.
    It returns a list of leave metadata.

    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{OKR_SERVER_URL}/leaves/"
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Get leaves failed: {response.text}")
@mcp.tool()
async def create_project(
    name: str,
    description: str,
    department_id: int,
    start_date: str,
    end_date: str,
):
    """_summary_
    Create a new project in the OKR system.
    This function allows an admin to create a new project in the OKR system.
    It requires the project's name, description, department_id, start_date, and end_date.
    It returns the created project's metadata.

    Args:
        name (str): _name of the project
        description (str): _description of the project
        department_id (int): _department_id of the project
        start_date (str): _start_date of the project
        end_date (str): _end_date of the project
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{OKR_SERVER_URL}/projects/",
            json={
                "name": name,
                "description": description,
                "department_id": department_id,
                "start_date": start_date,
                "end_date": end_date
            }
        )
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Create project failed: {response.text}")
@mcp.tool()
async def get_a_specific_project_details(
    project_id: int,
):
    """_summary_
    Get a specific project's details.
    This function allows an admin to get a specific project's details using their project_id.
    It returns the project's metadata.

    Args:
        project_id (int): _project_id of the project
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{OKR_SERVER_URL}/projects/{project_id}"
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Get project details failed: {response.text}")
@mcp.tool()
async def update_project(
    project_id: int,
    name: str,
    description: str,
    department_id: int,
    start_date: str,
    end_date: str,
    status: str):
    """_summary_
    Update a project in the OKR system.
    This function allows an admin to update a project in the OKR system.
    It requires the project's name, description, department_id, start_date, end_date, and status.
    args:
        project_id (int): _project_id of the project
        name (str): _name of the project
        description (str): _description of the project
        department_id (int): _department_id of the project
        start_date (str): _start_date of the project
        end_date (str): _end_date of the project
        status (str): _status of the project
    """
    async with httpx.AsyncClient() as client:
        response = await client.put(
            f"{OKR_SERVER_URL}/projects/{project_id}",
            json={
                "name": name,
                "description": description,
                "department_id": department_id,
                "start_date": start_date,
                "end_date": end_date,
                "status": status
            }
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Update project failed: {response.text}")
@mcp.tool()
async def delete_project(
    project_id: int,
):
    """_summary_
    Delete a project in the OKR system.
    This function allows an admin to delete a project in the OKR system.
    It requires the project's project_id.
    It returns a success message.

    Args:
        project_id (int): _project_id of the project
    """
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            f"{OKR_SERVER_URL}/projects/{project_id}"
        )
        if response.status_code == 204:
            return {"message": "Project deleted successfully"}
        else:
            raise Exception(f"Delete project failed: {response.text}")
@mcp.tool()
async def create_project_allocations(
    project_id: int,
    employee_id: int,
    role_in_project: str,
):
    """_summary_
    Create a new project allocation in the OKR system.
    This function allows an admin to create a new project allocation in the OKR system.
    It requires the project's project_id, employee_id, and role_in_project.
    It returns the created project allocation's metadata.

    Args:
        project_id (int): _project_id of the project allocation
        employee_id (int): _employee_id of the project allocation
        role_in_project (str): _role_in_project of the project allocation
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{OKR_SERVER_URL}/project_allocations/",
            json={
                "project_id": project_id,
                "employee_id": employee_id,
                "role_in_project": role_in_project
            }
        )
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Create project allocation failed: {response.text}")
@mcp.tool()
async def update_project_allocations(
    status: str,
    project_id: int,
    employee_id: int,
):
    """_summary_
    Update a project allocation in the OKR system.
    This function allows an admin to update a project allocation in the OKR system.
    It requires the project's project_id, employee_id, and status.
    args:
        status (str): _status of the project allocation
        project_id (int): _project_id of the project allocation
        employee_id (int): _employee_id of the project allocation
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{OKR_SERVER_URL}/project_allocations/{status}",
            json={
                "project_id": project_id,
                "employee_id": employee_id
            }
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Update project allocation failed: {response.text}")
@mcp.tool()
async def list_of_all_employess_in_a_project(
    project_id: int,
):
    """_summary_
    Get a list of all employees in a project.
    This function allows an admin to get a list of all employees in a project using their project_id.
    It returns the project's employee metadata.

    Args:
        project_id (int): _project_id of the project
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{OKR_SERVER_URL}/project_allocations/project/{project_id}"
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Get project allocation failed: {response.text}")
        
@mcp.tool()
async def list_all_project_of_a_employee(
    employee_id: int,
):
    """_summary_
    Get a list of all projects of an employee.
    This function allows an admin to get a list of all projects of an employee using their employee_id.
    It returns the employee's project metadata.

    Args:
        employee_id (int): _employee_id of the employee
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{OKR_SERVER_URL}/project_allocations/employee/{employee_id}"
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Get project allocation failed: {response.text}"
)
@mcp.resource("projects://projectAllocationlist")
async def get_project_allocations():
    """_summary_
    Get all project allocations metadata.
    This function allows an admin to get all project allocations metadata.
    It returns a list of project allocation metadata.

    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{OKR_SERVER_URL}/project_allocations/"
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Get project allocations failed: {response.text}")
    
@mcp.resource("projects://projectslist")
async def get_projects():
    """_summary_
    Get all projects metadata.
    This function allows an admin to get all projects metadata.
    It returns a list of project metadata.

    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{OKR_SERVER_URL}/projects/"
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Get projects failed: {response.text}")
@mcp.resource("leaveTypes://leavetypeslist")
async def get_leave_types():
    """_summary_
    Get all leave types metadata.
    This function allows an admin to get all leave types metadata.
    It returns a list of leave type metadata.

    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{OKR_SERVER_URL}/leave_types/"
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Get leave types failed: {response.text}")


@mcp.resource("timesheets://timesheetslist")
async def get_timesheets():
    """_summary_
    Get all time sheets metadata.
    This function allows an admin to get all time sheets metadata.
    It returns a list of time sheet metadata.

    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{OKR_SERVER_URL}/time_sheets/"
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Get time sheets failed: {response.text}")

@mcp.resource("objectives://objectiveslist")
async def get_objectives():
    """_summary_
    Get all objectives metadata.
    This function allows an admin to get all objectives metadata.
    It returns a list of objective metadata.

    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{OKR_SERVER_URL}/objectives/"
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Get objectives failed: {response.text}")

@mcp.resource("employees://employeeslist")
async def get_employees():
    """_summary_
    Get all employees metadata.
    This function allows an admin to get all employees metadata.
    It returns a list of employee metadata.

    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{OKR_SERVER_URL}/employees/"
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Get employees failed: {response.text}")

@mcp.resource("roles://roleslist")
async def get_roles():
    """_summary_
    Get all roles metadata.
    This function allows an admin to get all roles metadata.
    It returns a list of role metadata.

    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{OKR_SERVER_URL}/roles/"
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Get roles failed: {response.text}")
@mcp.resource("departments://departmentslist")
async def get_departments():
    """_summary_
    Get all departments metadata.
    This function allows an admin to get all departments metadata.
    It returns a list of department metadata.

    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{OKR_SERVER_URL}/departments/"
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Get departments failed: {response.text}")
if __name__ == "__main__":
    transport = "sse"
    if transport == "stdio":
        print("Starting MCP server with stdio transport...")
        mcp.run(transport="stdio")
    elif transport == "sse":
        print("Starting MCP server with SSE transport...")
        mcp.run(transport="sse")
    else:
        raise ValueError("Unsupported transport type. Use 'stdio' or 'sse'.")
       