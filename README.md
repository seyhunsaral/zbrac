[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![PyPI version](https://badge.fury.io/py/zbrac.svg)](https://badge.fury.io/py/zbrac)


# zBrac : A multilanguage tool for zTree

![weblogo](/visuals/img/png/weblogo.png)


Created by Ali Seyhun Saral and Anna Schröter

Licensed under GNU General Public License v3.0


## About the project


zBrac<sup>1</sup>is a tool designed for easily modify the text of treatment files of z-Tree(Fischbacher,2007) treatment files.  With this software you can export specified text into "language files" import it back after the the text edit/translation.

zBrac is particularly useful when the tratment file contains same piece of text several times. This is very common as it is often needed to copy-paste stage tree elements in z-Tree.

## Design
### Keys
zBrac recognizes the text that are enclosed in double brackets: `[[This is a text]]`. Each piece of text that are double bracketed are called "**keys**".

Each key acts as a placeholder and later potentially to be replaced by another text.

To give an example, if you'd like to add a welcome message on your zTree file but you are not sure about the exact message at that point, you can just put `[[welcome message]]` on the appropriate place.

If your treatment file is already written, the 
sentences or text blocks to be translated should be enclosed by `[[` 
and `]]`. If you will write a zTree treatment from scratch, it is better 
to write all the text in double brackets. You can easily strip them out 
by using the *Strip Brackets* function of zBrac.

### Language files (xlsx)
A language file is an excel file which in each row contains a key as the first column, and a text to replace the key in the second column. For instance, once we have our welcome message, an excel file following the structure would allow us to replace the key:  

| (column1)  | (column2) |
| ------------- | ------------- |
| [[welcome message]]| Welcome to our experiment |



### Treatment files (txt)
Treatment files (TXT): Treatment files are basically zTree treatment files in TXT. They can be exported/imported using zTree.

## Example: Translating 

Here we demonstrate how to use zBrac by using a Holt & Laury Measure of Risk Aversion (Holt and Laury, 2002) from English to German.[2]

This is the english version we started with:

![zT-H&L-en](/visuals/img/png/zT-H&L-en.png)

First enclosed all the text we want to modify with double brackets. Now the file looks like this: 

![zT-H&L-zBrac](/visuals/img/png/zT-H&L-zBrac.png)

Then we exported the file to a text file by clicking: 
`File` then `Export` and `Treatment`.

After that we opened zBrac and choose the `Create Language File` function. This creates a template file that contains all the keys in the file.

![zB-CL](/visuals/img/png/zB-CL.png)

By clicking `Save language file as...` we created a language file to save.


This language file now looks like this:

![xlsx-en](/visuals/img/png/xlsx-en.png)

Then we translated the second column to german and saved it.

![xlsx-de](/visuals/img/png/xlsx-de.png)

After that we were able to use the second function of zBrac `Implement 
Language File`.

![zB-IL](/visuals/img/png/zB-IL.png)

We browsed for our treatment file.

![zB-IL-browse-treatment](/visuals/img/png/zB-IL-browse-treatment.png)

And for the translated language file.

![zB-IL-browse-language](/visuals/img/png/zB-IL-browse-language.png)

Then the filepaths were written in the `Load treatment File` and `Load 
language File` fields.

![zB-IL-selected](/visuals/img/png/zB-IL-selected.png)

We clicked `Save treatment file as...` to create a translated version of 
our treatment file and save it.

![zB-save-treatment](/visuals/img/png/zB-save-treatment.png)

Finaly we went back to zTree and choose `File` and then `Import` and 
selected our translated treatment file.

![zT-select-import](/visuals/img/png/zT-select-import.png)

This is what our result looks like.

![zT-H&L-ge](/visuals/img/png/zT-H&L-ge.png)


## Installation

### Installation with Windows Installer

You can download the installer here:

[zBrac-1-0-3-win32-setup.exe](https://github.com/seyhunsaral/zbrac/releases/download/v1.0.3/zBrac-1-0-3-win32-setup.exe)



### Installation with pip (Windows, GNU/Linux, MacOS)

If you have Python(>=3.6) and pip on your computer you can install with

`pip3 install zbrac` or `pip install zbrac`


Then `zbrac` command opens the software




## Contributing

Guidelines for contributing will be available soon.


[1] :  The name zBrac is a portmanteau of the words zTree and brackets. 
It is pronounced ˈzibrək, like zebra (that's where the logo comes from)

[2] : We used this sample file sentto the z-Tree mail group. Credits : Andreas Drichoutis
