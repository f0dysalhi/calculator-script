import os

os.system("color 3")

print("""
                    ================================
                    ===== >    Saaaami <33     <====
                    ================================

            """)
print("")

for x in range(0,999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
   Num1 = int(input("Type Number 1 :"))
   print( " " )
   Amraz = input("+ - / * : ")
   print( " " )
   Num2 = int(input("Type Number 2 :"))
   print(" ")
   
   
   if Amraz == "+":
     print("{ ",Num1, end="")
     print(" + ", end="")
     print(Num2, end=" = ")
     print(Num1 + Num2," } ")
     print(" ")
     print("...................................................")
     print(" ")
     
     
   elif Amraz == "-":
     print("{ ",Num1, end="")
     print(" - ", end="")
     print(Num2, end=" = ")
     print(Num1 - Num2," } ")
     print(" ")
     print("...................................................")
     print(" ")
     
     
   elif Amraz == "/":
     print("{ ",Num1, end="")
     print(" / ", end="")
     print(Num2, end=" = ")
     print(Num1 / Num2," } ")
     print(" ")
     print("...................................................")
     print(" ")
     
     
   elif Amraz == "*":
     print("{ ",Num1, end="")
     print(" * ", end="")
     print(Num2, end=" = ")
     print(Num1 * Num2," } ")
     print(" ")
     print("...................................................")
     print(" ")
     
     
   else:
     print("Error")
     print(" ")
     print("...................................................")
     print(" ")



os.system("pause")