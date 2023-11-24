import os.path
import string
import datetime
import random
import time
import psycopg2

import requests

from Models.Company import Company
from Models.User import User
from Models.Project import Project
from Models.Dedication import Dedication
from Models.UserLogin import UserLogin
from CompanyFunctions import CompanyFunctions
from ProjectFunctions import ProjectFunctions
from UserFunctions import UserFunctions
from DedicationFunctions import DedicationFunctions


def execute_tests_company(url, urlid, urlcode, token):

    print(f"Ejecutando execute_tests_company")
    companyFunctions = CompanyFunctions()

    # Vamos a hacer un post para añadir uno
    element_created = companyFunctions.make_post_company(url, token, None)
    assert element_created is not None
    print(f"Se ha creado el elemento con id {element_created.id}")

    # Vamos a hacer un put con el objeto modificado
    element_created.name = "namecito"
    put_result = companyFunctions.update_company(url, token, element_created)
    assert put_result is not None

    # Vamos a hacer un get por ID a ese elemento
    specific_element = companyFunctions.get_company_id(urlid, token, element_created.id)
    assert specific_element.name == "namecito"
    print(f"Elemento {specific_element.id} devuelto correctamente. "
          f"name = {specific_element.name}")

    # Vamos a borrar el elemento modificado
    companyFunctions.delete_company(url, token, specific_element.id)

    # Vamos a pedirlo de nuevo pero por code
    specific_element = companyFunctions.get_company_code(urlcode, token, element_created.code)
    assert specific_element is None
    print(f"Elemento borrado satisfactoriamente")
    print(f"Todas las pruebas finalizadas con éxito")


def execute_tests_project(url, urlid, urlcode, token):

    print(f"Ejecutando execute_tests_project")
    projectFunctions = ProjectFunctions()

    # Vamos a hacer un post para añadir uno
    element_created = projectFunctions.make_post_project(url, token, None)
    assert element_created is not None
    print(f"Se ha creado el elemento con id {element_created.id}")

    # Vamos a hacer un put con el objeto modificado
    element_created.description = "namecito"
    put_result = projectFunctions.update_project(url, token, element_created)
    assert put_result is not None

    # Vamos a hacer un get por ID a ese elemento
    specific_element = projectFunctions.get_project_id(urlid, token, element_created.id)
    assert specific_element.description == "namecito"
    print(f"Elemento {specific_element.id} devuelto correctamente. "
          f"description = {specific_element.description}")

    # Vamos a borrar el elemento modificado
    projectFunctions.delete_project(url, token, specific_element.id)

    # Vamos a pedirlo de nuevo pero por code
    specific_element = projectFunctions.get_project_code(urlcode, token, element_created.code)
    assert specific_element is None
    print(f"Elemento borrado satisfactoriamente")
    print(f"Todas las pruebas finalizadas con éxito")

def execute_tests_user(url, urlid, urlcode, token):

    print(f"Ejecutando execute_tests_user")
    userFunctions = UserFunctions()

    # Vamos a hacer un post para añadir uno
    element_created = userFunctions.make_post_user(url, token, None)
    assert element_created is not None
    print(f"Se ha creado el elemento con id {element_created.id}")

    # Vamos a hacer un put con el objeto modificado
    element_created.name = "namecito"
    put_result = userFunctions.update_user(url, token, element_created)
    assert put_result is not None

    # Vamos a hacer un get por ID a ese elemento
    specific_element = userFunctions.get_user_id(urlid, token, element_created.id)
    assert specific_element.name == "namecito"
    print(f"Elemento {specific_element.id} devuelto correctamente. "
          f"name = {specific_element.name}")

    # Vamos a borrar el elemento modificado
    userFunctions.delete_user(url, token, specific_element.id)

    # Vamos a pedirlo de nuevo pero por code
    specific_element = userFunctions.get_user_code(urlcode, token, element_created.code)
    assert specific_element is None
    print(f"Elemento borrado satisfactoriamente")
    print(f"Todas las pruebas finalizadas con éxito")

