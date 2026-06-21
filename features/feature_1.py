from models.magic_sword import MagicSword


def view_inventory(inventory):
    print("\n--- KHO VŨ KHÍ CỦA NGƯỜI CHƠI ---")
    if not inventory:
        print("Kho vũ khí hiện đang trống.")
        print("Vui lòng rèn vũ khí bằng Chức năng 2 hoặc Chức năng 3.")
        return

    print(f"{'STT':<6}| {'Tên vũ khí':<30}| {'Loại':<14}| {'Cấp':<6}| Sát thương tổng")
    print("-" * 80)

    for i, item in enumerate(inventory, 1):
        # Polymorphism (Duck Typing) - Lesson 03:
        # Gọi calculate_total_damage() đồng nhất, Python tự dispatch đúng phiên bản
        weapon_type = type(item).__name__
        damage = item.calculate_total_damage()
        print(f"{i:<6}| {item.name:<30}| {weapon_type:<14}| {item.upgrade_level:<6}| {damage}")