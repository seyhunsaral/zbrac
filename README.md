[![License: GPL 
v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[![PyPI 
version](https://badge.fury.io/py/zbrac.svg)](https://badge.fury.io/py/zbrac)


# zBrac : A multilanguage tool for zTree

![weblogo](/visuals/img/png/weblogo.png)


Created by Ali Seyhun Saral and Anna Schröter

Licensed under GNU General Public License v3.0


## About the project


`zBrac`<sup>1</sup>is a tool designed for easy implementation of text 
and language files to `zTree` (Fischbacher,2007) treatment files.  With 
the software you can export "language files" in excel format from your 
zTree treatment files and import it back after the translation.


### Design


`zBrac` works with two types of files:


- **Treatment files (txt)**: What we call a treatment file is a file 
exported from a treatment file in zTree treatment files or a modified 
version of the file by zBrac.

- **Language files (xls):** These are the zBrac generated excel files. 
The first column contains keys(or original phrases) and the second 
column contains the relevant translation.


#### Placeholder operator: [[ . ]]


`zBrac` assumes that any text to be translated in a treatment file is 
wrapped between two open and two close brackets. `[[text]]`. The 
limitation of the software that it does not recognize automatically the 
text in a ztree file. If your treatment file is already written, the 
sentences or text blocks to be translated should be encapsulated by `[[` 
and `]]`. If you will write a zTree treatment from scratch, it is better 
to write all the text in double brackets. You can easily strip them out 
by using zBrac.


## Installation

### Installation with Windows Installer

You can download the installer here:

[zBrac-1-0-3-win32-setup.exe](https://github.com/seyhunsaral/zbrac/releases/download/v1.0.3/zBrac-1-0-3-win32-setup.exe)



### Installation with pip (Windows, GNU/Linux, MacOS)

If you have Python(>=3.6) and pip on your computer you can install with

`pip install zbrac`


Then `zbrac` command opens the software


## Example

Here we will show you how we translated a simple Holt & Laury experiment 
from english to german.

This is the english version we started with.

![zT-H&L-en](/visuals/img/png/zT-H&L-en.png)

First we found all text elements in the zTree file and wrapped them in 
double brackets.

![zT-H&L-zBrac](/visuals/img/png/zT-H&L-zBrac.png)

Then we exported this bracketed version to a text file by clicking 
`File` then `Export` and `Treatment`.

![zT-save-export](/visuals/img/png/zT-save-export.png)

After that we opened zBrac and choose the `Create Language File` function.

![zB-CL](/visuals/img/png/zB-CL.png)

We clicked `browse` to browse for our exported treatment file.

![zB-CL-browse](/visuals/img/png/zB-CL-browse.png)

Now the filepath of our treatment file is written in the `Load treatment 
File` field.

![zB-CL-selected](/visuals/img/png/zB-CL-selected.png)

By clicking `Save language file as...` we created a language file to save.

![zB-save-language](/visuals/img/png/zB-save-language.png)

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



## Contributing

Guidelines for contributing will be available soon.


[1] :  The name zBrac is a portmanteau of the words zTree and brackets. 
It is pronounced ˈzibrək, like zebra (that's where the logo comes from)
