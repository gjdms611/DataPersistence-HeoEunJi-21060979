import pytest

import repository


def test_create_item_appears_in_list(tmp_path):
    path = str(tmp_path / "items.json")
    repository.create_item("widget", 42, path=path)
    items = repository.list_items(path=path)
    assert len(items) == 1
    assert items[0]["name"] == "widget"
    assert items[0]["value"] == 42


def test_create_item_empty_name_raises_valueerror(tmp_path):
    path = str(tmp_path / "items.json")
    with pytest.raises(ValueError):
        repository.create_item("", 42, path=path)


def test_find_item_by_id(tmp_path):
    path = str(tmp_path / "items.json")
    created = repository.create_item("widget", 42, path=path)
    found = repository.find_item(created["id"], path=path)
    assert found == created


def test_find_item_missing_returns_none(tmp_path):
    path = str(tmp_path / "items.json")
    repository.create_item("widget", 42, path=path)
    assert repository.find_item(999, path=path) is None


def test_update_item_changes_field_and_persists(tmp_path):
    path = str(tmp_path / "items.json")
    created = repository.create_item("widget", 42, path=path)
    repository.update_item(created["id"], name="gadget", path=path)
    found = repository.find_item(created["id"], path=path)
    assert found["name"] == "gadget"
    assert found["value"] == 42


def test_update_item_missing_returns_none(tmp_path):
    path = str(tmp_path / "items.json")
    repository.create_item("widget", 42, path=path)
    assert repository.update_item(999, name="gadget", path=path) is None


def test_delete_item_removes_and_returns_true(tmp_path):
    path = str(tmp_path / "items.json")
    created = repository.create_item("widget", 42, path=path)
    assert repository.delete_item(created["id"], path=path) is True
    assert repository.list_items(path=path) == []


def test_delete_item_missing_returns_false(tmp_path):
    path = str(tmp_path / "items.json")
    repository.create_item("widget", 42, path=path)
    assert repository.delete_item(999, path=path) is False
