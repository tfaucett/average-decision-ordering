def calc_DO2(fx, gx, target, n_data):
    # normalize input data
    fx = norm(fx)
    gx = norm(gx)

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