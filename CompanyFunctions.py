import os.path
import string
import datetime
import random
import time

import requests

from Models.Company import Company

class CompanyFunctions:

    def get_company_id(self, url, token, element_id):
        headers = {"Authorization": "Bearer " + token, "Content-type": "application/json"}

        result_obj = None
        result = requests.get(f"{url}?id={element_id}", headers=headers)
        print(f"Result = {result.status_code}")
        if result.status_code == 200:
            print(f"Ok")
            result_obj = Company()
            result_obj.from_json(result.json())
        else:
            print(f"Error {result.status_code} haciendo el get al elemento {element_id}")
        return result_obj


    def get_company_code(self, url, token, element_code):
        headers = {"Authorization": "Bearer " + token, "Content-type": "application/json"}

        result_obj = None
        result = requests.get(f"{url}?code={element_code}", headers=headers)
        print(f"Result = {result.status_code}")
        if result.status_code == 200:
            print(f"Ok")
            result_obj = Company()
            result_obj.from_json(result.json())
        else:
            print(f"Error {result.status_code} haciendo el get al elemento {element_code}")
        return result_obj


    def make_post_company(self, url, token):
        result_obj = None
        headers = {"Authorization": "Bearer " + token, "Content-type": "application/json"}
        company_request = Company()

        json_to_send = company_request.to_json()
        result = requests.post(url, headers=headers, data=json_to_send)
        # print(f"{json_to_send}")

        if 200 <= result.status_code < 300:
            result_obj = Company()
            # result_obj.from_json(result.json())
            content = result.content.decode("utf-8")
            pos_start = content.index("[") + 1
            pos_end = content.index("]")
            ident = content[pos_start:pos_end]
            #print(f"Start {pos_start} and End {pos_end} and result {ident}")
            result_obj.id = ident
        else:
            print(f"Error {result.status_code} haciendo el post. Json {json_to_send}")
        return result_obj


    def update_company(self, url, token, company):
        result_obj = None
        headers = {"Authorization": "Bearer " + token, "Content-type": "application/json"}

        json_to_send = company.to_json()
        result = requests.put(url, headers=headers, data=json_to_send)

        if 200 <= result.status_code < 300:
            result_obj = company
            #result_obj.from_json(result.json())
        else:
            print(f"Error {result.status_code} haciendo el put.")
            # print(f"Error {result.status_code} haciendo el put. Json {json_to_send}")
        return result_obj


    def delete_company(self, url, token, company_id):
        result_obj = None
        headers = {"Authorization": "Bearer " + token, "Content-type": "application/json"}

        result = requests.delete(f"{url}/{company_id}", headers=headers)

        if 200 <= result.status_code < 300:
            print("Delete ok")
        else:
            print(f"Error {result.status_code} haciendo el delete.")
            # print(f"Error {result.status_code} haciendo el put. Json {json_to_send}")
