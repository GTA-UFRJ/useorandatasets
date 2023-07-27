import numpy as np

def read_iq_values_from_binary_file(filename,num_elements):
    # Read the binary file into a numpy array of 32-bit floats
    data = np.fromfile(filename, dtype=np.float32, count=num_elements)

    # Reshape the data to split I and Q values into separate columns
    iq_data = data.reshape(-1, 2)

    # Create an array of tuples representing (I, Q) values
    iq_tuples = [tuple(iq_pair) for iq_pair in iq_data]

    return iq_tuples

# Example usage
if __name__ == "__main__":
    filename = "../CLEAR.bin"  # Replace with the actual file path
    iq_values = read_iq_values_from_binary_file(filename,40)
    print(iq_values)
