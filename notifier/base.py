from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send_ip_change(self, old_ip: str, new_ip: str):
        """IP変更時の通知を送る"""
        pass
