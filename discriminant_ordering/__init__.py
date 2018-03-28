#! /usr/bin/env python

import numpy as np

def heaviside(x):
    return 0.5 * (np.sign(x) + 1)


def filter2D(x, y, target, stats=False):
    x0 = x[target==0]
    x1 = x[target==1]
    y0 = y[target==0]
    y1 = y[target==1]
    return np.asarray(x0), np.asarray(y0), np.asarray(x1), np.asarray(y1)


def calc_DO(fx, gx, target, n_data):
    # Data is shuffled to select a random subset of the input
    data = np.vstack((fx, gx, target)).T
    np.random.seed(123)
    np.random.shuffle(data)

    # Reduce dataset to n_data size
    data = data[0:n_data]

    # Filter data into signal and background
    fx0, gx0, fx1, gx1 = filter2D(data[:,0], data[:,1], data[:,2])

    # Compute DO
    heavi_sum = 0
    for idx in range(len(fx0)):
        for idy in range(len(fx1)):
            heavi_side = heaviside( (fx0[idx] - fx1[idy]) * (gx1[idy] - gx0[idx]) )
            heavi_sum = heavi_side + heavi_sum
    return 2*(np.abs((float(1.0/len(fx0)) * float(1.0/len(gx0)) * heavi_sum) - 0.5))


def boot_strap(fx, gx, target, n_data, boot_loops):
    # Calculate uncertainty using bootstrap
    n_bootstraps = boot_loops
    rng_seed = 42  # control reproducibility
    bootstrapped_scores = []

    rng = np.random.RandomState(rng_seed)
    for i in range(n_bootstraps):
        # bootstrap by sampling with replacement on the prediction indices
        indices = rng.random_integers(0, n_data - 1, n_data)

        score = calc_DO(fx[indices], gx[indices], target[indices], len(fx[indices]))
        bootstrapped_scores.append(score)
        #print("Bootstrap #{} ROC area: {:0.3f}".format(i + 1, score))
        sorted_scores = np.array(bootstrapped_scores)
        sorted_scores.sort()

        # Computing the lower and upper bound of the 90% confidence interval
        # You can change the bounds percentiles to 0.025 and 0.975 to get
        # a 95% confidence interval instead.
        confidence_lower = sorted_scores[int(0.025 * len(sorted_scores))]
        confidence_upper = sorted_scores[int(0.975 * len(sorted_scores))]
        #print("Confidence interval for the score: [{:0.3f} - {:0.3}]".format(confidence_lower, confidence_upper))
    DO_mean = np.mean(bootstrapped_scores)
    DO_var = np.std(bootstrapped_scores)
    return DO_mean, DO_var


''' Main DO function '''
def DO(fx, gx, target, n_data, stats=False, boot_loops=100):
    if stats==True:
        return boot_strap(fx, gx, target, n_data, boot_loops)
    else:
        return calc_DO(fx, gx, target, n_data)

