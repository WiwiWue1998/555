inventory = [] #Liste inventory definieren

while True:      #Anzeigen des Menüs bis eine Option gewählt wird (while loop)
    print("\n1. Add Product\n2. View Inventory\n3. Remove Product\n4. Exit") #Print der das Menü zeigt
    choice = int(input("Choose number of your desired option: ")) #Frage nach Wahl des Menüpunkts über auswahl der Nummer
    if choice == 1:       #Wenn 1 gewählt wird, nach Name und Anzahl des Produkts, was in das Inventar hinzugefügt werden soll gefragt
        product_name = input("Enter name of product: ")
        quantity = int(input("Enter quantity: "))
        product_exists = False             #Wenn das Produkt noch nicht in der Liste inventory ist wird es hinzugefügt und es wird wieder zum Menü zurückgekehrt
        for i in range(len(inventory)):
            if inventory[i][0] == product_name: #variable 0 ist Name
                inventory[i][1] += quantity     #variable 1 ist Anzahl
                product_exists = True
                break
        if not product_exists:                      #Wenn Produkt existiert anzahl anpassen
            inventory.append([product_name, quantity])
    elif choice == 2:                              # Wahl Menüpunkt 2 
        if len(inventory) == 0:                    # Fals Liste leer ist wird diese Nachricht angezeigt
            print("Inventory is empty.")
        else:
            print("\nProduct Name | Quantity")      # False Liste nicht leer ist Produkte mit Anzahl so formatiert Anzeigen
            for product in inventory:
                print(f"{product[0]} | {product[1]}")
    elif choice == 3:                                   #Wahl Menüpunkt 3
        product_name = input("Enter name of product to remove it: ") #Frage nach Input des Names des Produktes das entfernt werden soll
        for i in range(len(inventory)):              #Fals der Name in der Liste 'inventory' enthalten ist wird das Produkt entfernt und eine bestätigung ausgegeben 
            if inventory[i][0] == product_name:
                del inventory[i]
                print(f"Product '{product_name}' removed successfully.")
                break
        else:
            print(f"Product '{product_name}' not found in inventory.") #Fals nicht in der liste wird diese nachricht ausgegeben
    elif choice == 4:              # bei wahl von 4 anzeigen dieser nachricht
        print("Exiting...")
        break