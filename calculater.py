import os

os.system("color 9")

print("""
  SSSSSSSSSSSSSSS                                                              iiii  
 SS:::::::::::::::S                                                            i::::i 
S:::::SSSSSS::::::S                                                             iiii  
S:::::S     SSSSSSS                                                                   
S:::::S              aaaaaaaaaaaaa    aaaaaaaaaaaaa      mmmmmmm    mmmmmmm   iiiiiii 
S:::::S              a::::::::::::a   a::::::::::::a   mm:::::::m  m:::::::mm i:::::i 
 S::::SSSS           aaaaaaaaa:::::a  aaaaaaaaa:::::a m::::::::::mm::::::::::m i::::i 
  SS::::::SSSSS               a::::a           a::::a m::::::::::::::::::::::m i::::i 
    SSS::::::::SS      aaaaaaa:::::a    aaaaaaa:::::a m:::::mmm::::::mmm:::::m i::::i 
       SSSSSS::::S   aa::::::::::::a  aa::::::::::::a m::::m   m::::m   m::::m i::::i 
            S:::::S a::::aaaa::::::a a::::aaaa::::::a m::::m   m::::m   m::::m i::::i 
            S:::::Sa::::a    a:::::aa::::a    a:::::a m::::m   m::::m   m::::m i::::i 
SSSSSSS     S:::::Sa::::a    a:::::aa::::a    a:::::a m::::m   m::::m   m::::mi::::::i
S::::::SSSSSS:::::Sa:::::aaaa::::::aa:::::aaaa::::::a m::::m   m::::m   m::::mi::::::i
S:::::::::::::::SS  a::::::::::aa:::aa::::::::::aa:::am::::m   m::::m   m::::mi::::::i
 SSSSSSSSSSSSSSS     aaaaaaaaaa  aaaa aaaaaaaaaa  aaaammmmmm   mmmmmm   mmmmmmiiiiiiii

                    https://github.com/saaaami/calculator-script
                                                      
                                                      

            """)
print("")

for x in range(0,999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
   Num1 = int(input(" >                   Type Number 1 :"))
   print( " " )
   Amraz = input(" >                      + - / * : ")
   print( " " )
   Num2 = int(input(" >                   Type Number 2 :"))
   print(" ")
   
   
   if Amraz == "+":
     print("{ ",Num1, end="")
     print(" + ", end="")
     print(Num2, end=" = ")
     print(Num1 + Num2," } ")
     print(" ")
     print("----------------------------------------------------")
     print(" ")
     
     
   elif Amraz == "-":
     print("{ ",Num1, end="")
     print(" - ", end="")
     print(Num2, end=" = ")
     print(Num1 - Num2," } ")
     print(" ")
     print("----------------------------------------------------")
     print(" ")
     
     
   elif Amraz == "/":
     print("{ ",Num1, end="")
     print(" / ", end="")
     print(Num2, end=" = ")
     print(Num1 / Num2," } ")
     print(" ")
     print("----------------------------------------------------")
     print(" ")
     
     
   elif Amraz == "*":
     print("{ ",Num1, end="")
     print(" * ", end="")
     print(Num2, end=" = ")
     print(Num1 * Num2," } ")
     print(" ")
     print("----------------------------------------------------")
     print(" ")
     
     
   else:
     print("You have a error !!")
     print(" ")
     print("----------------------------------------------------")
     print(" ")



os.system("pause")
