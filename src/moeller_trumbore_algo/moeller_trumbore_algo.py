# -*- coding: utf-8 -*-
"""
@author: Cristiano Pizzamiglio

"""

from typing import Union, Tuple
import numpy as np


def ray_triangle_intersection(
    vertices: np.ndarray,
    ray_origin: np.ndarray,
    ray_direction: np.ndarray,
    culling: bool = False,
    epsilon: float = 1e-6,
) -> Union[bool, Tuple[float, float, float]]:
    """
    Implementation of the Möller-Trumbore ray-triangle intersection algorithm.

    Parameters
    ----------
    vertices : np.ndarray
        2D array with the x, y and z coordinates of the triangle vertices as rows.
    ray_origin : np.ndarray
        Ray origin.
    ray_direction : np.ndarray
        Ray direction.
    culling : bool, optional
        If True, back facing triangles are discarded. When the ray hits the
        triangle from "behind" (the ray and the normal points in the same
        direction), the triangle is said to be back-facing. In this case the
        determinant is negative.
        The default is False.
    epsilon : float, optional
        Tolerance. The default is 1e-6.

    Returns
    -------
    Union[bool, Tuple[float, float, float]]
        If the ray and triangle do not intersect False is always returned.
        Otherwise, the distance and the barycentric coordinates u and v are returned.

    References
    ----------
    Möller, T., & Trumbore, B. (1997). Fast, minimum storage ray-triangle
    intersection. Journal of graphics tools, 2(1), 21-28.

    https://www.scratchapixel.com/lessons/3d-basic-rendering/ray-tracing-rendering-a-triangle/moller-trumbore-ray-triangle-intersection

    Examples
    --------

    >>> vertices = np.array([[0.0, 0.0, 0.0], [0.0, 10.0, 0.0], [10.0, 0.0, 0.0]])
    >>> ray_origin = np.array([1.0, 1.0, 1.0])
    >>> ray_direction = np.array([0.0, 0.0, -1.0])
    >>> intersection = ray_triangle_intersection(vertices, ray_origin, ray_direction)
    (1.0, 0.1, 0.1)

    """
    vertex_0 = vertices[0]
    vertex_1 = vertices[1]
    vertex_2 = vertices[2]

    edge_1 = vertex_1 - vertex_0
    edge_2 = vertex_2 - vertex_0

    p_vec = np.cross(ray_direction, edge_2)

    determinant = np.dot(p_vec, edge_1)

    if culling:
        if determinant < epsilon:
            return False

        t_vec = ray_origin - vertex_0
        u_ = np.dot(p_vec, t_vec)
        if u_ < 0.0 or u_ > determinant:
            return False

        q_vec = np.cross(t_vec, edge_1)
        v_ = np.dot(q_vec, ray_direction)
        if v_ < 0.0 or (u_ + v_) > determinant:
            return False

        inv_determinant = 1.0 / determinant
        t = np.dot(q_vec, edge_2) * inv_determinant
        u = u_ * inv_determinant
        v = v_ * inv_determinant

        return t, u, v

    else:
        if np.abs(determinant) < epsilon:
            return False

        inv_determinant = 1.0 / determinant

        t_vec = ray_origin - vertex_0
        u = np.dot(p_vec, t_vec) * inv_determinant
        if u < 0.0 or u > 1.0:
            return False

        q_vec = np.cross(t_vec, edge_1)
        v = np.dot(q_vec, ray_direction) * inv_determinant
        if v < 0.0 or (u + v) > 1.0:
            return False

        t = np.dot(q_vec, edge_2) * inv_determinant
        if t < epsilon:
            return False
        return t, u, v
