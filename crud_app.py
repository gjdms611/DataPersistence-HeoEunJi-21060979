import repository

MENU = """=== DataPersistence CRUD PoC ===
1. Create
2. Read (list all)
3. Read (find by id)
4. Update
5. Delete
6. Exit
"""


def do_create():
    name = input("name: ")
    value = input("value: ")
    item = repository.create_item(name, value)
    print(f"생성됨: {item}")


def do_list():
    items = repository.list_items()
    if not items:
        print("저장된 데이터 없음")
        return
    for item in items:
        print(item)


def do_find():
    item_id = int(input("id: "))
    item = repository.find_item(item_id)
    if item is None:
        print("not found")
    else:
        print(item)


def do_update():
    item_id = int(input("id: "))
    name = input("new name (empty to keep): ")
    value = input("new value (empty to keep): ")
    item = repository.update_item(
        item_id,
        name=name if name else None,
        value=value if value else None,
    )
    if item is None:
        print("not found")
    else:
        print(f"수정됨: {item}")


def do_delete():
    item_id = int(input("id: "))
    success = repository.delete_item(item_id)
    if success:
        print("삭제됨")
    else:
        print("not found")


def main():
    while True:
        print(MENU)
        choice = input("choice: ")
        if choice == "1":
            do_create()
        elif choice == "2":
            do_list()
        elif choice == "3":
            do_find()
        elif choice == "4":
            do_update()
        elif choice == "5":
            do_delete()
        elif choice == "6":
            print("종료합니다.")
            break
        else:
            print("잘못된 선택입니다.")


if __name__ == "__main__":
    main()
