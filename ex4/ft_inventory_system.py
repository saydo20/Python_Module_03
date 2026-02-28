import sys

items_base = {
    "sword": {"type": "weapon", "value": 150},
    "shield": {"type": "armor", "value": 120},
    "armor": {"type": "armor", "value": 200},
    "helmet": {"type": "armor", "value": 80},
    "potion": {"type": "consumable", "value": 25},
}


def inventory_parser() -> dict:
    if len(sys.argv) <= 1:
        raise ValueError("the program must has arguments")
    inventory = {}
    for arg in sys.argv[1:]:
        element = arg.split(":")
        if len(element) != 2 or element[0] == "":
            raise ValueError("argument must be key:quantity")
        name, quantity = element
        item_info = items_base.get(
            name, {"type": "unknown", "value": 0}
        )

        inventory.update({
            name: {
                "name": name,
                "type": item_info["type"],
                "quantity": int(quantity),
                "value": item_info["value"],
                }
        })

    return inventory


def get_max(inventory) -> tuple[int, int]:
    max_key, *rest = inventory.keys()
    max_value = inventory[max_key]["quantity"]

    for key, item in inventory.items():
        if item["quantity"] > max_value:
            max_value = item["quantity"]
            max_key = key

    return max_key, max_value


def get_min(inventory) -> tuple[int, int]:
    min_key, *rest = inventory.keys()
    min_value = inventory[min_key]["quantity"]

    for key, item in inventory.items():
        if item["quantity"] < min_value:
            min_value = item["quantity"]
            min_key = key

    return min_key, min_value


def manage_categories(inventory: dict) -> None:
    print("\n=== Item Categories ===")
    moderate = {}
    scarce = {}

    for key, item in inventory.items():
        qty = item["quantity"]
        if qty >= 5:
            moderate[key] = qty
        else:
            scarce[key] = qty
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")


def suggestions_manager(inventory: dict) -> None:
    print("\n=== Management Suggestions ===")
    suggestions = []
    for key, value in inventory.items():
        if value["quantity"] <= 1:
            suggestions += [value["name"]]
    print("Restock needed: ", end="")
    print(*suggestions, sep=", ")


def inventory_system(inventory: dict) -> None:
    max_key, max_value = get_max(inventory)
    min_key, min_value = get_min(inventory)
    print("=== Inventory System Analysis ===")
    total_items = 0
    for item in inventory.values():
        total_items += item["quantity"]
    if total_items == 0:
        raise ValueError("inventory is empty")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")
    print("\n=== Current Inventory ===")
    factor = 100 / total_items
    current_max = max_value
    while current_max > 0:
        for key, item in inventory.items():
            value = item["quantity"]
            if value == current_max:
                percent = factor * value
                if value == 1:
                    print(f"{key}: {value} unit ({percent:.1f}%)")
                else:
                    print(f"{key}: {value} units ({percent:.1f}%)")
        current_max -= 1
    print("\n=== Inventory Statistics ===")
    if max_value == 1:
        print(f"Most abundant: {max_key} ({max_value} unit)")
    else:
        print(f"Most abundant: {max_key} ({max_value} units)")
    if min_value == 1:
        print(f"Most abundant: {min_key} ({min_value} unit)")
    else:
        print(f"Most abundant: {min_key} ({min_value} units)")
    manage_categories(inventory)
    suggestions_manager(inventory)
    keys = []
    values = []
    for key in inventory.keys():
        keys += [key]
    print("Dictionary keys: ",  end="")
    print(*keys, sep=" ,")
    for value in inventory.values():
        values += [value['quantity']]
    print("Dictionary values: ", end="")
    print(*values, sep=" ,")
    print(f"Sample lookup - 'sword' in inventory : {'sword' in inventory}")


def main() -> None:
    try:
        inventory = inventory_parser()
        inventory_system(inventory)
    except Exception as error:
        print(f"error : {error}")


main()
