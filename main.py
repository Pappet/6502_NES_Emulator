from rom import ROM


def load():
    path = '/home/peter/Python/6502_NES_Emulator/Roms/mario.nes'
    rom = ROM()
    rom.load_rom(path)
    rom.print()


if __name__ == '__main__':
    load()
