import json
from difflib import get_close_matches
data=json.load(open("data.json"))
query=input("Enter any word: ")

#functon to do the searching
def search(query):
    query1=query.lower()
    query2=query.upper()
    if query in data:   #if exact match is found
        for x in data[query]:
            print(x)
    elif query1 in data:  #if exact lower case is matched
        for x in data[query1]:
            print(x)
    elif query2 in data:    #else if Exact upper case is matched
        for x in data[query2]:
            print(x)
    else:                   #searching for similar words
        if len(get_close_matches(query,data.keys(),n=1,cutoff=0.8)) > 0:
            result=(get_close_matches(query1,data.keys(),n=1,cutoff=0.8))[0]
            input2=str(input("%s is the word you were looking for? If yes Press Y else N: " %result))
            if input2 is 'Y':
                for x in data[result]:
                    print(x)
            else:
                print("Try Again!")
        else:
            print("Sorry this word doesn't exists!")

search(query)
