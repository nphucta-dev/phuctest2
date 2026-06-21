from abc import ABC, abstractmethod


class Equipment(ABC):
    """
    Abstract Base Class — Lesson 05.
    Không thể khởi tạo trực tiếp Equipment().
    @abstractmethod buộc mọi lớp con phải tự định nghĩa calculate_total_damage().
    """

    @abstractmethod
    def calculate_total_damage(self):
        """Mỗi loại vũ khí có công thức sát thương riêng — bắt buộc override."""
        pass