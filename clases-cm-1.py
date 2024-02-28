class TarjetaCredito:
    """
    Representación de una tarjeta de crédito en Python.
    Solamente nos enfocamos en los datos del cliente y su saldo.
    """

    def __init__(self, nombre, apellido, saldo=0):
        self.nombre = nombre
        self.apellido = apellido
        self.saldo = saldo

    def mostrar_datos(self):
        print(f"Titular de la tarjeta: {self.nombre}")
        print(f"Saldo tarjeta: {self.saldo}")
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nSaldo tarjeta: {self.saldo}"

    def __repr__(self):
        return f"TarjetaCredito(nombre={self.nombre}, apellido={self.apellido}, saldo={self.saldo})"
    
    def __lt__(self, other):
        return self.saldo < other.saldo    
    
    def __le__(self, other):
        return self.saldo <= other.saldo    
    
    def __eq__(self, other):
        return self.saldo == other.saldo and self.nombre == other.nombre and self.apellido == other.apellido
    
    def __nq__(self, other):
        """
        Compara dos objetos de la clase TarjetaCredito para determinar si son diferentes
        """
        return self.nombre != other.nombre or self.apellido != other.apellido   
    
    def __gt__(self, other):
        return self.saldo > other.saldo    
    
    def __ge__(self, other):
        return self.saldo >= other.saldo
    
    def __add__(self, other):

        if self != other:
            print("Las tarjetas no pertenecen a la misma persona.")
            return None

        saldo_inicial = self.saldo
        saldo_suma = other.saldo
        suma = saldo_suma + saldo_inicial

        self.saldo = 0
        other.saldo = 0

        nueva = TarjetaCredito(self.nombre, self.apellido, suma)
        return nueva


tarjeta_nueva = TarjetaCredito(nombre="Santi", apellido="Rosales", saldo=50)
tarjeta_dos = TarjetaCredito(nombre="Santiago", apellido="Rosales", saldo=200)
resultante = tarjeta_nueva + tarjeta_dos
print(resultante)
print(tarjeta_nueva)
print(tarjeta_dos)