class Sneaker:

    def __init__ (self, brand, model, colorway, release_year, size, condition):
         """
        Parameters:
        brand (str): Brand of the sneaker (e.g., Nike, Adidas).
        model (str): Model of the sneaker (e.g., Air Jordan, Ultraboost).
        colorway (str): Color scheme of the sneaker.
        release_year (int): Year the sneaker was released.
        size (float): Size of the sneaker.
        condition (str): Condition of the sneaker (e.g., new, used).
        """
         self.brand = brand
         self.model = model
         self.colorway = colorway
         self.release_year = release_year
         self.size = size
         self.condition = condition

    def __str__(self):
              """"
              Return a string representation of the Sneaker instance.
              """
              return f"{self.brand} {self.model} - {self.colorway}, Size: {self.size}, Released in {self.release_year}, Condition: {self.condition}"
# Example case:
if __name__ == "__main__":
    sneaker1 = Sneaker("Nike", "Air Jordan 1", "Black/Red", 1985, 9, "new")
    print(sneaker1)