import py2exe, os
from distutils.core import setup
setup(
    windows=[
        {
            "script": "ShowIP.py",
            "icon_resources": [(1, "ip.ico")]
        },
  ], 
    data_files=[
        (".",["ip.ico",]),
        (".",["gui.xrc",]),
	],
)

