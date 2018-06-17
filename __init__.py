#!/usr/bin/env python3

import os

from .shape_index import ShapeIndex

indices = {}

shapes_dir = os.path.join(
    os.path.dirname(
        os.path.realpath(__file__)
    ),
    "shapes"
)

for geojson_gz in os.listdir(shapes_dir):
    index = ShapeIndex()
    index.add_geojson(os.path.join(shapes_dir, geojson_gz))
    indices[".".join(geojson_gz.split(".")[:-2])] = index

def list_indices():
    print("\n".join([
        "%s: %d shape%s" % (
            index_name, index.n_shapes, index.n_shapes == 1 and " " or "s"
        )
        for (index_name, index) in indices.items()
    ]))
