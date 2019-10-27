import http.client
import json
import os
import ssl

conn = http.client.HTTPSConnection("api.hypr.cl", context=ssl._create_unverified_context())

headers = {
    'x-api-key': os.getenv('HYPR_API_KEY'),
    'command': "list",
    'time_start': "2019-08-01T12-00-00Z",
    'time_stop': "2019-08-01T12-01-00Z",
    'Accept': "*/*", 'Cache-Control': "no-cache", 'Host': "api.hypr.cl", 'Accept-Encoding': "gzip, deflate",
    'Content-Length': "0",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

conn.request("POST", "/station/", headers=headers)
res = conn.getresponse()
data = res.read()

nice_json_res = json.loads(data.decode("utf-8"))

all_stations = nice_json_res['list']

text_file = open("stations.json", "w")
text_file.write(json.dumps(all_stations))
text_file.close()

print("Done")
