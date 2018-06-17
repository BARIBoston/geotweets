#!/usr/bin/env python3

import gzip
import json
import rtree
import shapely.geometry

class ShapeIndex(object):

    def __init__(self):
        self.index = rtree.index.Index()
        self.n_shapes = 0

    def add_geojson(self, path_to_geojson_gz):
        with gzip.open(path_to_geojson_gz, "r") as f:
            data = json.load(f)
            for shape_record in data["features"]:
                shape = shapely.geometry.shape(shape_record["geometry"])
                self.index.insert(
                    int(shape_record["properties"]["geoid"]),
                    shape.bounds,
                    obj = shape
                )
                self.n_shapes += 1

    def lookup_geoid(self, x, y):
        results = list(self.index.intersection((x, y), objects = True))
        if (len(results) == 1):
            return results[0].id
        else:
            point = shapely.geometry.Point(x, y)
            for result in results:
                if (result.object.contains(point)):
                    return result.id
