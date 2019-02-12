#    This file is part of zBrac.
#
#    zBrac is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    zBrac is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with zBrac.  If not, see <https://www.gnu.org/licenses/>.


import zbrac.interface
import argparse
import sys

parser = argparse.ArgumentParser(description='zBrac')
parser.add_argument('name',
                    help='name of the file')
parser.add_argument('--version',action='store_true',
                    help='gives the version of zBrac')
parser.add_argument('-p',type=int,metavar='N',
                    help='do something with the int')

def main():
    args=parser.parse_args(sys.argv)
    
    if(args.version):
        print(zbrac.interface.titletext)
    if(args.p!=None):
        print('Hi '+str(args.p))
    if(len(sys.argv)==1):
        zbrac.interface.startgui()


if __name__ == '__main__':
    main()
