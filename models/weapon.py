from models.equipment import Equipment


class Weapon(Equipment):
    """
    Vũ khí vật lý — Lesson 01 (Inheritance) + Lesson 04 (Operator Overloading).
    Kế thừa Equipment, override calculate_total_damage().
    Nạp chồng __gt__ và __add__ để so sánh và dung hợp vũ khí.
    """

    def __init__(self, name, base_damage, upgrade_level=0):
        self.name = name
        self.base_damage = base_damage
        self.upgrade_level = upgrade_level

    def calculate_total_damage(self):
        """Lesson 03 - Polymorphism: mỗi lớp tự tính sát thương theo công thức riêng."""
        return self.base_damage + (self.upgrade_level * 10)

    def __gt__(self, other):
        """
        Lesson 04 - Operator Overloading: nạp chồng toán tử >.
        So sánh sát thương tổng giữa 2 trang bị.
        Edge case: chỉ so sánh được với Equipment, không phải kiểu dữ liệu khác.
        """
        if not isinstance(other, Equipment):
            print("Chỉ có thể so sánh giữa các trang bị!")
            return NotImplemented
        return self.calculate_total_damage() > other.calculate_total_damage()

    def __add__(self, other):
        """
        Lesson 04 - Operator Overloading: nạp chồng toán tử + (Dung hợp).
        Trả về Weapon mới với tên ghép, base_damage cộng gộp, upgrade_level cộng gộp.
        Edge case: chỉ dung hợp được với Equipment.
        """
        if not isinstance(other, Equipment):
            print("Chỉ có thể dung hợp giữa các trang bị!")
            return NotImplemented
        new_name = f"Fusion({self.name} + {other.name})"
        new_base = self.base_damage + other.base_damage
        new_level = self.upgrade_level + other.upgrade_level
        return Weapon(new_name, new_base, new_level)