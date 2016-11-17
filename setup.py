from cx_Freeze import setup, Executable #, version
 
 
build_exe_options = {"packages": ["cffi"]} 
setup(
    name ='ColorTest',
    version ='1.0',
    description ='Shows the result of various RGB combinations.',
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py")],
    )