class MusicalManager:
    instruments = []

    def __init__(self):
        pass

    def sort_by_weight(self):
        self.instruments.sort(key=lambda m_instrument: m_instrument.weight, reverse=True)

    def find_by_type(self, instrument_type):
        founded_instruments = []

        for instrument in self.instruments:
            if instrument.instrument_type == instrument_type:
                founded_instruments.append(instrument)

        return founded_instruments

    def add(self, m_instrument):
        self.instruments += m_instrument

    def print_list(self):
        for m_instrument in self.instruments:
            print(m_instrument)
        print("\n")
