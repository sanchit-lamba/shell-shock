import jsbsim

initial_conditions = {
    'ic/vt-kts': 486,
    'ic/h-sl-ft': 40000,
    'ic/lat-gc-deg': 24.8430132946,
    'ic/long-gc-deg': 67.0544497822,
    'ic/psi-true-deg': 240.0,
    'ic/theta-deg': 0.0,
    'ic/phi-deg': 0.0,
    'ic/p-rad_sec': 0.0,
    'ic/q-rad_sec': 0.0,
    'ic/r-rad_sec': 0.0,
}

fdm = jsbsim.FGFDMExec(None)
fdm.load_script('scripts/mk82_script.xml')
for property, value in initial_conditions.items():
    fdm[property] = value

fdm.run_ic()

terrain_alt_ft = fdm['position/terrain-elevation-asl-ft']

while fdm.run():
    if fdm['position/h-sl-ft'] <= terrain_alt_ft:
        break

print("\n --- Ground Impact Detected ---")
print(f"Total Flight Time: {fdm['simulation/sim-time-sec']:.2f} seconds")
print(f"Impact Altitude (ASL): {fdm['position/h-sl-ft']:.2f} ft")
print(f"Horizontal Distance Traveled: {fdm['position/distance-from-start-mag-mt']:.2f} meters")