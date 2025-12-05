def invert():
    """ run this function to read in the in.png image,
        change it, and write out the result to out.png
    """
    im_pix = get_rgb('in.png')  # lees het bestand in.png in
    print("De eerste twee pixels van de eerste rij zijn", im_pix[0][0:2])
    #
    # Onthoud dat im_pix een lijst (de afbeelding) van
    # lijsten (elke rij) van lijsten (elke pixel is [R,G,B]) is
    #

    new_pix = [[change(pix) for pix in row] for row in im_pix] 

    new_pix = []
    for row in im_pix:
        new_row=[]
        for pixel in row:
            new_pixel = change(pixel)
            new_row+= [new_pixel]
        new_pix += [new_row]
    # sla nu het bestand 'out.png' op
    save_rgb(new_pix, 'out.png')


def make_row_column(r, c):
    new_list = [[0] * r for col in range(c)]
    return new_list

print(make_row_column(3, 5))


def remove_uneven_n(l):
    return [[nesteditem for nesteditem in item if nesteditem % 2 == 0]for item in l]

print(remove_uneven_n([[9,8,7],[1,2,4]]))