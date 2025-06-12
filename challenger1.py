array = []
target = int(input("Digite o valor target: "))
while len(array) < 10:
    numeros = int(input("Digite o valor para adicionar a lista: "))
    array.append(numeros)
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i] + array[j] == target:
            print(f"[{array[i]},{array[j]}]")
            break