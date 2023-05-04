class ROM:
    def __init__(self):
        self.path = None
        self.data = None

    def load_rom(self, path):
        self.path = path

        with open(self.path, 'rb') as f:
            hex_str = f.read()  # Lese den Inhalt der Datei als Zeichenkette und entferne Leerzeichen

        self.data = hex_str

    def print(self):
        print(self.data)
