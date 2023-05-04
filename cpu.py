class CPU:
    def __init__(self):
        self.a = 0  # Akkumulator
        self.x = 0  # X-Register
        self.y = 0  # Y-Register
        self.pc = 0  # Programmzähler
        self.sp = 0  # Stack Pointer

        # Initialisiere das Statusregister (N, V, -, B, D, I, Z, C)
        """
        N = negative flag (1 when result is negative)
        V = overflow flag (1 on signed overflow)
        # = unused (always 1)
        B = break flag (1 when interupt was caused by a BRK)
        D = decimal flag (1 when CPU in BCD mode)
        I = IRQ flag (when 1, no interupts will occur (exceptions are IRQs forced by BRK and NMIs))
        Z = zero flag (1 when all bits of a result are 0)
        C = carry flag (1 on unsigned overflow)
        """
        self.status = 0b00100000

        def reset(self):
            # Setze die CPU auf ihren Anfangszustand zurück
            pass

        def execute(self, opcode):
            # Führe einen Befehl basierend auf dem gegebenen Opcode aus
            if opcode in self.opcodes:
                self.opcodes[opcode]()
            else:
                print(f"Unbekannter Opcode: {opcode:02X}")

        def set_flag(self, flag, value):
            # Setze oder lösche ein Statusflag
            pass

        def get_flag(self, flag):
            # Prüfe den Wert eines Statusflags
            pass
