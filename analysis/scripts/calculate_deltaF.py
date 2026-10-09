import numpy as np
import glob
import re

kBT = 2.494339

basin1 = (-3.05, -1.96)
basin2 = (-1.96, -0.85)

files = [
    f for f in glob.glob("fes_[0-9]*.dat")
    if re.fullmatch(r"fes_\d+\.dat", f)
]

files = sorted(
    files,
    key=lambda x: int(re.search(r'fes_(\d+)\.dat', x).group(1))
)

results = []

for f in files:
    data = np.loadtxt(f, comments="#")
    phi = data[:, 0]
    F = data[:, 1]

    F = F - np.min(F)

    mask1 = (phi >= basin1[0]) & (phi < basin1[1])
    mask2 = (phi >= basin2[0]) & (phi <= basin2[1])

    P1 = np.trapz(np.exp(-F[mask1] / kBT), phi[mask1])
    P2 = np.trapz(np.exp(-F[mask2] / kBT), phi[mask2])

    deltaF = -kBT * np.log(P1 / P2)

    n = int(re.search(r'fes_(\d+)\.dat', f).group(1))

    results.append((n, n * 200, deltaF))

np.savetxt(
    "deltaF_vs_time.dat",
    results,
    header="snapshot gaussian_count deltaF_kJmol"
)

print("snapshot  gaussians  DeltaF(kJ/mol)")
for row in results:
    print(f"{row[0]:8d} {row[1]:10d} {row[2]:14.6f}")
