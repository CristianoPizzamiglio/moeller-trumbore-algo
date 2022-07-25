# -*- coding: utf-8 -*-
"""
@author: Cristiano Pizzamiglio

"""

import numpy as np
import pytest

from moeller_trumbore_algo import ray_triangle_intersection


vertices_1 = np.array([[0.0, 0.0, 0.0], [0.0, 10.0, 0.0], [10.0, 0.0, 0.0]])
ray_origin_1 = np.array([1.0, 1.0, 1.0])
ray_direction_1 = np.array([0.0, 0.0, -1.0])
culling_1 = False
intersection_expected_1 = (1.0, 0.1, 0.1)

vertices_2 = np.array([[0.0, 0.0, 0.0], [0.0, 10.0, 0.0], [10.0, 0.0, 0.0]])
ray_origin_2 = np.array([1.0, 1.0, 1.0])
ray_direction_2 = np.array([0.0, 0.0, -1.0])
culling_2 = True
intersection_expected_2 = False

vertices_3 = np.array([[0.0, 0.0, 0.0], [0.0, 10.0, 0.0], [10.0, 0.0, 0.0]])
ray_origin_3 = np.array([10.0, 10.0, 1.0])
ray_direction_3 = np.array([0.0, 0.0, -1.0])
culling_3 = False
intersection_expected_3 = False

vertices_4 = np.array([[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]])
ray_origin_4 = np.array([0.3, 0.25, 1.0])
ray_direction_4 = np.array([0.0, 0.0, -1.0])
culling_4 = False
intersection_expected_4 = (1.0, 0.25, 0.3)

vertices_5 = np.array([[0.0, 0.0, 0.0], [0.0, 10.0, 0.0], [10.0, 0.0, 0.0]])
ray_origin_5 = np.array([1.0, 1.0, 1.0])
ray_direction_5 = np.array([1.0, 0.0, 0.0])
culling_5 = True
intersection_expected_5 = False

vertices_6 = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
ray_origin_6 = np.array([0.0, 0.0, 0.0])
ray_direction_6 = np.array([-1.0, -1.0, -1.0])
culling_6 = False
intersection_expected_6 = False

vertices_7 = np.array([[0.0, 0.0, 0.0], [0.0, 10.0, 0.0], [10.0, 0.0, 0.0]])
ray_origin_7 = np.array([-1.0, -1.0, -1.0])
ray_direction_7 = np.array([0.0, 0.0, -1.0])
culling_7 = False
intersection_expected_7 = False


@pytest.mark.parametrize(
    ("vertices", "ray_origin", "ray_direction", "culling", "intersection_expected"),
    [
        (vertices_1, ray_origin_1, ray_direction_1, culling_1, intersection_expected_1),
        (vertices_2, ray_origin_2, ray_direction_2, culling_2, intersection_expected_2),
        (vertices_3, ray_origin_3, ray_direction_3, culling_3, intersection_expected_3),
        (vertices_4, ray_origin_4, ray_direction_4, culling_4, intersection_expected_4),
        (vertices_5, ray_origin_5, ray_direction_5, culling_5, intersection_expected_5),
        (vertices_6, ray_origin_6, ray_direction_6, culling_6, intersection_expected_6),
        (vertices_7, ray_origin_7, ray_direction_7, culling_7, intersection_expected_7),
    ],
)
def test_intersection(vertices, ray_origin, ray_direction, culling, intersection_expected):

    intersection = ray_triangle_intersection(vertices, ray_origin, ray_direction, culling)

    assert intersection == intersection_expected
    