#ESERCIZIO 1) 
def list_to_dict(my_list) -> dict:
    l_lower = [i.lower for i in my_list] #trasformo tutti gli elementi della lista in lowercase
    
    """
    l_lower = []
    for i in my_list:
        l_lower.append(i.lower())
    """
    
    l_set = set(l_lower) #elimino i duplicati creando un insieme dalla lista (oggetti unici)
    l_dict = {i: 0 for i in l_set} 

    """
    l_dict = dict()
    l_dict = {}

    for i in l_set:
        l_dict[i] = 0    <--per ogni parola del set inizializza una coppia chiave valore in cui la parola è quella del set e il valore è 0
    """
    for word in l_lower: #Per ogni parola nella lista originale
        l_dict[word] += 1 #Se la parola è presente nella lista aggiungi uno al valore associato a quella chiave
    return l_dict

#ESERCIZIO 2)

def sum_sales(file):
    somma = 0
    my_file = open(file, 'r')
    for line in my_file:
        elements = line.split(',')

        if elements[0] != 'Date':
            value = elements[1]
            somma += float(value)
        print(f"La somma è uguale a: {somma}")
    my_file.close()
    return somma

file = 'shampoo_sales(in).csv'
sum_sales(file)

#ESERCIZIO 3

print('--------------------------')
def count_words(file, word):
    count = 0
    my_file = open(file, 'r')

    for line in my_file:
        if word in line: 
            count += 1
    my_file.close()
    print(count)
    return count

count_words('shampoo_sales(in).csv', 'Sales')

def count(file):
    my_file = open(file, 'r')
    list = []
    for line in my_file:
        elements = line.split(',')
        for element in elements:
            list.append(element)

    my_list = []
    for i in list:
        my_list.append(i.lower())
    
    my_set = set(my_list)

    my_dict = {}
    for idx in my_set:
        my_dict[idx] = 0
    
    for word in my_list:
        my_dict[word] += 1
    

    for word in my_dict:
        print(word, my_dict[word])

    my_file.close()

    return my_dict

count('shampoo_sales(in).csv')

