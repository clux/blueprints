import sys
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_and_filter(csv_path: Path, run_val, tick_range=(0.0, 1.0), max_columns=None):
    df = pd.read_csv(csv_path)
    df_run = df[df["run"].astype(int) == int(run_val)].copy()
    if df_run.empty:
        raise ValueError(f"No rows found for run={run_val}")
    total_ticks_run = len(df_run)
    start_idx = int(len(df_run) * tick_range[0])
    end_idx = int(len(df_run) * tick_range[1])
    df_range = df_run.iloc[start_idx:end_idx].reset_index(drop=True)
    num_original_ticks = len(df_range)

    all_columns = [c for c in df_range.columns if c not in ("run", "tick")]
    excluded_cols = set(PARAM_COLUMNS + ["wholeUpdate", "latencyUpdate", "gameUpdate"])
    other_columns = [c for c in all_columns if c not in excluded_cols]
    if other_columns:
        df_range["other"] = df_range[other_columns].sum(axis=1)
    else:
        df_range["other"] = 0.0

    df_range_ms = df_range.copy()
    df_range_ms[PARAM_COLUMNS] /= 1_000_000
    df_range_ms = df_range.copy()
    df_range_ms[PARAM_COLUMNS] = df_range_ms[PARAM_COLUMNS] / 1_000_000
    if max_columns and len(df_range) > max_columns:
        group_size = len(df_range) / max_columns
        df_approx = []
        for i in range(max_columns):
            start = int(i * group_size)
            end = int((i + 1) * group_size)
            group_mean = df_range.iloc[start:end][PARAM_COLUMNS].mean()
            df_approx.append(group_mean)
        df_final = pd.DataFrame(df_approx)
        df_final["run"] = run_val
        df_final["tick"] = np.linspace(start_idx, end_idx, max_columns).astype(int)
    else:
        df_final = df_range.copy()
    df_final[PARAM_COLUMNS] = df_final[PARAM_COLUMNS].apply(pd.to_numeric, errors="coerce").fillna(0.0)
    return df_final, num_original_ticks, total_ticks_run, df_range_ms


def plot_stacked_bars(df: pd.DataFrame, csv_name, tick_range, num_original_ticks,
                      total_ticks_run, df_range_ms, run_val=0, output_path: Path = None, dpi=150):
    if "tick" in df.columns:
        x = df["tick"].astype(str).tolist()
    else:
        x = [str(i) for i in range(len(df))]
    n = len(x)
    ind = np.arange(n)
    bottoms = np.zeros(n)
    plt.style.use('dark_background')
    plt.figure(figsize=(12, 6), facecolor='black')
    try:
        cmap = plt.colormaps["tab20"]
    except AttributeError:
        from matplotlib import cm
        cmap = cm.get_cmap("tab20")
    num_params = len(PARAM_COLUMNS)
    colors = [cmap(i % cmap.N) for i in range(num_params)]
    df_ms = df.copy()
    df_ms[PARAM_COLUMNS] = df_ms[PARAM_COLUMNS] / 1_000_000
    for i, col in enumerate(PARAM_COLUMNS):
        values = df_ms[col].to_numpy(dtype=float)
        plt.bar(ind, values, bottom=bottoms, width=0.8, label=col, color=colors[i])
        bottoms += values
    mean_values = {col: df_ms[col].mean() for col in PARAM_COLUMNS}
    legend_labels = [
        (f"{col}: {mean_values[col]:.2f}, "
         f"{df_range_ms[col].min():.2f}, "
         f"{df_range_ms[col].max():.2f}")
        for col in PARAM_COLUMNS
    ]
    plt.text(
        n + 4, bottoms.max() * 1.1,
        "Legend numbers: mean, min, max (ms)",
        color='white',
        va='top',
        ha='left',
        fontsize=10
    )
    plt.xticks(ind, x, rotation=45, ha="right", color='white')
    plt.ylabel("Value (ms)", color='white')
    plt.title(f"{csv_name.split('/')[-1]}, run={run_val}", color='white')
    plt.legend(
        legend_labels,
        bbox_to_anchor=(1.02, 1),
        loc="upper left",
        fontsize="small",
        ncol=1,
        facecolor='black',
        labelcolor='white',
        frameon=True,
        edgecolor='white'
    )
    sec_analyzed = num_original_ticks / 60
    sec_total = total_ticks_run / 60
    info_text = (f"Run index: {run_val}\n"
                 f"Tick range: {tick_range[0]*100:.1f}% - {tick_range[1]*100:.1f}%\n"
                 f"Ticks analyzed: {num_original_ticks} ({sec_analyzed:.2f} s)\n"
                 f"Total ticks in run: {total_ticks_run} ({sec_total:.2f} s)")
    plt.text(n + 4, 0, info_text, color='white', va='center', ha='left', fontsize=10)
    plt.gca().ticklabel_format(style='plain', axis='y')
    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=dpi, bbox_inches="tight", facecolor='black')
        print(f"Saved plot to {output_path}")
    else:
        plt.show()


