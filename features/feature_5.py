def fusion(inventory):
    print("\n--- DUNG HỢP VŨ KHÍ ---")
    if len(inventory) < 2:
        print("Cần ít nhất 2 vũ khí trong kho để dung hợp!")
        return

    w1 = inventory[0]
    w2 = inventory[1]

    print("Đang dung hợp 2 vũ khí đầu tiên trong kho...")
    print(f"\nVũ khí 1: {w1.name} | Cấp: {w1.upgrade_level} | Sát thương: {w1.calculate_total_damage()}")
    print(f"Vũ khí 2: {w2.name} | Cấp: {w2.upgrade_level} | Sát thương (base): {w2.base_damage}")

    # Operator Overloading __add__ — Lesson 04
    new_weapon = w1 + w2

    inventory.remove(w1)
    inventory.remove(w2)
    inventory.insert(0, new_weapon)

    print(f"\n>> Dung hợp vũ khí thành công!")
    print(f"Đã xóa khỏi kho: {w1.name}")
    print(f"Đã xóa khỏi kho: {w2.name}")
    print(f"\nVũ khí mới: {new_weapon.name}")
    print(f"Loại: Weapon")
    print(f"Cấp cường hóa: {new_weapon.upgrade_level}")
    print(f"Sát thương tổng: {new_weapon.calculate_total_damage()}")