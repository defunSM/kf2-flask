# returns ID of the steamworkshop mod from a url
def getWorkShopId(text):
    if ("steam" and "&" in text):
        id = text.split("?id=")[1].split("&")[0] # Extracts ID
        if ( len(id) == 10 ):                    # Checks if ID is 10 digits long
            return id                            # Returns ID if passes validation
        else:
            print("Invalid URL or ID")

    elif ("steam" in text):                      # Similar but if url doesnt contain trialing characters
        id = text.split("?id=")[1]
        if ( len(id) == 10 ):
            return id
        else:
            print("Invalid URL or ID")

    elif ( len(text) == 10 ):                    # Condition for if the ID is given
        id = text                                # Simply sets the text to the Id and no spliting done
        return text

    else:
        print("Invalid URL or ID")

# text = "https://steamcommunity.com/sharedfiles/filedetails/?id=1819268190&searchtext="

# id = getWorkShopId(text)
# print(id)