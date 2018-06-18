#!/usr/bin/env python3

import os

from .shape_index import ShapeIndex

class LazyLoadIndices(object):

    def __init__(self):
        self.indices = {}
        self._shapes_dir = os.path.join(
            os.path.dirname(
                os.path.realpath(__file__)
            ),
            "shapes"
        )
        self._index_names = [
            ".".join(geojson.split(".")[:-1])
            for geojson in os.listdir(self._shapes_dir)
        ]

    def list(self):
        for index_name in self._index_names:
            if (index_name in self.indices):
                index = self.indices[index_name]
                print("%s: %d shape%s" % (
                    index_name, index.n_shapes, index.n_shapes == 1 and " " or "s"
                ))
            else:
                print("%s: uninitialized" % index_name)

    def __getitem__(self, key):
        if (not key in self._index_names):
            raise KeyError("no such index")
        elif (key in self.indices):
            return self.indices[key]
        else:
            index = shape_index.ShapeIndex()
            index.add_geojson(os.path.join(
                self._shapes_dir,
                "%s.geojson" % key
            ))
            self.indices[key] = index
            return index

indices = LazyLoadIndices()
