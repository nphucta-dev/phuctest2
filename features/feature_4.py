def appraise(inventory):
    print("\n--- THẨM ĐỊNH VŨ KHÍ ---")
    if len(inventory) < 2:
        print("Cần ít nhất 2 vũ khí trong kho để thẩm định!")
        return

    w1 = inventory[0]
    w2 = inventory[1]
    d1 = w1.calculate_total_damage()
    d2 = w2.calculate_total_damage()

    print(f"Vũ khí thứ nhất:")
    print(f"{w1.name} | Loại: {type(w1).__name__} | Sát thương: {d1}")
    print(f"\nVũ khí thứ hai:")
    print(f"{w2.name} | Loại: {type(w2).__name__} | Sát thương: {d2}")

    # Operator Overloading __gt__ — Lesson 04
    if w1 > w2:
        print(f"\nKết quả: {w1.name} mạnh hơn {w2.name}.")
    elif w2 > w1:
        print(f"\nKết quả: {w2.name} mạnh hơn {w1.name}.")
    else:
        print(f"\nKết quả: Hai vũ khí có sức mạnh ngang nhau.")