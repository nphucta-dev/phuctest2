from models.weapon import Weapon
from models.magic_mixin import MagicMixin


class MagicSword(Weapon, MagicMixin):
    """
    Kiếm Ma Thuật — Lesson 02 (Multiple Inheritance & MRO).
    MRO: MagicSword → Weapon → Equipment → MagicMixin → object

    Gọi trực tiếp Weapon.__init__ và MagicMixin.__init__ thay vì super()
    để đảm bảo cả 2 nhánh đều được khởi tạo đầy đủ (tránh Bẫy 3 - MRO).
    """

    def __init__(self, name, base_damage, upgrade_level, magic_power):
        Weapon.__init__(self, name, base_damage, upgrade_level)
        MagicMixin.__init__(self, magic_power)

    def calculate_total_damage(self):
        """
        Lesson 03 - Polymorphism: override riêng cho MagicSword.
        Công thức: base_damage + (upgrade_level * 10) + magic_power
        """
        return self.base_damage + (self.upgrade_level * 10) + self.magic_power