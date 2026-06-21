from models.magic_sword import MagicSword


def forge_magic_sword(inventory):
    print("\n--- RÈN KIẾM MA THUẬT ---")
    name = input("Nhập tên kiếm ma thuật: ").strip().title()

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

    try:
        magic_power = int(input("Nhập sức mạnh phép thuật: ").strip())
    except ValueError:
        print("Giá trị phải lớn hơn 0!")
        return

    if magic_power <= 0:
        print("Giá trị phải lớn hơn 0!")
        return

    sword = MagicSword(name, base_damage, upgrade_level, magic_power)
    inventory.append(sword)

    print(f"\n>> Rèn kiếm ma thuật thành công!")
    print(f"Tên vũ khí: {sword.name}")
    print(f"Loại: MagicSword")
    print(f"Cấp cường hóa: {sword.upgrade_level}")
    print(f"Sát thương gốc: {sword.base_damage}")
    print(f"Sức mạnh phép thuật: {sword.magic_power}")
    print(f"Sát thương tổng: {sword.calculate_total_damage()}")