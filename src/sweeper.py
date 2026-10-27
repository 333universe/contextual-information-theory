import os
import csv
import numpy as np
from engine import TUMCalibratedEnginePRO

def execute_validation_sweep():
    # 1. Initialize directory tracking infrastructure
    os.makedirs("data", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    
    csv_filename = "data/tum_complete_analysis.csv"
    
    # 2. Instantiate engine configuration and baseline reproducible metrics
    base_bandwidth = 1000.0
    block_size = 96
    engine = TUMCalibratedEnginePRO(block_size=block_size, base_bandwidth=base_bandwidth)
    
    np.random.seed(42)  # Fixed seed enforces strict peer-review replication tracking
    raw_data = np.random.randint(0, 2, block_size)
    sector = block_size // 3
    
    # 3. Define the multi-order parametric noise distribution scaling boundary (0.01 -> 100.0)
    noise_steps = np.logspace(-2, 2, 50)
    
    print(f"======================================================================")
    print(f" CIT REPLICATION SUITE: EXECUTING PARAMETRIC NOISE BOUNDARY SWEEP     ")
    print(f"======================================================================")
    print(f" Target Sequence: 50 Log-Spaced Intervals | Block Size: {block_size} bits")
    print(f" Processing data arrays...")

    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Structural logging headers matching formal CIT manuscript variables
        writer.writerow([
            "Target_Noise_Power", 
            "NFL_Capacity_BPS", 
            "Bandwidth_NFL_Hz", 
            "Structural_Friction", 
            "Measured_BER", 
            "Semantic_Torque_Tau"
        ])
        
        for idx, noise in enumerate(noise_steps):
            # Forward matrix transfer calculation
            c_tum = engine.transmit_bitstream_frame(raw_data, noise)
            
            # Extract localized mathematical states matching current frame attributes
            S_ideal = np.array([
                np.sum(raw_data[0:sector]) / sector, 
                np.sum(np.diff(raw_data[sector:2*sector]) != 0) / (sector - 1), 
                np.sum(raw_data[2*sector:]) / sector
            ])
            signal_power = max(1e-6, np.sum(S_ideal**2))
            
            # Recalculate channel distortion boundaries
            N_vector = np.random.normal(0, np.sqrt(noise / 3.0), 3)
            S_received = S_ideal + N_vector
            actual_noise_power = max(1e-6, np.sum(N_vector**2))
            snr_linear = signal_power / actual_noise_power
            
            # Subspace isolation mapping tracking matrix state parameters
            S_projected = S_received - (N_vector * (1.0 / (1.0 + snr_linear)))
            structural_friction = max(1e-6, np.std(S_projected))
            
            tau = max(0.0, min(0.9999, 1.0 - np.exp(-0.5 * ((actual_noise_power / signal_power) / structural_friction))))
            bandwidth_nfl = engine.B_zero / (1.0 + engine.alpha * (np.linalg.norm(engine.Xi) * 1000.0))
            
            # Tripartite Receiver Decoder Emulation for BER Extraction
            decoded_bits = np.zeros_like(raw_data)
            decoded_bits[0:sector] = 1 if S_received[0] > 0.5 else 0
            decoded_bits[2*sector:] = 1 if S_received[2] > 0.5 else 0
            
            est_transitions = int(round(S_received[1] * (sector - 1)))
            s2_block = np.zeros(sector)
            curr_state = 0
            for i in range(sector):
                if i > 0 and est_transitions > 0 and i % (max(1, sector // (est_transitions + 1))) == 0:
                    curr_state = 1 - curr_state
                    est_transitions -= 1
                s2_block[i] = curr_state
            decoded_bits[sector:2*sector] = s2_block
            
            # Measure resulting error rate performance metrics
            bit_errors = np.sum(raw_data != decoded_bits)
            ber = bit_errors / block_size
            
            # Save historical step parameters to structured dataset file log
            writer.writerow([noise, c_tum, bandwidth_nfl, structural_friction, ber, tau])
            
            # Intermittent console tracking updates for the engineer
            if (idx + 1) % 10 == 0 or idx == 0:
                print(f" Step {idx+1:02d}/50 | Noise: {noise:8.4f} | Capacity: {c_tum:7.2f} bps | BER: {ber:.4f}")

    print(f"======================================================================")
    print(f" 🎉 SWEEP INTEGRATION COMPLETE                                        ")
    print(f" Reference evaluation record matrix successfully written to: {csv_filename}")
    print(f"======================================================================")

if __name__ == "__main__":
    execute_validation_sweep()