def parse_args():
    p = argparse.ArgumentParser(description="Plot stacked bars from a CSV for a selected run")
    p.add_argument("--csv", default="./data.csv", help="Path to input CSV file")
    p.add_argument("--run", type=int, default=0, help="Run index: 0+")
    p.add_argument("--tick-range", default="0.05-1", help="Tick range: 0.0-1.0")
    p.add_argument("--columns", type=int, default=60, help="Columns number on graph")
    p.add_argument("--output", default=None, help="If provided, save graph")
    p.add_argument("--dpi", type=int, default=150, help="Output DPI when saving image")
    return p.parse_args()

# PARAM_COLUMNS = [
#     "wholeUpdate", "latencyUpdate", "gameUpdate", "planetsUpdate", "controlBehaviorUpdate",
#     "transportLinesUpdate", "electricHeatFluidCircuitUpdate", "electricNetworkUpdate",
#     "heatNetworkUpdate", "fluidFlowUpdate", "entityUpdate", "lightningUpdate",
#     "tileHeatingUpdate", "particleUpdate", "mapGenerator", "mapGeneratorBasicTilesSupportCompute",
#     "mapGeneratorBasicTilesSupportApply", "mapGeneratorCorrectedTilesPrepare",
#     "mapGeneratorCorrectedTilesCompute", "mapGeneratorCorrectedTilesApply",
#     "mapGeneratorVariations", "mapGeneratorEntitiesPrepare", "mapGeneratorEntitiesCompute",
#     "mapGeneratorEntitiesApply", "spacePlatforms", "collectorNavMesh",
#     "collectorNavMeshPathfinding", "collectorNavMeshRaycast", "crcComputation",
#     "consistencyScraper", "logisticManagerUpdate", "constructionManagerUpdate",
#     "pathFinder", "trains", "trainPathFinder", "commander", "chartRefresh",
#     "luaGarbageIncremental", "chartUpdate", "scriptUpdate",
# ]

# PARAM_COLUMNS = [
#     "entityUpdate", "controlBehaviorUpdate", "transportLinesUpdate", "electricHeatFluidCircuitUpdate",
#     "fluidFlowUpdate", "spacePlatforms", "logisticManagerUpdate", "constructionManagerUpdate",
#     "trains", "trainPathFinder",
# ]
PARAM_COLUMNS = [
"entityUpdate",
"controlBehaviorUpdate",
"transportLinesUpdate",
"electricHeatFluidCircuitUpdate",
"electricNetworkUpdate",
"heatNetworkUpdate",
"fluidFlowUpdate",
"particleUpdate",
"spacePlatforms",
# "consistencyScraper",
# "logisticManagerUpdate",
# "constructionManagerUpdate",
# "pathFinder",
"trains",
# "trainPathFinder",
# "commander",
# "chartRefresh",
# "luaGarbageIncremental",
# "chartUpdate",
# "scriptUpdate",
]

PARAM_COLUMNS = [*PARAM_COLUMNS, "other"]

def main():
    args = parse_args()
    csv_path = Path(args.csv)
    if not csv_path.exists():
        print(f"CSV file not found: {csv_path}", file=sys.stderr)
        sys.exit(2)
    start_frac, end_frac = map(float, args.tick_range.split('-'))
    tick_range = (start_frac, end_frac)
    try:
        df, num_original_ticks, total_ticks_run, df_range_ms = \
            load_and_filter(csv_path, args.run, tick_range, args.columns)
    except Exception as e:
        print(f"Error loading/filtering CSV: {e}", file=sys.stderr)
        sys.exit(3)
    out = Path(args.output) if args.output else None
    plot_stacked_bars(df, args.csv, tick_range, num_original_ticks,
                      total_ticks_run, df_range_ms, output_path=out, dpi=args.dpi)


if __name__ == "__main__":
    main()
