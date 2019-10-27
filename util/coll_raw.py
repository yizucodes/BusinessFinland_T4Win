import datetime
import os

import requests

url = "https://api.hypr.cl/raw/"

headers = {
    'x-api-key': os.getenv('HYPR_API_KEY'),
    'command': "list",
    'time_start': "2019-08-01T00:00:00Z", 'time_stop': "2019-08-01T00:00:00Z", 'Accept': "*/*",
    'Cache-Control': "no-cache", 'Host': "api.hypr.cl", 'Accept-Encoding': "gzip, deflate", 'Content-Length': "0",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}


def get_datetime_str(dt):
    return dt.replace(microsecond=0).isoformat() + "Z"


# EXAMPLE: get_heat_map(datetime.datetime(2019, 8, 1, 0, 58, 0), datetime.datetime(2019, 8, 1, 0, 58, 30))
def get_raw(time_start, time_stop):
    headers['time_start'] = get_datetime_str(time_start)
    headers['time_stop'] = get_datetime_str(time_stop)
    response = requests.request("POST", url, headers=headers)
    if response.status_code != 200:
        print(f"Error {response.status_code} for {time_start} - {time_stop} interval")
    return response.text


def sample_day_per_minute(year, month, day, sec_per_minute=3, sec=0, output_to_multiple_files=True):
    cur_time = datetime.datetime(year, month, day, 0, 0, sec)
    day_end = datetime.datetime(year, month, day, 23, 59, sec)

    while cur_time <= day_end:
        time_stop = cur_time + datetime.timedelta(seconds=sec_per_minute)
        result = get_raw(cur_time, time_stop)
        if output_to_multiple_files:
            filename = cur_time.strftime('%H%M')
            text_file = open(filename + ".json", "w")
            text_file.write(result)
            text_file.close()
        cur_time += datetime.timedelta(minutes=1)

    print("THE END")


if __name__ == "__main__":
    sample_day_per_minute(2019, 8, 1)
