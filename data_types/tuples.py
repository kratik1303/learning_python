masala_spices  = ('cardamom','cloves','cinamon')

spice1,spice2,spice3 = masala_spices

print (f"Main Masala spices : {spice1},{spice2},{spice3}")

ginger_ratio,cardamom_ratio = 2,1 

print(f"Ratio of ginger is {ginger_ratio} and the ratio of cardamom is {cardamom_ratio}")

ginger_ratio,cardamom_ratio = cardamom_ratio , ginger_ratio

print(f"Ratio of ginger is {ginger_ratio} and the ratio of cardamom is {cardamom_ratio}")

#Membership testing 

print(f"Lets find out something in masala_spices,{'ginger' in masala_spices}")

## TUPLES ARE CASE_SENSITIVE 
## TUPLES ARE IMMUTABLE 
## TUPLES have a () symbol 