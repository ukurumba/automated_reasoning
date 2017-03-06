# -*- mode: python -*-

block_cipher = None


a = Analysis(['tests\\tests.py'],
             pathex=['D:\\ukuru\\Documents\\Classes_Spring_2016\\csc_242\\projects\\automated_reasoning'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='tests',
          debug=False,
          strip=False,
          upx=True,
          console=True )
