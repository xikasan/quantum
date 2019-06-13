# Ising Machine

Research recode of the ising model and quantum computing useing it.

## General Ising system

N-qubit system $\Lambda$ is considered.
Each qubit $q_k \in \Lambda$ has the spin $\sigma_k = \left\{ -1, +1 \right\}$, and the qubit spin configurationis  $\sigma = (\sigma_k)_{q_k \in \Lambda}$.
Then the Hamiltonian of this system is described as below:
$$
H(\sigma) = - \sum_{i \neq j \in \Lambda}J_{ij}\sigma_i \sigma_j - \sum_{i \in \Lambda} \mu_i \sigma_i
$$

where $J$ is an interaction factor between each qubit, and $\mu$ is a interaction with the magnetic field.

Probability of the spin state can be expressed using the Boltzman distribution as the follows:
$$
P_\beta(\sigma) = \frac{\exp\left(- \beta H(\sigma)\right)}{\sum_\sigma \exp\left(- \beta H(\sigma) \right)}
$$
where $\beta = 1/k_B T$ is the inverse of Boltzman coefficient and templeture. Denominator is a pertition function like as the normalizing factor which is a sum of all possible spin configuration.

## Single qubit model

First of all, let us consider most simple model, the single qubit ising system.
The configuration is $\sigma = \left\{\sigma_0=(-1) \: \or \: \sigma_1=(+1) \right\}$.
The Hamiltonian is written as below:
$$
H_1(\sigma) = - \mu \sigma = \left\{ \begin{array}{cc}
  - \mu & \sigma=\sigma_0 \\
    \mu & \sigma=\sigma_1
\end{array} \right.
$$

Probability of the configration is described as the following:
$$
P_\beta(\sigma) = \frac{\exp\left(-\beta H_1(\sigma)\right)}{\sum_{\sigma=\{\sigma_0, \sigma_1\}} \exp\left(-\beta H_1(\sigma)\right)} 
= \frac{\exp\left(-\beta H_1(\sigma)\right)}{Z_\beta}
= \left\{ \begin{array}{cc}
  \exp\left( \beta \mu\right)/Z_\beta & \sigma=\sigma_0 \\
  \exp\left(-\beta \mu\right)/Z_\beta & \sigma=\sigma_1
\end{array} \right.
$$
Where $Z_\beta = \exp(\beta \mu) + \exp(-\beta \mu)$ is the pertition function.