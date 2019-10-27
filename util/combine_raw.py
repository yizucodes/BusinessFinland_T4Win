import datetime
import json


def get_all_fn_hour(hour):
    filename_list = list()
    cur_time = datetime.datetime(2019, 1, 1, hour, 0, 0)
    end_time = datetime.datetime(2019, 1, 1, hour, 59, 0)
    while cur_time < end_time:
        filename = cur_time.strftime('%H%M') + ".json"
        filename_list.append(filename)
        cur_time += datetime.timedelta(minutes=1)
    return filename_list


def combine_hour(hour) -> list:
    result = list()
    fns = get_all_fn_hour(hour)
    for fn in fns:
        with open(fn) as f:
            new_data = json.load(f)
        raw_list = new_data.get('raw') or list()
        result.extend(raw_list)

    return result


def day() -> list:
    full_day = list()
    for hour in range(0, 23):
        res = combine_hour(hour)
        full_day.extend(res)
    return full_day


if __name__ == "__main__":
    day = day()
    with open('full_day.json', 'w') as outfile:
        json.dump(day, outfile)
