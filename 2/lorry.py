def lorry():
    weight = 0
    load = []
    items = [750, 387, 291, 712, 100, 622, 109, 750, 282]
    for item in items:
        if weight <= 3000:           
            load.append(items[item])
            weight+= item
        
