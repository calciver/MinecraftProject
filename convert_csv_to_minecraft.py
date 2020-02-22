from mcpi.minecraft import Minecraft
import csv

def generate_dictionary(dictionary_csv = 'another_Block_ID_list.csv'):
    block_dictionary = {}
    with open(dictionary_csv) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            block_dictionary[row[0]] = [int(row[1]),int(row[2])]
    return(block_dictionary)

def set_block(coordinates,material):
    combined_list = coordinates + material        
    mc.setBlock(combined_list)
    
def csv_to_minecraft(blueprint_csv = 'Sample_item.csv', desired_location = [-1000,106,43]):
    block_dictionary = generate_dictionary()
    header = True
    with open(blueprint_csv) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:            
            if header == True:
                header = False
            else:
                x_coordinate = int(row[2]) + int(desired_location[0])
                y_coordinate = int(row[4]) + int(desired_location[1])
                z_coordinate = int(row[3]) + int(desired_location[2])
                coordinate_list = [x_coordinate,y_coordinate,z_coordinate]
                material_list = block_dictionary[row[1]]
                
                set_block(coordinate_list,material_list)

    print('Build Complete')

mc = Minecraft.create()
mc.player.setTilePos(-1100,110,50)
# mc.setBlock(-101,81,-56,39,0)
csv_file = 'for_use2.csv'
# with open(csv_file, newline='') as csvfile:
#     reader = csv.reader(csvfile,quotechar='|')
#     for row in reader:
#         print(row)
generate_dictionary()
csv_to_minecraft(csv_file)