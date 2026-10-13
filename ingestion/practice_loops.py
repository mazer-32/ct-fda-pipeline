trial_phases = ["Phase 1", "Phase 2", "Phase 3", "Phase 2", "Phase 3", "Phase 3", "Phase 4"]

counts = {}
for phase in trial_phases:
    counts[phase] = counts.get(phase, 0) + 1

for phase, n in sorted(counts.items()):
    print(phase, n)
    print("Total trials:", len(trial_phases))