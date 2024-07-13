# Copyright (c) 2022 Sumartian Studios
#
# SpaceKit is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License v3.0.

bl_info = {
    "name": "SpaceKit",
    "description": "Blender utilities and nodes for science-fiction productions",
    "author": "Sumartian Studios",
    "version": (0, 0, 0),
    "blender": (3, 1, 0),
    "warning": "",
    "doc_url": "https://github.com/sumartian/spacekit",
    "category": "Interface",
}

import bpy
import os

from bpy.app.handlers import persistent


class State(object):
    asset_library_loaded = False


@persistent
def load_handler(dummy):
    if State.asset_library_loaded:
        return

    asset_dir = os.path.join(os.path.dirname(__file__), "assets")

    asset_libraries = bpy.context.preferences.filepaths.asset_libraries

    if "SpaceKit" in asset_libraries:
        asset_libraries["SpaceKit"].path = asset_dir
        State.asset_library_loaded = True
        return

    bpy.ops.preferences.asset_library_add(directory=asset_dir)

    for library in bpy.context.preferences.filepaths.asset_libraries:
        if library.path == asset_dir:
            library.name = "SpaceKit"
            State.asset_library_loaded = True
            return


def register():
    bpy.app.handlers.load_post.append(load_handler)


if __name__ == "__main__":
    register()
