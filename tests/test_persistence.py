import repository


def test_data_persists_after_simulated_restart(tmp_path):
    path = str(tmp_path / "items.json")

    item1 = repository.create_item("widget", 42, path=path)
    item2 = repository.create_item("gadget", 7, path=path)

    # Simulate a fresh process reading the file from disk (no in-memory cache).
    items = repository.list_items(path=path)
    assert len(items) == 2
    assert items[0] == item1
    assert items[1] == item2

    # Update one item, then re-read fresh to confirm the change stuck.
    repository.update_item(item1["id"], value=100, path=path)
    items = repository.list_items(path=path)
    updated = next(i for i in items if i["id"] == item1["id"])
    assert updated["value"] == 100

    # Delete the other item, then re-read fresh to confirm only one remains.
    repository.delete_item(item2["id"], path=path)
    items = repository.list_items(path=path)
    assert len(items) == 1
    assert items[0]["id"] == item1["id"]
    assert items[0]["value"] == 100
