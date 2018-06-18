usage
=====

drop geojson files into the ./shapes/ directory for them to be made available

.. code-block:: python

    >>> import geotweets
    >>> geotweets.indices.list()
    continental_us_states: uninitialized
    boston: uninitialized
    continental_us_states_simplified: uninitialized
    boston_blockgroups: uninitialized
    >>> geotweets.indices["boston_blockgroups"].lookup_geoid(-71.0889958, 42.3383195)
    250250104051
    >>> geotweets.indices.list()
    continental_us_states: uninitialized
    boston: uninitialized
    continental_us_states_simplified: uninitialized
    boston_blockgroups: 651 shapes

