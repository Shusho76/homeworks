class Country:
    def __init__(self, country_name, continent):
        self.country_name = country_name
        self.continent = continent
    def present_country(self):

        return F"Тhis is {self.country_name} and it is in {self.continent}." 

class Brand:
    def __init__(self, brand_name, business_start_date):
        self.brand_name = brand_name
        self.business_start_date= business_start_date

    def present_brend(self):
        return F"Тhis brand is called {self.brand_name} and it was founded on {self.business_start_date}."
class Season:
    def __init__(self, season_name, average_temperature):    

        self.season_name = season_name
        self.average_temperature = average_temperature

    def present_season(self):
        return F"It is {self.season_name} now and the average temperature can reach up to {self.average_temperature} degrees."

class Product(Country,Brand,Season):        
    def __init__(self, product_name, product_type, product_price, country_name, continent, brand_name, business_start_date,  season_name, average_temperature):
        self.product_name = product_name
        self.product_type = product_type
        self.product_price = product_price
        super().__init__(country_name,continent)
        super().__init__(brand_name,business_start_date)
        Season.__init__(self,season_name, average_temperature)
        

    def present_product(self):    
        return F"Our company  products {self.product_name} it refers to {self.product_type}, products cost nearly {self.product_price}."

    def discount(self):
        return F"It is {self.season_name} now and we have seasonal discounts 20 percent and our products now cost {self.product_price- 20 * (self.product_price /100)}."

country = Country("Germany","Europe")
print(country.present_country())
brand = Brand("Adidas","18/08/1949")
print(brand.present_brend())
season = Season("Spring", "25")
print(season.present_season())
product = Product("Sport shoes", "sport goods", 120 , "Germany", "Europe", "Adidas", "18.08.1949", "spring" , "25")
print(product.present_product())

print(product.discount())
