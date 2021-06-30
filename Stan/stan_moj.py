from state_machine import (State, Event, acts_as_state_machine,
                           after, before, InvalidStateTransition)


@acts_as_state_machine
class Process:
    zatrzymanie = State(initial=True)
    otwarcie_drzwi = State()
    zamkniecie_drzwi = State()
    zablokowanie = State()
    jazda_w_gore = State()
    jazda_w_dol = State()
    odblokowanie = State()

    zatrzymac = Event(from_states=(jazda_w_dol, jazda_w_gore, odblokowanie), to_state=zatrzymanie)
    otwierac = Event(from_states=(zatrzymanie, odblokowanie), to_state=otwarcie_drzwi)
    zamykac = Event(from_states=otwarcie_drzwi, to_state=zamkniecie_drzwi)
    jechac_w_gore = Event(from_states=zamkniecie_drzwi, to_state=jazda_w_gore)
    jechac_w_dol = Event(from_states=zamkniecie_drzwi, to_state=jazda_w_dol)
    blokowac = Event(from_states=(zatrzymanie, otwarcie_drzwi, zamkniecie_drzwi),to_state=zablokowanie)
    odblokowac = Event(from_states=zablokowanie, to_state=odblokowanie)

    def __init__(self, name):
        self.name = name

    @ after('zatrzymac')
    def wait_info(self):
        print(f'{self.name} się zatrzymała')

    @ after('otwierac')
    def block_info(self):
        print(f'Drzwi {self.name}(y) otwarły się')

    @ after('zamykac')
    def swap_wait_info(self):
        print(f'Drzwi {self.name}(y) zamknęły się')

    @ after('jechac_w_gore')
    def run_info(self):
        print(f'{self.name} rusza do góry')

    @ after('jechac_w_dol')
    def terminate_info(self):
        print(f'{self.name} rusza w dół')

    @ after('blokowac')
    def swap_wait_info(self):
        print(f'{self.name} jest zablokowana')

    @after('odblokowac')
    def swap_block_info(self):
        print(f'{self.name} jest odblokowana')


def transition(process, event, event_name):
    try:
        event()
    except InvalidStateTransition as err:
        print(f'Error: przejście {process.name} z procesu {process.current_state} do {event_name} jest niepoprawne')


def state_info(process):
    print(f'stan procesu: {process.name}: '
          f'{process.current_state}')


def main():
    ZATRZYMYWANIE = 'zatrzymywanie'
    OTWIERANIE = 'otwieranie'
    ZAMYKANIE = 'zamykanie'
    JAZDA_W_GORE = 'jazda_w_gore'
    JAZDA_W_DOL = 'jazda_w_dol'
    BLOKOWANIE = 'blokowanie'
    ODBLOKOWANIE = 'odblokowanie'

    p1 = Process('Winda')
    state_info(p1)

    print()
    transition(p1, p1.otwierac, OTWIERANIE)
    state_info(p1)

    print()
    transition(p1, p1.zamykac, ZAMYKANIE)
    state_info(p1)

    print()
    transition(p1, p1.jechac_w_gore, JAZDA_W_GORE)
    state_info(p1)

    print()
    transition(p1, p1.zatrzymac, ZATRZYMYWANIE)
    state_info(p1)

    print()
    transition(p1, p1.otwierac, OTWIERANIE)
    state_info(p1)

    print()
    transition(p1, p1.zamykac, ZAMYKANIE)
    state_info(p1)

    print()
    transition(p1, p1.jechac_w_dol, JAZDA_W_DOL)
    state_info(p1)

    print()
    transition(p1, p1.jechac_w_gore, JAZDA_W_GORE)
    state_info(p1)

    print()
    transition(p1, p1.zatrzymac, ZATRZYMYWANIE)
    state_info(p1)

    print()
    transition(p1, p1.otwierac, OTWIERANIE)
    state_info(p1)

    print()
    transition(p1, p1.zamykac, ZAMYKANIE)
    state_info(p1)

    print()
    transition(p1, p1.blokowac, BLOKOWANIE)
    state_info(p1)

    print()
    transition(p1, p1.odblokowac, ODBLOKOWANIE)
    state_info(p1)


if __name__ == '__main__':
    main()
