class MagicMixin:
    """
    Mixin class — Lesson 02 (Multiple Inheritance).
    Không đứng độc lập, chỉ bổ sung thuộc tính phép thuật cho lớp kết hợp.
    """

    def __init__(self, magic_power):
        self.magic_power = magic_power

    def cast_glow(self):
        print(f"✨ Vũ khí phát sáng với sức mạnh phép thuật {self.magic_power}!")