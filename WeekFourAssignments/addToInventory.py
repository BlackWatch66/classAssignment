def addToInventory(inventory, addedItems):
    count = 0
    for i in addedItems :
        val = 1
        if inventory.__contains__(i) :
            val = inventory [i] + 1 
        inventory[i] = val
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)
displayInventory(inv)