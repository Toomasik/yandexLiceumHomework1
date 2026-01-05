import sys
import os
import shutil
from PyInstaller.utils.hooks import collect_dynamic_libs
from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT

# Данные проекта
datas = [
    ('data/coffee.db', 'data'),
    ('UI/main.ui', 'UI'),
    ('UI/addEditCoffeeForm.ui', 'UI'),
]

# Все нужные DLL берём из текущего Python 3.10
binaries = collect_dynamic_libs('')

# Анализ исходников
a = Analysis(
    ['main.py'],
    pathex=[os.path.abspath('.')],  # текущая папка
    binaries=binaries,
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False  # если хочешь консоль, поставь True
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    name='main',
)