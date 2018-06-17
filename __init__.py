#!/usr/bin/env python3

import os

from .shape_index import ShapeIndex

index = ShapeIndex()
index.add_geojson(
    os.path.join(
        os.path.dirname(
            os.path.realpath(__file__)
        ),
        "shapes",
        "boston_blockgroups.geojson"
    )
)
