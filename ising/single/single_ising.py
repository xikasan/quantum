# coding: utf-8

import numpy as np
from absl import app, flags


FL = flags.FLAGS
flags.DEFINE_float("magnetic_field", 1., "Magnetic field [T]")
flags.DEFINE_float("temp", 10, "Temperature [K]")
flags.DEFINE_integer("iteration", 300, "")

kB = 1.38064852e-23


def entry(_):
    sigma = np.random.randint(2) * 2 - 1
    for i in range(FL.iteration):
        beta = FL.temp * (FL.iteration - i) / FL.iteration
        p = probability(sigma, beta)
        r = np.random.rand()
        if p > r:
            sigma *= -1
        print(
            "Step: {: 3.0f}".format(i),
            "beta: {:7.2f}".format(beta),
            "sigma: {: 2.0f}".format(sigma),
            ":", np.exp(-2/beta)
        )


def Hamiltonian(sigmas):
    return - FL.magnetic_field * sigmas


def probability(sigmas, beta):
    exp_sigmas = np.exp(- Hamiltonian(sigmas) / (beta + 1e-14))
    z_beta = np.sum(np.exp(Hamiltonian(1) / beta) + np.exp(Hamiltonian(-1) / beta))
    y = exp_sigmas / z_beta
    return y


if __name__ == '__main__':
    app.run(entry)
