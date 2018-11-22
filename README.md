# zBrac : A text paste utility for zTree
![weblogo](/visuals/img/png/weblogo.png)

Created by Ali Seyhun Saral and Anna Schröter  
Licensed under GNU General Public License v3.0 

## About the project

`zBrac`<sup>1</sup>is a tool designed for easy implementation of text and language files to `zTree` (Fischbacher,2007) treatment files.  With the software you can export "language files" in excel format from your zTree treatment files and import it back after the translation.

### Design

 `zBrac` works with two types of files:

- **Treatment files (txt)**: What we call a treatment file is a file exported from a treatment file in zTree treatment files or a modified version of the file by zBrac. 
- **Language files (xls):** These are the zBrac generated excel files. The first column contains keys(or original phrases) and the second column contains the relevant translation. 

#### Placeholder operator: [[ . ]]

`zBrac` assumes that any text to be translated in a treatment file is wrapped between two open and two close brackets. `[[text]]`. The limitation of the software that it does not recognize automatically the text in a ztree file. If your treatment file is already written, the sentences or text blocks to be translated should be encapsulated by `[[` and `]]`. If you will write a zTree treatment from scratch, it is better to write all the text in double brackets. You can easily strip them out by using zBrac.

## Installation
### Installation with pip (Windows, GNU/Linux, MacOS)
If you have Python(>=3.6) and pip on your computer you can install with
`pip install zbrac` 

Then `zbrac` command opens the software

### Installation with Windows Installer
You can download the installer here: 
[zBrac-1-0-3-win32-setup.exe](https://github.com/seyhunsaral/zbrac/raw/master/installer/Output/zBrac-1-0-3-win32-setup.exe)

## Contributing
Guidelines for contributing will be available soon.

[1] :  pronounced ˈzibrək, like zebra (that's where the logo comes from)
