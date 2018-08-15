import requests
import os
r = requests.get('rapi.rapidtrade.biz/get/swf/failed/Inbound', auth=('DEMO', 'DEMO'))
print(r.json())

