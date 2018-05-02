from enum_type.TypeInstrument import TypeInstrument
from mus_instrument.MusicalInstrument import MusicalInstrument


class Keyboard(MusicalInstrument):
    instrument_type = TypeInstrument.KEYBOARD

    def __init__(self, name, prise, weight, country_from):
        self.name = name
        self.prise = prise
        self.weight = weight
        self.country_from = country_from

    def __str__(self):
        return " Type of instrument:.." + str(self.instrument_type.value) + " Name:.." + \
            self.name + " Prise:.." + str(self.prise) + " Coontry from:.." + self.country_from+" Weight:.." + str(self.weight)
