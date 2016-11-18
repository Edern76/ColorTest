# ColorTest
Shows the result of various RGB combinations.  
Made with Python 3.5 using the TDL library.  
Use the right and left arrows in order to select a color to change and to change it's value. Pressing F1 brings up the help menu.

# Requirements
In order to run / compile the code, you'll need the following modules :  
- TDL (1.5.3 +) : https://pypi.python.org/pypi/tdl  
- Libtcod-cffi : https://pypi.python.org/pypi/libtcod-cffi/2.0a2  
- CFFI (1.8+) : https://pypi.python.org/pypi/cffi

In addition to these, if you want to compile this program using setup.py you'll need cx_Freeze : https://pypi.python.org/pypi/cx_Freeze

# Compiling
In order to compile for Windows, just run setup.py (or setupconda.py if you're using Anaconda, otherwise this will result in unecessary clutter in the binaries folder) with the argument "build" without quotation marks. Therefore, the full command looks like :   
```python setup.py build```  
At the moment, there is no build script for Linux or OSX.

# Binaries

Compiled Windows binaries available at the Releases page (https://github.com/Edern76/ColorTest/releases)
