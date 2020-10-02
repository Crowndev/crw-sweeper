# -*- mode: python -*-
import sys
import os
import os.path
import platform

block_cipher = None

os_type = sys.platform
base_dir = os.path.dirname(os.path.realpath('__file__'))

add_files = [
 ('img/screenshot.png','/img'),
 ('img/sweeper.ico','/img')
]

a = Analysis(['src/sweeper.py'],
             pathex=[base_dir],
             binaries=[],
             datas=add_files,
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
          name='CrownSweeper',
          debug=False,
          strip=False,
          upx=False,
          console=False,
          icon=os.path.join('img',('sweeper.%s' % ('icns' if os_type=='darwin' else 'ico'))))

if os_type == 'darwin':
    app = BUNDLE(exe,
                 name='CrownSweeper.app',
                 icon='img/sweeper.icns',
                 bundle_identifier=None,
                     info_plist={
                        'NSHighResolutionCapable': 'True'
                     }
                 )