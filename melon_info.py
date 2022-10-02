"""Print out all the melons in our inventory."""


# from melons import melon_names, melon_prices, melon_seedlessness 
from melons import melon_data 

# # def print_melon(name, price, seedless):
# def print_melon_report(attribute, value):

#     """Print each melon with corresponding attribute information."""
#     print(f"{attribute}: {value}")


# for melon, data in melon_data.items():
#     print("\n")
#     print(f"{melon.upper()}")
#     for attribute, value in data.items():
#         print_melon(attribute, value)
#     print("\n")
#     print("**********************************")

# def print_melon(name, price, seedless):
def print_melon_report(melons):

    """Print each melon with corresponding attribute information."""

    for melon, attributes in melons.items():
        print("\n")
        print(f"{melon.upper()}")
        for attribute, value in attributes.items():
            print(f"{attribute}: {value}")
        print("\n")
        print("**********************************")

print_melon_report(melon_data)
