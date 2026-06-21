"""
1. Abstract Base Class — Equipment

Dùng ABC + @abstractmethod buộc mọi lớp con phải tự định nghĩa calculate_total_damage(). Nếu lập trình viên "hậu bối" tạo class Bow(Equipment) mà quên override, Python sẽ raise TypeError ngay khi Bow() — không chờ đến lúc runtime crash
Equipment() trực tiếp cũng không khởi tạo được → Bẫy 1 tự xử lý
2. Multiple Inheritance & MRO của MagicSword
MagicSword → Weapon → Equipment → MagicMixin → object
MagicSword.__mro__ = [MagicSword, Weapon, Equipment, MagicMixin, object]
__init__ của MagicSword:
pythondef __init__(self, name, base_damage, upgrade_level, magic_power):
    Weapon.__init__(self, name, base_damage, upgrade_level)  # khởi tạo Weapon
    MagicMixin.__init__(self, magic_power)                   # khởi tạo Mixin
Gọi tên trực tiếp thay vì super() để đảm bảo cả 2 nhánh đều được khởi tạo đầy đủ.
3. Polymorphism — Chức năng 1

Vòng lặp gọi item.calculate_total_damage() đồng nhất trên mọi phần tử inventory. Python tự gọi đúng phiên bản của Weapon hay MagicSword tùy loại thực tế của object — Duck Typing: "miễn có method này là chạy được."
4. Operator Overloading — __add__ pseudocode
__add__(self, other):
    if other không phải Equipment → báo lỗi
    new_name = "Fusion({self.name} + {other.name})"
    new_base  = self.base_damage + other.base_damage
    new_level = self.upgrade_level + other.upgrade_level
    return Weapon(new_name, new_base, new_level)   # luôn trả về Weapon
"""


from features import view_inventory, forge_weapon, forge_magic_sword, appraise, fusion


def main():
    inventory = []

    while True:
        print("\n===== LÒ RÈN VŨ KHÍ RIKKEI STUDIOS =====")
        print("1. Xem kho vũ khí & Sát thương tổng")
        print("2. Rèn Vũ khí Vật lý (Tạo Weapon)")
        print("3. Rèn Kiếm Ma Thuật (Tạo MagicSword)")
        print("4. Thẩm định vũ khí (So sánh lớn hơn)")
        print("5. Dung hợp vũ khí (Cộng dồn cấp độ)")
        print("6. Thoát game")
        print("==========================================")
        choice = input("Chọn chức năng (1-6): ").strip()

        match choice:
            case "1":
                view_inventory(inventory)
            case "2":
                forge_weapon(inventory)
            case "3":
                forge_magic_sword(inventory)
            case "4":
                appraise(inventory)
            case "5":
                fusion(inventory)
            case "6":
                print("Thoát Lò Rèn. Hẹn gặp lại Anh hùng!")
                break
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 6!")


if __name__ == "__main__":
    main()