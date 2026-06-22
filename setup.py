from cx_Freeze import setup, Executable

executables =[
    Executable(
        script='app.py',
        base='Win32GUI',
        icon='TesteSis.ico',
        
        )
    ]

setup(
    name = "Gerenciador",
    version ="1.0",
    description = "Sistema Para akemiNT",
    executables = executables
    )