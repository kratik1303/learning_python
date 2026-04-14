chai_type = " Ginger Chai "
customer_name = " Angel Agrawal "

print(f"Order for {customer_name} : {chai_type} please!!!!")

chai_description = "Aromatic and Bold"

print(f"First word is :{chai_description[0:8]}")
print(f"Last word is :{chai_description[12:]}")
print(f"Reverse word is :{chai_description[::-1]}")

label_txt = 'Chai_Sp$$cial'
encoded_label = label_txt.encode("UTF-8")

print(label_txt)
print(encoded_label)

decoded_label = encoded_label.decode("UTF-8")
 
print(decoded_label)