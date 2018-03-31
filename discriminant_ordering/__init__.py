#! /usr/bin/env python

import numpy as np
import itertools

def heaviside(x):
    return 0.5 * (np.sign(x) + 1)

def norm(x):
    normed = (x-min(x))/(max(x)-min(x))
    return normed

def filter2D(fx, gx, target):
    fx0 = fx[target==0]
    fx1 = fx[target==1]
    gx0 = gx[target==0]
    gx1 = gx[target==1]
    return np.asarray(fx0), np.asarray(fx1), np.asarray(gx0), np.asarray(gx1)


def calc_DO(fx, gx, target, n_data):
    # normalize input data
    fx = norm(fx)
    gx = norm(gx)

    min_length = min(len(fx), len(gx))

    # Data is shuffled to select a random subset of the input
    data = np.vstack((fx[0:min_length], gx[0:min_length], target[0:min_length])).T
    np.random.seed(123)
    np.random.shuffle(data)

    # Reduce dataset to n_data size
    data = data[0:n_data]

    # Filter data into signal and background
    fx0, fx1, gx0, gx1 = filter2D(data[:,0], data[:,1], data[:,2])

    heavi_side = heaviside(np.multiply([(x-y) for x in fx0 for y in fx1 ],[(x-y) for x in gx0 for y in gx1 ]))

    return 2*(np.abs(((1.0/len(heavi_side)) * np.sum(heavi_side)) - 0.5))

def calc_DO_itertools(fx, gx, target, n_data):
    # This is an alternate way of calculating the DO. But testing has shown that it's about half as fast as the numpy approach
    # normalize input data
    fx = norm(fx)
    gx = norm(gx)

    min_length = min(len(fx), len(gx))

    # Data is shuffled to select a random subset of the input
    data = np.vstack((fx[0:min_length], gx[0:min_length], target[0:min_length])).T
    np.random.seed(123)
    np.random.shuffle(data)

    # Reduce dataset to n_data size
    data = data[0:n_data]

    # Filter data into signal and background
    fx0, fx1, gx0, gx1 = filter2D(data[:,0], data[:,1], data[:,2])

    heavi_side = heaviside(np.multiply(np.diff(list(itertools.product(fx0, fx1))),np.diff(list(itertools.product(gx0, gx1)))))

    return 2*(np.abs((float(1.0/len(heavi_side)) * np.sum(heavi_side)) - 0.5))

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
def DO(fx, gx, target, n_data=None, stats=False, boot_loops=100):
    if n_data == None:
        n_data = min(len(fx), len(gx))
    if stats==True:
        return boot_strap(fx, gx, target, n_data, boot_loops)
    else:
        return calc_DO(fx, gx, target, n_data)

