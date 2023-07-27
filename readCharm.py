#This file is an example of how to use the I/Q samples dataset available
# in http://hdl.handle.net/2047/D20423481

import numpy as np

def read_iq_values_from_binary_file(filename,nrSamples):
    # Read the binary file into a numpy array
    # dtype='<f4' means 32-bit floats with little endian
    data = np.memmap(filename, dtype='<f4', mode='r')

    #Select a subset fromt the data, based on the number of required samples
    datasubset = data[0:nrSamples*2]

    # Reshape the data to split I and Q values into separate columns
    iq_data = datasubset.reshape(-1, 2)

    # Create an array of tuples representing (I, Q) values
    iq_tuples = [tuple(iq_pair) for iq_pair in iq_data]

    return iq_tuples


# Example usage
if __name__ == "__main__":
    filename = "../LTE_1M.bin"  # Replace with the actual file path
    numberIQSamples=40 # Replace with the number of IQ samples you want to read.
    iq_samples = read_iq_values_from_binary_file(filename,numberIQSamples)
    print(iq_samples)
