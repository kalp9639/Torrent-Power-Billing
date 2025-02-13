from abc import ABC, abstractmethod


class TariffCategory(ABC):
    """Abstract base class for all tariff categories."""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def run(self):
        """Abstract method to calculate the bill. Must be implemented in subclasses."""
        pass
