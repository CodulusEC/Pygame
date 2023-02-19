from csv import reader

def import_csv_layout(path):
    terrmap = []
    with open(path) as level_map:
        layout = reader(level_map, delimeter = ',')
        for row in layout:
            terrmap.append(list(row))
        return terrmap
