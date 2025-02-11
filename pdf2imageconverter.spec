# -*- mode: python ; coding: utf-8 -*-
import os


# バージョン情報取得
with open("version.txt", "r") as f:
    version_name = f.read().strip()

block_cipher = None
tool_name = 'pdf2imageconverter' + '-ver' + version_name

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[
    ],
    datas=[
        ("poppler/Library/bin", "poppler/Library/bin"),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    exclude_binaries = True,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='pdf2imageconverter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=tool_name,
)

