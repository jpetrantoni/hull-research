import numpy as np

# Gradient descent optimization


def gradient_descent(path, learning_rate, temperature, cooling_rate):
    # Calculate the initial cost
    initial_cost = cost(path)

    # Initialize the best path and cost
    best_path = path
    best_cost = initial_cost

    # Initialize the current path and cost
    current_path = path
    current_cost = initial_cost

    # Initialize the number of iterations
    num_iterations = 0

    # Run the optimization loop
    while temperature > 1e-6:
        # Update the number of iterations
        num_iterations += 1

        # Calculate the new path
        new_path = update_path(
            current_path, learning_rate, temperature)

        # Calculate the new cost
        new_cost = cost(new_path)

        # Calculate the cost difference
        cost_difference = new_cost - current_cost

        # If the new cost is better, then update the current path and cost
        if cost_difference > 0:
            current_path = new_path
            current_cost = new_cost

        # If the new cost is worse, then update the current path and cost with a probability
        else:
            probability = np.exp(cost_difference / temperature)
            if np.random.random() < probability:
                current_path = new_path
                current_cost = new_cost

        # If the new cost is better than the best cost, then update the best path and cost
        if new_cost > best_cost:
            best_path = new_path
            best_cost = new_cost

        # Update the temperature
        temperature *= cooling_rate

    # Print the number of iterations
    print("Number of iterations:", num_iterations)

    # Return the best path and cost
    return best_path, best_cost

# Simulated annealing optimization


def simulated_annealing(path, learning_rate, temperature, cooling_rate):
    # Calculate the initial cost
    initial_cost = cost(path)

    # Initialize the best path and cost
    best_path = path
    best_cost = initial_cost

    # Initialize the current path and cost
    current_path = path
    current_cost = initial_cost

    # Initialize the number of iterations
    num_iterations = 0

    # Run the optimization loop
    while temperature > 1e-6:
        # Update the number of iterations
        num_iterations += 1

        # Calculate the new path
        new_path = update_path(
            current_path, learning_rate, temperature)

        # Calculate the new cost
        new_cost = cost(new_path)

        # Calculate the cost difference
        cost_difference = new_cost - current_cost

        # If the new cost is better, then update the current path and cost
        if cost_difference > 0:
            current_path = new_path
            current_cost = new_cost

        # If the new cost is worse, then update the current path and cost with a probability
        else:
            probability = np.exp(cost_difference / temperature)
            if np.random.random() < probability:
                current_path = new_path
                current_cost = new_cost

        # If the new cost is better than the best cost, then update the best path and cost
        if new_cost > best_cost:
            best_path = new_path
            best_cost = new_cost

        # Update the temperature
        temperature *= cooling_rate

    # Print the number of iterations
    print("Number of iterations:", num_iterations)

    # Return the best path and cost
    return best_path, best_cost

# Update the path


def update_path(path, learning_rate, temperature):
    # Calculate the number of points in the path
    num_points = len(path)

    # Calculate the number of dimensions
    num_dimensions = len(path[0])

    # Calculate the number of points to update
    num_points_to_update = np.random.randint(1, num_points)

    # Choose the points to update
    points_to_update = np.random.choice(
        num_points, num_points_to_update, replace=False)

    # Calculate the number of dimensions to update
    num_dimensions_to_update = np.random.randint(1, num_dimensions)

    # Choose the dimensions to update
    dimensions_to_update = np.random.choice(
        num_dimensions, num_dimensions_to_update, replace=False)

    # Calculate the new path
# Calculate the new path
    new_path = path

    for i in range(num_points_to_update):
        point = points_to_update[i]

        for j in range(num_dimensions_to_update):
            dimension = dimensions_to_update[j]

            try:
                new_path[point][dimension] += np.random.normal(
                    scale=learning_rate * temperature)
            except:
                pass

    # Return the new path
    return new_path


def angle_between_vectors(vector1, vector2):
    # Calculate the dot product
    dot_product = np.dot(vector1, vector2)

    # Calculate the length of the vectors
    length_vector1 = np.linalg.norm(vector1)
    length_vector2 = np.linalg.norm(vector2)

    # Calculate the angle
    angle = np.arccos(dot_product / (length_vector1 * length_vector2))

    # Return the angle
    return angle


def cost(path):
    # Calculate the number of points in the path
    num_points = len(path)

    # Calculate the number of dimensions
    num_dimensions = len(path[0])

    # Initialize the total cost
    total_cost = 0

    # Loop over all points in the path
    for point in range(num_points):
        # Loop over all dimensions
        for dimension in range(num_dimensions):
            # Check if the point and dimension indices are within the bounds of the array
            if point >= 0 and point < num_points and dimension >= 0 and dimension < num_dimensions:
                # Add the cost of the current point and dimension to the total cost
                try:
                    total_cost += (path[point][dimension] -
                                   path[point-1][dimension]) ** 2
                except:
                    pass

    # Return the total cost
    return total_cost
