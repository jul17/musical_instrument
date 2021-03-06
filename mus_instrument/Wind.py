from enum_type.TypeInstrument import TypeInstrument
from mus_instrument.MusicalInstrument import MusicalInstrument


class Wind(MusicalInstrument):
    instrument_type = TypeInstrument.WIND

    def __init__(self, name, prise, guaranty, weight):
        self.name = name
        self.prise = prise
        self.guaranty = guaranty
        self.weight = weight

    def __str__(self):
        return " Type of instrument:.." + str(self.instrument_type.value) + " Name:.." +\
            self.name + " Prise:.." + str(self.prise) + " Guaranty:.." + self.guaranty + " Weight:.." + str(self.weight)