def execute_tests_dedication(url, urlid, urlcode, token):

    print(f"Ejecutando execute_tests_dedication")
    dedicationFunctions = DedicationFunctions()

    # Vamos a hacer un post para añadir uno
    element_created = dedicationFunctions.make_post_dedication(url, token)
    assert element_created is not None
    print(f"Se ha creado el elemento con id {element_created.id}")

    # Vamos a hacer un put con el objeto modificado
    element_created.description = "namecito"
    put_result = dedicationFunctions.update_dedication(url, token, element_created)
    assert put_result is not None

    # Vamos a hacer un get por ID a ese elemento
    specific_element = dedicationFunctions.get_dedication_id(urlid, token, element_created.id)
    assert specific_element.description == "namecito"
    print(f"Elemento {specific_element.id} devuelto correctamente. "
          f"description = {specific_element.description}")

    # Vamos a borrar el elemento modificado
    dedicationFunctions.delete_dedication(url, token, specific_element.id)

    # Vamos a pedirlo de nuevo pero por code
    specific_element = dedicationFunctions.get_dedication_code(urlcode, token, element_created.projectCode, element_created.user)
    assert specific_element is None
    print(f"Elemento borrado satisfactoriamente")
    print(f"Todas las pruebas finalizadas con éxito")    


def get_token(email, password, auth_url, print_token=True):

    #headers = {"Authorization": "Basic " + token, "Content-type": "application/json"}
    headers = {"Content-type": "application/json"}
    
    userlogin = UserLogin()
    userlogin.email = email
    userlogin.password = password
    userlogin_send = userlogin.to_json()

    result = requests.post(auth_url, data=userlogin_send, headers=headers)

    if result.status_code == 200:
        token = result.json()['token']
        if print_token:
            print(f"{email} - {token}")
        return token

    print(f"Result = {result.status_code}. {result.content}")

    return None

def create_data():

    #Establishing the connection
    conn = psycopg2.connect(
    database="hermes", user='docker', password='docker', host='127.0.0.1', port= '5432'
    )
    #Setting auto commit false
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Preparing SQL queries to INSERT a record into the database.
    cursor.execute('''INSERT INTO public.company(active, code, "name")
     VALUES(true, '11112222A', 'TEST')''')

    cursor.execute('''INSERT INTO public.user_data(active, "admin", code, "name", "password", "email", company_id)
     VALUES(true, true, '75763090D', 'Fran', '$2a$12$2qJkjx/w0Kq1zBib6zLa9uqKuc.76oCODmStIlis/HaGZrXQl7AX.', 'fj@gmail.com', 1)''')

    cursor.execute('''INSERT INTO public.project(active, code, "description", "name", company_id)
     VALUES(true, '222', 'la descripcion', 'proyecto', 1)''')

    # Commit your changes in the database
    conn.commit()
    print("Records inserted........")

    # Closing the connection
    conn.close()


def delete_data():

    #Establishing the connection
    conn = psycopg2.connect(
    database="hermes", user='docker', password='docker', host='127.0.0.1', port= '5432'
    )
    #Setting auto commit false
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Preparing SQL queries to DELETE a record into the database
    cursor.execute('''DELETE FROM public.project''')

    cursor.execute('''DELETE FROM public.user_data''')

    cursor.execute('''DELETE FROM public.company''')     

    # Commit your changes in the database
    conn.commit()
    print("Records deleted........")

    # Closing the connection
    conn.close()    


if __name__ == '__main__':
    
    # INSERTS previos en la BD
    create_data()

    _url_auth = f"http://localhost:8080/auth/login"
    _url_company = f"http://localhost:8080/company"
    _url_company_id = f"http://localhost:8080/company/getCompanyById"
    _url_company_code = f"http://localhost:8080/company/getCompanyByCode"
    _url_project = f"http://localhost:8080/project"
    _url_project_id = f"http://localhost:8080/project/getProjectById"
    _url_project_code = f"http://localhost:8080/project/getProjectByCode"
    _url_user = f"http://localhost:8080/user"
    _url_user_id = f"http://localhost:8080/user/getUserById"
    _url_user_code = f"http://localhost:8080/user/getUserByCode"    
    _url_dedication = f"http://localhost:8080/dedication"
    _url_dedication_id = f"http://localhost:8080/dedication/getDedicationById"
    _url_dedication_code = f"http://localhost:8080/dedication/getDedicationByProjectAndUser"    

    _token = get_token("fj@gmail.com", "LAQUESEA", _url_auth, True)
    print("\r\n")
    
    execute_tests_company(_url_company, _url_company_id, _url_company_code, _token)
    print("\r\n")

    execute_tests_project(_url_project, _url_project_id, _url_project_code, _token)
    print("\r\n")

    execute_tests_user(_url_user, _url_user_id, _url_user_code, _token)
    print("\r\n")

    execute_tests_dedication(_url_dedication, _url_dedication_id, _url_dedication_code, _token)
    print("\r\n")

    delete_data()

   
