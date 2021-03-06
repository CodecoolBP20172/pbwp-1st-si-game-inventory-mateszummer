# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification

# Displays the inventory.

def display_inventory(inventory):
    print("Inventory:\n")
    for key, value in inventory.items():
        print (value, key)
    print("Total number of items: ", sum(inventory.values()))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory.keys():
            inventory[item] += 1
        elif item == "": #empty values will not be added (import inventory, new line related)
            ...
        else:
            inventory[item] = 1
    return inventory


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order):
    order_dict = {"count,asc": False, "count,desc": True} #just trying out with dict
    if order is None:
        sorted_values = list(set(inventory.values()))
    else:
        sorted_values = sorted(list(set(inventory.values())), reverse=order_dict[order])
    max_len = len(max(inventory, key=len))
    hyphen_len = max_len * 2 + 1
    align_right = "{:>%d} {:>%d}" % (max_len, max_len)
    print("Inventory:")
    print(align_right.format("Count", "Item"))
    print("-" * hyphen_len)
    for number in sorted_values:
        for key, value in inv.items():
            if number == value: #reformed,useless count removed
                print(align_right.format(value, key))
    print("-" * hyphen_len)
    print("Total number of items: ", sum(inventory.values()))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename):
  import csv
    if filename is None:
        filename = "import_inventory.csv"
    with open(filename) as csvfile:
        for row in csv.reader(csvfile):
            add_to_inventory(inventory, row) #useless loop removed, named properly(row)
    return inventory


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename):
    import csv
    export_list = []
    if filename is None:
        filename = "export_inventory.csv"
    with open(filename, 'w') as myfile:
        wr = csv.writer(myfile)
        for key, value in inventory.items():
            for count in range(value):
                export_list.append(key)
        wr.writerow(export_list)

