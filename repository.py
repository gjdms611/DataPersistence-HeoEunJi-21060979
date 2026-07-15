import storage


def next_id(items: list) -> int:
    if not items:
        return 1
    return max(item["id"] for item in items) + 1


def list_items(path=storage.DEFAULT_DATA_FILE) -> list:
    return storage.load_data(path)


def find_item(item_id, path=storage.DEFAULT_DATA_FILE):
    items = storage.load_data(path)
    for item in items:
        if item["id"] == item_id:
            return item
    return None


def create_item(name, value, path=storage.DEFAULT_DATA_FILE) -> dict:
    if not name:
        raise ValueError("name must not be empty")
    items = storage.load_data(path)
    item = {"id": next_id(items), "name": name, "value": value}
    items.append(item)
    storage.save_data(items, path)
    return item


def update_item(item_id, name=None, value=None, path=storage.DEFAULT_DATA_FILE):
    items = storage.load_data(path)
    for item in items:
        if item["id"] == item_id:
            if name is not None:
                item["name"] = name
            if value is not None:
                item["value"] = value
            storage.save_data(items, path)
            return item
    return None


def delete_item(item_id, path=storage.DEFAULT_DATA_FILE) -> bool:
    items = storage.load_data(path)
    new_items = [item for item in items if item["id"] != item_id]
    if len(new_items) == len(items):
        return False
    storage.save_data(new_items, path)
    return True
