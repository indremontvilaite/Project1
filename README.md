# Startup name generator	

Project task is to provide some name for Startup regarding user preferences. The user is asked for 4 input questions:
- Enter key words about Startup
- Choose one name style from given options: 
  - 1:"Person names like Chanel"
  - 2:"Rhyming words like SubHub and FireWire"
  - 3:"Real words like Apple and Always"
  - 4:"Foreign words like Iki and Toyota"
  - 5:"Multiple words like Facebook"
  - 6:"Misspelled words like Lyft"
- Choose how long name should be
- Choose how many suggestion user would like to get from a given range

To generate Startup names various methods are used:
- 1 style: program uses input data file *first_names.txt* and selects names randomly regarding given constrains.
- 2 style: program uses *pronouncing* package and key words about Startup.
- 3 style: program uses input data file *usa.txt* and  *nltk* package.
- 4 style: program uses *googletrans* package. Several languages are predefined.
- 5 style: program uses input data file *usa.txt* and selects names randomly regarding given constrains.
- 6 style: program misspells kye words about Startup.

Project output is a list with Startup name suggestions.

## How to start	
Program `code` is written in Python 3. The program uses *googletrans*, *nltk* and *wordnet* database, *pronouncing* and *random* packages. Before running the program, *googletrans*, *pronouncing*, *nltk* and  *wordnet* should be installed. 

``$ pip install googletrans``

More information about *googletrans* are available [here](https://pypi.org/project/googletrans/).

``$ pip install pronouncing``

More information about *pronouncing* are available [here](https://pypi.org/project/pronouncing/).

```
$ pip install --user -U nltk
$ python -m nltk.downloader wordnet
```

More information about *nltk* are available [here](https://www.nltk.org/install.html).

To start the project, run `main.py` file. You need to answer the given questions in order to recieve suggestions for Startup's name. *Usa.txt* and *first_names.txt* are input files to main.py program and have to be in the same folder as `main.py` file.

## Build status
Startup name selection algorithm uses a few python packages designed to analyse text. 6 style options are used in the algorithm and 2 output constrains(name's lenght and quantity of suggestions). 



