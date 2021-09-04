from mockdb.dummy_data import initial_db_state
import json

db_state = initial_db_state


def get(type):
    return db_state[type]


def getById(type, id):
    return next((i for i in get(type) if i["id"] == id), None)


def create(type, payload):
    last_id = max([i["id"] for i in get(type)])
    new_id = last_id + 1
    payload["id"] = new_id
    db_state[type].append(payload)
    return payload


def updateById(type, id, update_values):
    item = getById(type, id)
    if item is None:
        return None
    for k, v in update_values.items():
        if k is not "id" and v is not None:
            item[k] = v
    return item


def deleteById(type, id):
    db_state[type] = [i for i in get(type) if i["id"] != id]

def getMinEpisodes(type, min):
    l = []
    for item in db_state[type]:
        if item['episodes_seen'] >= int(min):
            l.append(item)
    db_state["shows"] = l
    return db_state