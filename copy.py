import shutil
import os
import sys

build_dir = "build" if os.path.exists("build") else "builddir"

src = "./Cactus.ModLoader/ExampleMod/"
dest = build_dir + "/Minecraft.Client/mods/ExampleMod"

try:
    shutil.copytree(src,dest,dirs_exist_ok=True)
    print("Copied example mod successfully")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(-1)