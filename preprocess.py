from getNames import namesDF


def preprocess(names, train=True):

    names['name'] = names['name'].str.lower()  # lowercases
    names['name'] = [list(name)
                     for name in names['name']]  # splits by characters

    # makes all names have a length of 50
    nameLength = 50
    names['name'] = [(name + [' ']*nameLength)[:nameLength]
                     for name in names['name']]

    # change characrteers to numberes
    names['name'] = [[max(0, ord(char)-96)for char in name]
                     for name in names['name']]

    if train:
        # encode the gender to a number (if female 0 if male 1)
        names['gender'] = [0 if gender ==
                           'F' else 1 for gender in names['gender']]

    return names


processedNamesDF = preprocess(namesDF)
processedNamesDF.head()
print(processedNamesDF)
