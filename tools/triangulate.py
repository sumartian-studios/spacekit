# Copyright (c) 2022 Sumartian Studios
#
# SpaceKit is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License v3.0.

from blender import bpy
from blender import bmesh

import glob

from pathlib import Path

# Load .glb files in the current working directory and output triangulated files
# that QtQuick3D can import into scenes.

for file in glob.glob("*.glb"):
    bpy.ops.wm.read_homefile(use_empty=True)

    # Import model...
    bpy.ops.import_scene.gltf(filepath=str(Path(file).resolve()))

    # Triangulate...
    for obj in bpy.data.objects:
        if obj.type == "MESH":
            me = obj.data
            bm = bmesh.new()
            bm.from_mesh(me)

            # Triangulate...
            bmesh.ops.triangulate(bm, faces=bm.faces[:])

            bm.to_mesh(me)
            bm.free()

    # Export model...
    bpy.ops.export_scene.gltf(
        export_format="GLB",
        export_colors=True,
        export_selected=False,
        export_yup=True,
        filepath=str(Path(file).resolve()),
    )
