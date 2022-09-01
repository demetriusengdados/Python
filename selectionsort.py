def selectionSort(list):
    for i in range(len(list) - 1): #Iteração n - 1
        minimun = i
        for j in range(i + 1, len(list)): #Compara os elementos i e i + 1
            if (list[j] < list[minimum]):
                minimum = j
        if(minimum != i):
            list[i], list[minimum] = list[minimum], list[i]
    return list

if __name__ == '__main__':
    list = [3,4,2,6,5,7,1,9,8]
    print('Lista Sorteada: ',selectionSort(list))