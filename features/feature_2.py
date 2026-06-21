from models.weapon import Weapon


def forge_weapon(inventory):
    print("\n--- RÈN VŨ KHÍ VẬT LÝ ---")
    name = input("Nhập tên vũ khí: ").strip().title()

    try:
        base_damage = int(input("Nhập sát thương gốc: ").strip())
    except ValueError:
        print("Giá trị phải lớn hơn 0!")
        return

    if base_damage <= 0:
        print("Giá trị phải lớn hơn 0!")
        return

    try:
        upgrade_level = int(input("Nhập cấp cường hóa: ").strip())
    except ValueError:
        print("Giá trị phải lớn hơn 0!")
        return

    if upgrade_level <= 0:
        print("Giá trị phải lớn hơn 0!")
        return

    weapon = Weapon(name, base_damage, upgrade_level)
    inventory.append(weapon)

    print(f"\n>> Rèn vũ khí vật lý thành công!")
    print(f"Tên vũ khí: {weapon.name}")
    print(f"Loại: Weapon")
    print(f"Cấp cường hóa: {weapon.upgrade_level}")
    print(f"Sát thương tổng: {weapon.calculate_total_damage()}")