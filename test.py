def printHello():
    print("Hello " + name)

name = "Vadiman"  # ← Конфликтующее изменение!
printHello()