import webbrowser

def main():
        googleURL = "https://www.google.ca/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q="
        noOptions = True
        
        while(True):
                query = input("Enter your main search query here: ")
                options = input("Search Operators: Price, Hashtag, Remove, Exact \nEnter your search operators separated by commas here: ")                
                
                #Split the string on commas
                optionList = options.split(",")              
                
                #loop through options
                for option in optionList:
                        #Make the option lower case in case user enters capital letters and remove all whitespace
                        opt = option.replace(" ", "").lower()
                        if  opt == "remove":
                                query = queryRemove(query)
                                noOptions = False
                        else:
                                print (opt + " is not a valid option")
                
                #Alert the user that no operators selected
                if noOptions:
                        print ("No operators selected")
                
                print ("Your Query: " + query)
                
                if YorN("Search for query?"):
                        #Open the search query in the user's browser
                        webbrowser.open(googleURL + query)   
                
                if not YorN("Restart?"):
                        return False

#Add remove string to query
def queryRemove(queryR):
        removeStr = input("Enter the string you would like to remove from your query: ")
        queryR = queryR + " -" + removeStr
        return queryR
        
#Displays question and reutrns boolean, True if yes False if no
def YorN(DispStr):
        yornStr = input(DispStr + " (Y/N): ")
        
        if yornStr.lower() == "y":
                return True
        elif yornStr.lower() == "n":
                return False
        else:
                print ("Please enter either Y or N")
                YorN(DispStr)
        
                
if __name__ == "__main__":
        main()



        



