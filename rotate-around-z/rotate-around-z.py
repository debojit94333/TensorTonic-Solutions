import numpy as np

def rotate_around_z(points, theta):
    """
    Rotate 3D point(s) around the Z-axis by angle theta (radians).
    """
    # Your code here
    points = np.asarray(points, dtype = float)
    single = (points.ndim == 1)
    if single:
        points = np.reshape(points, (1, 3))
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    x = points[:, 0]
    y = points[:, 1]
    z = points[:, 2]
    x_dash = x * cos_theta - y * sin_theta
    y_dash = x * sin_theta + y * cos_theta
    result = np.column_stack([x_dash, y_dash, z])

    if single:
        return result[0]
    return result