import vk
import os
import json


session = vk.Session(access_token='')
vk_api = vk.API(session)
obj = vk_api.wall.search(owner_id=-34215577, offset=100, owners_only=True, count=100, query='#Подслушано_БЕСИТ@overhear', version='5.69')
print(obj[0])
#print(len(obj))