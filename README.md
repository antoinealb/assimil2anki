# Convert Assimil MP3 files to Anki Decks

This simple script lets you couvert Assimil lessons into Anki decks in case you
want to learn a bit more intensely like I do. The foreign language sentences
are taken from the metadata of Assimil's MP3 files, so you will need those. The
translation in the native language will have to be input by you, as I don't
have an automated way to extract those.

## Installation

You will need to install dependencies required for parsing MP3 files:

```shell
$ pip install -r requirements.txt
```

Or alternatively you can install `python-mutagen` from your distribution
package manager.

## Usage

You can run `assimil2anki` by pointing it at a folder containing Assimil
lessons, and giving it a CSV file as output, which we will later import into
Anki. You can get a list of options by running `assimil2anki.py --help`.

Run it as follow:

```shell
$ ./assimil2anki.py ~/Desktop/Assimil\ Polski/L008-Polish\ ASSIMIL/ -o ~/lesson08.csv
```

The tool will start asking you for translations in the order given in the
course book, which should allow you to quickly input them. While you can edit
input while typing, there is no way to go back and edit them later, but that is
easy to do in the CSV file.

Once you have the CSV file, you can go to Anki, then follow those steps:

1. Click "Import file" and choose the CSV file generated above.
1. Make sure that "Deck" is correct and that card type is set to "Basic and reversed".
1. In the Field Mapping section, make sure that the tags column is assigned. This will allow you to find those cards in your collection easily.
