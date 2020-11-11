import pandas as pd
from collections import Counter
import nltk

# Tar bort varningarna för ett fel som vi kan ignorera
pd.options.mode.chained_assignment = None  # default='warn'

# Läser in vår data från csv filen
stackOverflow = pd.read_csv(
    './Data.csv',
    encoding='utf-8'
)

# Skriver ut storleken på vårt dataset
print('Number of Rows and Columns:')
print(stackOverflow.shape)

# Printar ut namnen på att columns som finns i datasetet
listOfColumnNames = stackOverflow.columns.values.tolist()
print('\nColumn names:')
for name in listOfColumnNames:
    print(name)

# Ändra här för att ta med fler columns in i dataFramen
df = stackOverflow[['AcceptedAnswerId', 'Title',
                    'CreationDate', 'Body']]

# Denna rad funkar inte men det som ska göras här är att om raden för AcceptedAnswerId inte är tom så ska raden bort då vi letar efter frågor utan
# ett accepterat svar
#df = df.loc[df['AcceptedAnswerId'] != '']

# Printar ut från vilka datum som vår data kommer ifrån
minValue = df['CreationDate'].min()
maxValue = df['CreationDate'].max()
print('\nDatum mellan vilka datan är tagen ifrån: ' +
      minValue + ' & ' + maxValue + '\n')


# Sätter värdena i title och body till lowercase
df['Title'] = df['Title'].str.lower()
df['Body'] = df['Body'].str.lower()


# Denna funkar men vi måste göra den mer sofistikerad då meningarna ofta hänger ihop med html taggarna och därmed inte tas bort
# Därför jag tex skrivit '<p>i' här nere för att visa att det funkar men detta måste kunna göras på ett bättre sätt.
# Kanske börja med att köra igenom koden och lägga till ett space efter och innan varje html tagg?
stopWords = ['code', 'gt', 'i', '<p>i']

# Tar bort alla stopWords från Body
df['Body'] = df['Body'].apply(lambda x: ' '.join(
    [word for word in x.split() if word not in (stopWords)]))

# Print för att testa stopWords funktionen
print('Testa StopWords funktionen: \n')
print(df['Body'].head(4) + '\n')

# Denna skapar en lista över de vanligaste orden. Du ändrar hur många ord den ska ta med genom variabeln här under
nrOfWords = 10
rslt = Counter(' '.join(df['Body']).split()).most_common(nrOfWords)

# Printar ut listan med de vanligaste orden
print('\n')
for word in rslt:
    print('{} = {}'.format(word[1], word[0]))
