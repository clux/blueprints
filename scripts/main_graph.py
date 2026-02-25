import os
import argparse
import pandas as pd
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--filepath", "-f", required=True, help="Path to the CSV file (e.g., ./results.csv)")
file_path = parser.parse_args().filepath

df = pd.read_csv(file_path)
print(df.to_string(index=False))

filtered_groups = []
mean_ups_dict = {}
for save_name, group in df.groupby("save_name"):
    mean_ups = group["effective_ups"].mean()
    lower_bound = mean_ups * 0.0
    upper_bound = mean_ups * 10.1
    filtered = group[(group["effective_ups"] >= lower_bound) & (group["effective_ups"] <= upper_bound)]
    removed = group[~group.index.isin(filtered.index)]
    mean_ups_filtered = filtered["effective_ups"].mean()
    mean_ups_dict[save_name] = mean_ups_filtered
    print(f"[{save_name}] Mean UPS: {mean_ups:.2f}, "
          f"after filtering: {mean_ups_filtered:.2f}, "
          f"deleted {len(removed)}/{len(group)} dots")
    filtered_groups.append(filtered)


df_filtered = pd.concat(filtered_groups, ignore_index=True)
sorted_save_names = sorted(mean_ups_dict, key=mean_ups_dict.get)
worst_avg_ups = min(mean_ups_dict.values())

fig, ax = plt.subplots()
plt.figure(figsize=(10, 6))

for save_name in sorted_save_names:
    group = df_filtered[df_filtered["save_name"] == save_name]
    mean_ups_filtered = mean_ups_dict[save_name]
    improvement_pct = (mean_ups_filtered - worst_avg_ups) / worst_avg_ups * 100
    plt.plot(group["run_index"], group["effective_ups"], marker=5,
        label=f"{save_name} (avg UPS: {mean_ups_filtered:.2f}, +{improvement_pct:.1f}%)")

plt.xlabel("Run index")
plt.ylabel("Effective UPS")
plt.title("UPS performance per run")
plt.legend()
plt.box(True)
plt.grid(True)
plt.tight_layout()

output_dir = os.path.dirname(file_path)
output_path = os.path.join(output_dir, "results.png")
plt.savefig(output_path, dpi=300)
