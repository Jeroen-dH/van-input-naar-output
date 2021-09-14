#jeroen , de Heer en opdracht: Pizza calculator
pizza_groote = ['small', 'medium', 'large']
prijs_pizza = {'small': 7, 'medium': 9, 'large': 12}
totaal_bedrag = []
eind_bedrag = {}


print("Goedemerge, welkom bij de pizzawinkel")
order_pizza = True
while order_pizza:    
    print("maak hier een keuze: ")
    
    for pizzas in pizza_groote:
        print(pizzas)
        
    while True:
        pizza = input("wat is uw keuze")
        if pizza in pizza_groote:
            print(f"Je heb de {pizza} pizza bestelled.")
            totaal_bedrag.append(prijs_pizza[pizza])
            break
        if pizza not in pizza_groote:
            print(f"sorry maar die hebben we niet {pizza}.")

    extra_pizza = input("wil je nog een andere pizza toevoegen?")
    if extra_pizza == "nee":
        for key, value in eind_bedrag.items():
            print(f"\nje hebt besteld: {key} pizza")
        check_order = True
        while check_order:
            print()
            order_correct = input("klopt uw bestelling? ja/nee ")
            if order_correct == "ja":
                check_order = False
                order_pizza = False
            if order_correct == "nee":
                print("dat is pech, u kunt niet meer terug")


print(f"Je totaal bedrag is: ${sum(totaal_bedrag)}")