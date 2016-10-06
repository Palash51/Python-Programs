from string import Template

def Main():
    cart = []
    cart.append(dict(item="Cock", price=8, qty=2))
    cart.append(dict(item="cack", price=12, qty=1))
    cart.append(dict(item="fish", price=32, qty=4))

    t = Template("$qty * $item = $price")
    total = 0
    print(cart)
    for data in cart:
        print(t.substitute(data))
        total += data["price"]

            
    print ("Total: " +str(total))

if __name__ == "__main__":
    Main()
