"""Script to input EEG signals in the form of .mat files and prepare
them for processing"""

import scipy.io
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data")

def mat_to_array(dir_name, cat, idx):
    """Convert .mat file to numpy array"""

    file_name = "%s/%s/%s_%s_segment_%04d.mat" % (BASE_DIR, dir_name,
                                                  dir_name, cat, idx)
    mat = scipy.io.loadmat(file_name)

    data = mat["%s_segment_%d" % (cat, idx)]
    signal = data['data'][0, 0]

    return signal

if __name__ == "__main__":
    print BASE_DIR
    SIGNAL = mat_to_array('Patient_1', 'preictal', 1)
    #plt.plot(SIGNAL[0, :100000])
    #plt.show()
