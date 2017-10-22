# -*- mode: python -*-

block_cipher = None

datas = [('GUI\\UI\\qss\\*.qss', 'GUI\\UI\\qss'),
('SDK', 'SDK'),
('setting\\*.pickle', 'setting'),
('setting\\*.json', 'setting'),
('setting\\configs', 'setting\\configs'),

('IMG\\G652\\pk\\*.BMP','IMG\\G652\\pk'),
('report\\*.css','report\\')]

a = Analysis(['cvon.py'],
             pathex=['D:\\MyProjects\\WorkProject\\opencv4fiber\\geomety'],
             binaries=[],
             datas=datas,
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
          exclude_binaries=True,
          name='cvon',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='cvon')
