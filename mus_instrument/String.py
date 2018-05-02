from enum_type.TypeInstrument import TypeInstrument
from mus_instrument.MusicalInstrument import MusicalInstrument


class String(MusicalInstrument):
    instrument_type = TypeInstrument.STRING
    length = 0.0

    def __init__(self, name, prise, weight, length):
        self.name = name
        self.prise = prise
        self.weight = weight
        self.length = length

    def __str__(self):
        return " Type of instrument:.." + str(self.instrument_type.value) + " Name:.." + self.name + " Prise:.." +\
               str(self.prise)  + " Length:.." + str(self.length) + " Weight:.." + str(self.weight)
