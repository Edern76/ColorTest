from cx_Freeze import setup, Executable #, version

build_exe_options = {"packages": ["cffi"]}
bdist_msi_options = {'add_to_path' : True}

setup(
    name ='ColorTest',
    version ='1.0',
    description ='Shows the result of various RGB combinations.',
    options = {"build_exe": build_exe_options, "bdist_msi": bdist_msi_options},
    executables = [Executable("main.py")],
    )#This is a test comment