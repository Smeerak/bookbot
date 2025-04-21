def count_words(book_string):
    rtr_count = 0
    read_list = []
    read_list = book_string.split()
    rtr_count = len(read_list)

    return(rtr_count)

def sort_on(dict):
    for key, value in dict.items(): #remembe you still have to itterate through key/value
        #print(key, value)
        return (value)

def count_character_frequency(book_string):
    rtr_count = 0
    rtr_dict = {}
    inc = 0

    #set the entire book to 'lowercase'
    book_string = book_string.lower()

    #print(f"length is: {len(book_string)}")   
    for i in range(0,len(book_string),1):
        char_comp = book_string[i]
        if(book_string[i] in rtr_dict):      
            inc = rtr_dict[book_string[i]]
            inc += 1
            rtr_dict[book_string[i]] = inc
        else:
            rtr_dict[book_string[i]] = 1
    #print (rtr_dict)
    return(rtr_dict)

def return_sorted_dict(dict):
    rtr_list = []
    alpha_count = 0;
    
    for i in dict:
        if(i.isalpha()):
            alpha_count += 1
            #print(f"{i}: {dict[i]}")
            rtr_list.append({i:dict[i]})

    #unsorted list of dictionaries rtr_list
    

    #we need to sort the list of dictionaries:
    rtr_list.sort(reverse=True, key=sort_on)

    return(rtr_list)
        
    





