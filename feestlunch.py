croisantje = 0.39
stokbrood = 2.78
kortingsbon = -0.50
print ("Croisantjes kopen")
croisantjes =float(input ('aantal croisantjes: '))
print (croisantjes * croisantje) 
print ("stokbroodjes kopen")
stokbrooden = float(input ("aantal stokbrooden: "))
print (stokbrooden * stokbrood) 
print ("heeft u kortings bonnen?")
kortingsbonnen =float(input ("Hoeveel kortings bonnen: "))
print (kortingsbonnen * kortingsbon)
print ("Het subtotaal is: ")
print (croisantje * croisantjes + stokbrood * stokbrooden + kortingsbon * kortingsbonnen)