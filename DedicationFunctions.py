import os.path
import string
import datetime
import random
import time

import requests

from Models.Dedication import Dedication

class DedicationFunctions:

    def get_dedication_id(self, url, token, element_id):
        headers = {"Authorization": "Bearer " + token, "Content-type": "application/json"}

        result_obj = None
        result = requests.get(f"{url}?id={element_id}", headers=headers)
        print(f"Result = {result.status_code}")
        if result.status_code == 200:
            print(f"Ok")
            result_obj = Dedication()
            result_obj.from_json(result.json())
        else:
            print(f"Error {result.status_code} haciendo el get al elemento {element_id}")
        return result_obj


    def get_dedication_code(self, url, token, element_cod_proj, element_cod_user):
        headers = {"Authorization": "Bearer " + token, "Content-type": "application/json"}

        result_list = list()

        result = requests.get(f"{url}?codProject={element_cod_proj}&codUser={element_cod_user}", headers=headers)
        print(f"Result = {result.status_code}")
        if result.status_code == 200:
            print(f"Ok")
            for dedications_json in result.json():
                dedication = Dedication()
                dedication.from_json(dedications_json)
                result_list.append(dedication)
                return result_list
        else:
            print(f"Error {result.status_code} haciendo el get al elemento {element_cod_proj} y {element_cod_user}")
        return None


    def make_post_dedication(self, url, token):
        result_obj = None
        headers = {"Authorization": "Bearer " + token, "Content-type": "application/json"}
        dedication_request = Dedication()

        json_to_send = dedication_request.to_json()
        result = requests.post(url, headers=headers, data=json_to_send)
        # print(f"{json_to_send}")

        if 200 <= result.status_code < 300:
            result_obj = Dedication()
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


    def update_dedication(self, url, token, dedication):
        result_obj = None
        headers = {"Authorization": "Bearer " + token, "Content-type": "application/json"}

        json_to_send = dedication.to_json()
        result = requests.put(url, headers=headers, data=json_to_send)

        if 200 <= result.status_code < 300:
            result_obj = dedication
            #result_obj.from_json(result.json())
        else:
            print(f"Error {result.status_code} haciendo el put.")
            # print(f"Error {result.status_code} haciendo el put. Json {json_to_send}")
        return result_obj


    def delete_dedication(self, url, token, dedication_id):
        result_obj = None
        headers = {"Authorization": "Bearer " + token, "Content-type": "application/json"}

        result = requests.delete(f"{url}/{dedication_id}", headers=headers)

        if 200 <= result.status_code < 300:
            print("Delete ok")
        else:
            print(f"Error {result.status_code} haciendo el delete.")
            # print(f"Error {result.status_code} haciendo el put. Json {json_to_send}")
