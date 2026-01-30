"""
Improved Convergence Test - Extended Integration
Authors: Sabine Thöni, Claude (AI Assistant)
"""

from mpmath import mp, zetazero
from riemann_dynamical_symmetry import gradient_flow, defect_functional
import numpy as np

mp.dps = 30

def test_extended_integration(zero_idx=1, n_steps=200):
    """Test with longer integration time"""
    rho = zetazero(zero_idx)
    tau = float(rho.imag)
    
    print(f"\nExtended test for zero #{zero_idx} (τ={tau:.2f})")
    print(f"Integration steps: {n_steps}\n")
    
    sigma_inits = [0.25, 0.35, 0.45, 0.55, 0.65, 0.75]
    
    for sigma_init in sigma_inits:
        sigma_final = gradient_flow(sigma_init, tau, n_steps=n_steps, dt=0.5)
        D_final = defect_functional(sigma_final, tau)
        
        improvement = abs(sigma_init - 0.5) - abs(sigma_final - 0.5)
        pct = 100 * improvement / abs(sigma_init - 0.5)
        
        print(f"σ₀={sigma_init:.2f} → σ={sigma_final:.6f} "
              f"(improved {pct:.1f}%, D={D_final:.2e})")

if __name__ == "__main__":
    test_extended_integration(1, n_steps=200)
    test_extended_integration(10, n_steps=200)
