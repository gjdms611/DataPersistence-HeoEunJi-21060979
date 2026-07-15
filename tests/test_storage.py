import storage


def test_load_data_missing_file_returns_empty_list(tmp_path):
    path = tmp_path / "nofile.json"
    assert storage.load_data(path=str(path)) == []


def test_save_then_load_roundtrip(tmp_path):
    path = tmp_path / "items.json"
    data = [{"id": 1, "name": "widget", "value": 42}]
    storage.save_data(data, path=str(path))
    assert storage.load_data(path=str(path)) == data
