import math
import numpy as np

angle_deg=314.3 # Example angle in degrees

center_stn=(-10.63,-0.04, -3.61)  # Example origin point
contact_point= (-9.81, -2.58, -5.37)  # Example contact point





# Calculate the angle in radians
angle_rad = math.radians(angle_deg)  # Convert angle to radians

sin_value = math.sin(angle_rad)  # Calculate sine of the angle
cos_value = math.cos(angle_rad)  # Calculate cosine of the angle

# Print the sine and cosine values
print(f"sin({angle_deg}) = {sin_value}")
print(f"cos({angle_deg}) = {cos_value}")

def subtract_points(point1, point2):
    x_diff = point1[0] - point2[0]
    y_diff = point1[1] - point2[1]
    z_diff = point1[2] - point2[2]
    return (x_diff, y_diff, z_diff)


result = subtract_points(contact_point, center_stn)  # Subtract the origin from the contact point
print(f"Result of subtracting origin from contact_point: {np.round(result, 2)}")

matrix = np.array([[cos_value, -sin_value, 0],
                   [sin_value, cos_value, 0],
                   [0, 0, 1]])  # Rotation matrix for Z-axis rotation
#print(f"Rotation matrix:\n{matrix}")
vector = np.array(result)  # Convert the result to a numpy array
rotated_vector = np.dot(matrix, vector)  # Apply the rotation matrix to the vector
rotated_vector_rounded = np.round(rotated_vector, 2)  # Round the result to 2 decimal places
print(f"the resulted of multipling matrix with vector is: {rotated_vector_rounded}")


distance =np.sqrt(np.sum(rotated_vector_rounded**2))  # Calculate the distance from the origin
distance_rounded = np.round(distance, 2)  # Round the distance to 2 decimal places
print(f"Distance from the origin of STN: {distance_rounded}")
    