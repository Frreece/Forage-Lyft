from abc import ABC, abstractmethod
from engine import engine


class Car(ABC):
    def __init__(self, engine, battery, last_service_date):
        self.engine = engine
        self.Battery = battery

    @abstractmethod
    def needs_service(self):
        if (self.engine.needs_service):
            return True
        
        if (self.Battery.needs_service):
            return True
