Introduction
------------

The Möller–Trumbore ray-triangle intersection algorithm_, named after its inventors Tomas Möller and Ben Trumbore, is a fast method for calculating the intersection of a ray and a triangle in three dimensions without needing precomputation of the plane equation of the plane containing the triangle.

.. _algorithm: https://www.tandfonline.com/doi/abs/10.1080/10867651.1997.10487468

Example Usage
-------------

>>> vertices = np.array([[0.0, 0.0, 0.0], [0.0, 10.0, 0.0], [10.0, 0.0, 0.0]])
>>> ray_origin = np.array([1.0, 1.0, 1.0])
>>> ray_direction = np.array([0.0, 0.0, -1.0])
>>> intersection = ray_triangle_intersection(vertices, ray_origin, ray_direction)
(1.0, 0.1, 0.1)

Acknowledgment
--------------
Wikipedia_, Scratchapixel_ and pyvista_

.. _Wikipedia: https://en.wikipedia.org/wiki/M%C3%B6ller%E2%80%93Trumbore_intersection_algorithm
.. _Scratchapixel: https://www.scratchapixel.com/lessons/3d-basic-rendering/ray-tracing-rendering-a-triangle/moller-trumbore-ray-triangle-intersection
.. _pyvista: https://docs.pyvista.org/examples/99-advanced/ray-trace-moeller.html
