text = """Hello, today is an open day at our school! We invite you, your friends and relatives to visit our school!
          Today there will be open lessons on various interesting topics. In the assembly hall we organized a concert.
          The gym will host volleyball, foodball and basketball competitions.
       """

a = text.find('f')
b = text.rfind('f')


if a != -1:
   print(a)
if b != -1:
   print(b)
else:
   a or b == -1
   print("")
