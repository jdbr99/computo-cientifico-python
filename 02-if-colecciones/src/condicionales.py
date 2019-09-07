age = input("¿Cuál es tu edad?\n> ")
age = int(age)
if age > 18 and age < 80:
  print("Puedes pasar")
elif age >= 80 and age < 120:
  print("Adelante, anciano")
elif age >= 120:
  print("- お前はもう死んでいる!\n- なに?!")
else:
  print("Estás muy chavo!")