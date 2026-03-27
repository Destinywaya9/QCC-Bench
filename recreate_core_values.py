import json
import numpy as np
import pandas as pd
from scipy.special import expi

optimized_alpha = 1.75608139162434
optimized_R0 = 4.999024146689842
optimized_beta = 0.260023414975139
optimized_spikes = [(5.356291525500936, 5.764583324405555, 1.9931930878883104), (9.237791026456424, 15.0, 0.05), (9.23715532560747, 15.0, 0.05), (2.6434115756261063, 1.9913212808549445, 1.9878940055179606), (2.5651949565486682, 2.191041928496458, 1.9063506290639705)]

def resonance_density(r, R0, beta):
    return R0 * np.exp(-beta * r)

def qtlet_age_multi_spike(r0, r_now, alpha, R0, beta, spikes):
    r_vals = np.linspace(r0, r_now, 2000)
    dS_total = alpha / r_vals
    for (A, r_spike, sigma) in spikes:
        dS_total += A * ((r_vals - r_spike) / (sigma ** 2)) * np.exp(-((r_vals - r_spike) ** 2) / (2 * sigma ** 2))
    R_vals = resonance_density(r_vals, R0, beta)
    integrand = dS_total / R_vals
    return np.trapz(integrand, r_vals)

print("Echo Meridian I:", qtlet_age_multi_spike(1.0, 22.0, optimized_alpha, optimized_R0, optimized_beta, optimized_spikes))
