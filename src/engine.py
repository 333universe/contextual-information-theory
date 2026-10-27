import numpy as np

class TUMCalibratedEnginePRO:
    def __init__(self, block_size=96, base_bandwidth=1000.0, alpha_latency=0.003):
        """
        Initializes the Next-Gen CIT Tripartite Unitary Matrix (TUM) Engine.
        """
        self.B_zero = base_bandwidth
        self.block_size = block_size
        self.phi_catalyst = 0.0001
        self.alpha = alpha_latency
        self.Xi = np.zeros((3, 3))
        self.gamma_decay = 0.15
        
        # Formally defining the anti-symmetric transformation tensor (Infinitesimal Rotation)
        self.Phi = np.array([
            [ 0.0,    0.0001, -0.0001], 
            [-0.0001,  0.0,    0.0001], 
            [ 0.0001, -0.0001,  0.0   ]
        ])
        
    def transmit_bitstream_frame(self, raw_bits, target_noise_power):
        """
        Transmits raw bits through the TUM channel, computes dynamic thermodynamic 
        metrics, and applies the No-Free-Lunch capacity equation.
        """
        # 1. Apply memory tensor decay profile
        self.Xi *= (1.0 - self.gamma_decay)
        sector = self.block_size // 3
        
        # 2. Structural Feature Extraction across Tripartite Sectors
        S_ideal = np.array([
            np.sum(raw_bits[0:sector]) / sector, 
            np.sum(np.diff(raw_bits[sector:2*sector]) != 0) / (sector - 1), 
            np.sum(raw_bits[2*sector:]) / sector
        ])
        signal_power = max(1e-6, np.sum(S_ideal**2))
        
        # 3. Inject Vector Channel Gaussian Distortions
        N_vector = np.random.normal(0, np.sqrt(target_noise_power / 3.0), 3)
        S_received = S_ideal + N_vector
        actual_noise_power = max(1e-6, np.sum(N_vector**2))
        snr_linear = signal_power / actual_noise_power
        snr_db = 10 * np.log10(snr_linear)
        
        # 4. Denoised Subspace Projection for Structural Friction Isolation
        S_projected = S_received - (N_vector * (1.0 / (1.0 + snr_linear)))
        structural_friction = max(1e-6, np.std(S_projected))
        
        # 5. Thermodynamic Semantic Torque Parameter Calculation
        tau = max(0.0, min(0.9999, 1.0 - np.exp(-0.5 * ((actual_noise_power / signal_power) / structural_friction))))
        
        # 6. Rotational Shear Tensor Alignment mapping via Phi Matrix
        if tau > 0.05: 
            rotated_noise = N_vector + np.dot(self.Phi, N_vector)
            self.Xi += tau * np.outer(rotated_noise, rotated_noise)
            
        # 7. Dynamic Invariant Shortfall Calculation
        epsilon = max(0.0001, min(0.9999, 1.0000 - (np.mean(np.abs(S_received)) + self.phi_catalyst)))
        
        # 8. No-Free-Lunch Bandwidth Scaling Execution
        bandwidth_nfl = self.B_zero / (1.0 + self.alpha * (np.linalg.norm(self.Xi) * 1000.0))
        sigmoidal_guardrail = 1.0 / (1.0 + np.exp(0.5 * snr_db))
        
        # 9. Compute TUM Capacity Bound Envelope
        denominator = (actual_noise_power * (1.0 - tau)) + ((1.0 - epsilon) * signal_power * sigmoidal_guardrail)
        c_tum_nfl = bandwidth_nfl * np.log2(1.0 + (signal_power / max(1e-6, denominator)))
        
        return c_tum_nfl
