# Single Qubit Ising system
Implementation of a ising system with single qubit.

## General Ising Model
The Hamiltonian of the N-qubit system is described as bellow:
$$
H = \sum_{i \neq j} J_{ij} \sigma_i \sigma_j + \sum_i \mu_i \sigma_i
$$
where $\sigma \in \{-1, +1\}$ is a spin of i-th qubit, $J_{ij}$ is a interaction, and $\mu_i$ is a interraction with magnetic field.
Normally, $J$ and $h$ have same values for evry qubit, respectively.
But here, to expand as qubit in the quantum computing in future, interaction and magnetic field effect are defined for each qubit.

Probability of the spin direction of the i-th qubit is described as the follows:
$$
P_\beta(\sigma) = \frac{\exp(-\beta H(\sigma))}{\sum_\sigma \exp (-\beta H(\sigma))}
$$
where $\beta = 1/k_B T$ is a Boltzmann distribution with inversed temperature $T$.

## Single qubit model

The Hamiltonian is written down as bellow:
$$
H_1=\mu\sigma
$$
This means that only magnetic field effects the spin of qubit
Then theh probability that a qubit spin becomes $|+1>$ is written as bellow:
$$
P_\beta(\sigma) = 1
$$



----------

$\left| 0 \right\rangle$

----------

# 単量子ビットイジングモデル

## 一般系イジングモデル

N量子ビット系のハミルトニアンは：
$$
H = \sum_{i \neq j} J_{ij} \sigma_i \sigma_j + \sum_i \mu_i \sigma_i
$$

ここで、 $\sigma \in \{-1, +1\}$はi番目の量子ビットのスピン、$J_{ij}$は量子ビット間相互作用、$\mu_i$は磁場との相互作用である。.
一様に量子ビットが配置されている場合の$J$、または一様磁場中の $h$はそれぞれ全ての量子ビットで同じ値をとる。
ただし、のちの量子計算への応用を考慮して、独立したパラメータとして導入する。

スピンが$|+1>$となる確率はハミルトニアンを用いて以下のように記述される：
$$
P_\beta(\sigma) = \frac{\exp(-\beta H(\sigma))}{\sum_\sigma \exp (-\beta H(\sigma))}
$$
ここで $\beta = 1/k_B T$ は温度$T$に依存いたボルツマン分布である。

## 単量子ビットイジングモデル

１量子ビット系のハミルトニアンは以下のように記述される:
$$
H_1=\mu\sigma
$$
すなわち、磁場からの相互作用によってのみその状態が定まる。この時の確率は

