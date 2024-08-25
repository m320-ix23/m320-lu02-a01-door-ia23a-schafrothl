"""
Dieses Modul beschreibt eine Türklasse (Door) und eine Türschlossklasse (DoorLock).
"""

class Door:
    """
    Diese Klasse beschreibt eine Türe mit der Eigenschaft color (Farbe) und den Zuständen
    door_is_open (für geöffnete Türe) sowie door_is_locked (für verriegelte Türe).
    Die Türe überwacht die beiden Zustände und verhindert so Aktionen, die nicht möglich sind.
    Das Verriegeln selbst delegiert die Türe an ein Objekt vom Typ DoorLock (Türschloss).
    """

    def __init__(self, ref2door_lock, base_color):
        """
        Erzeugt ein Tür-Objekt.
        :param ref2door_lock: Referenz auf ein Türschloss-Objekt
        :param base_color: Farbe der Tür
        """
        self._the_door_lock = ref2door_lock
        self.color = base_color
        self._door_is_open = False
        self._door_is_locked = False

    def open_the_door(self):
        """
        Methode für das Öffnen der Tür.
        Das ist aber nur möglich, wenn die Tür nicht verriegelt ist.
        """
        if not self.door_is_locked:
            self._door_is_open = True

    def close_the_door(self):
        """
        Methode für das Schließen der Tür.
        Das geht immer, auch wenn die Tür schon geschlossen
        oder verriegelt ist. Der Zustand ändert dann nämlich nicht.
        """
        self._door_is_open = False

    def lock_the_door(self):
        """
        Methode für das Verriegeln der Tür.
        Das ist nur möglich, wenn die Tür nicht offen ist.
        Für das Verriegeln ist aber das Türschloss zuständig. Es weiß, wie das geht.
        """
        if not self._door_is_open:
            self._door_is_locked = self._the_door_lock.lock()

    def unlock_the_door(self):
        """
        Methode für das Entriegeln der Tür.
        Das ist nur möglich, wenn die Tür verriegelt ist.
        Für das Entriegeln ist aber das Türschloss zuständig. Es weiß, wie das geht.
        """
        if self._door_is_locked:
            self._door_is_locked = self._the_door_lock.unlock()

    def test(self):
        """
        Schreibt alle Attribute in den StdOut.
        """
        print(f'Türfarbe: {self.color}\n'
              f'Tür offen: {self._door_is_open}\n'
              f'Tür verriegelt: {self._door_is_locked}')

    @property
    def door_is_open(self):
        """
        Getter-Methode für den Zustand door_is_open.
        :return: True, wenn die Tür offen ist, sonst False.
        """
        return self._door_is_open

    @property
    def door_is_locked(self):
        """
        Getter-Methode für den Zustand door_is_locked.
        :return: True, wenn die Tür verriegelt ist, sonst False.
        """
        return self._door_is_locked

    @property
    def color(self):
        """
        Getter-Methode für die Eigenschaft color.
        :return: Die Farbe des Objekts.
        """
        return self._color

    @color.setter
    def color(self, new_color):
        """
        Setter-Methode für die Eigenschaft color.
        :param new_color: Neue Farbe der Tür.
        """
        self._color = new_color


class DoorLock:
    """
    Dummy-Klasse, damit in der Klasse Tür kein Fehler auftritt.
    """

    def __init__(self):
        print("Ein Schloss wurde erzeugt")

    def lock(self):
        return True

    def unlock(self):
        return False


# Hier die main-Methode festlegen
if __name__ == "__main__":
    print("Test für Tür-Objekt")
    the_door_lock = DoorLock()
    the_door = Door(the_door_lock, "grün")
    the_door.test()
    print("-- Tür jetzt öffnen")
    the_door.open_the_door()
    the_door.test()
