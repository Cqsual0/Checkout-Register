class Product:
    def __init__(self, barcode, name, description, price):
        self.set_barcode(barcode)
        self.set_name(name)
        self.set_description(description)
        self.set_price(price)

    def __str__(self):
        return f"Barcode: {self.get_barcode()}, Name: {self.get_name()}, Description: {self.get_description()}, Price: {self.get_price()}"

    def get_barcode(self) -> int:
        """Get the product's barcode."""
        return self._barcode

    def set_barcode(self, barcode: int):
        """Set the product's barcode."""
        self._barcode = barcode

    def get_name(self) -> str:
        """Get the product's name."""
        return self._name

    def set_name(self, name: str):
        """Set the product's name."""
        self._name = name

    def get_description(self) -> str:
        """Get the product's description."""
        return self._description

    def set_description(self, description: str):
        """Set the product's description."""
        self._description = description

    def get_price(self) -> float:
        """Get the product's price."""
        return self._price

    def set_price(self, price: float):
        """Set the product's price."""
        self._price = price

