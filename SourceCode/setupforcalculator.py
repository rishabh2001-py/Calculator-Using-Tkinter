from cx_Freeze import  *

includefiles=['Blackvariant-Shadow135-System-Calculator.ico']
base=None
if sys.platform =="win32":
    base="Win32Gui"
shortcut_table=[("DesktopShortcut",
                "Desktopfolder",
                "MyCalculator",
                "TARGETDIR",
                "[TARGETDIR]\calcu.exe",
                 None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 "TARGETDIR",
                 )
]
msi_data={'Shortcut': shortcut_table}
bdist_msi_options={'data':msi_data }
setup(
    version="0.1",
    description="My calci",
    author="Rishabh",
    name= "CALCULATOR-RISHABH",
    options={'build_exe':{'include files':includefiles},"bdist_msi":bdist_msi_options,},
     executables=[
    Executable(
    script="calcu.py",
    base=base,
    icon='Blackvariant-Shadow135-System-Calculator.ico',
)
]
)

