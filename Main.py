from MusicalManager import MusicalManager
from enum_type.TypeInstrument import TypeInstrument
from mus_instrument.Drum import Drum
from mus_instrument.Keyboard import Keyboard
from mus_instrument.String import String
from mus_instrument.Wind import Wind

if __name__ == '__main__':
    manager = MusicalManager()

    drum = Drum("Drum Kit", 222.4, "1 year", 1)
    keyboard = Keyboard("Keyboard", 342.5, 3, "Brazil")
    string_violin = String("Violin", 2385.8, 2, 34)
    wind = Wind("Saxophone", 895.3, "3 years", 4)
    string_clarinet = String("Clarinet", 4565.8, 5, 24)

    manager.instruments = [drum, keyboard, string_violin, wind, string_clarinet]
    print("All Musical Instruments List:")
    manager.print_list()

    manager.sort_by_weight()
    print("Sorted by weight list")
    manager.print_list()

    manager.instruments = manager.find_by_type(TypeInstrument.STRING)
    print("Found by type:")
    manager.print_list()

    pass
