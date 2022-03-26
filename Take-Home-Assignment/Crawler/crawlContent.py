from ProductDetails.productDetailsCPs import pdCP
from ProductDetails.productDetailsDDV import pdDDV
from ProductDetails.productDetailsFPTS import pdFPTS
from ProductDetails.productDetailsGearVN import pdGVN
from ProductDetails.productDetailsTGDD import pdTGDD
def crawlContent(links):
    for key , value in links.items():
        if(key == 'thegioididong'):
            pdTGDD(value)
        elif(key == 'cellphones'):
            pdCP(value)
        elif(key == 'fptshop'):
            pdFPTS(value)
        elif(key == 'didongviet'):
            pdDDV(value)
        elif(key == 'gearvn'):
            pdGVN(value)
        else:
            continue