#!/bin/bash
set -euxo pipefail

./belt-charts/dist/index.js boxplot '*.csv' \
   -w 1200 \
   -h 1200 \
   --remove-first-ticks 90000 \
   -o "charts/cryo_comp_box.png"
./belt-charts/dist/index.js summary '*.csv' \
  -w 1600 \
  -h 1600 \
  --remove-first-ticks 90000 \
  -o "charts/cryo_comp_summary.png" \
  --aggregate-strategy average \
  --summary-table true \
  --metrics "entityUpdate,heatNetworkUpdate,controlBehaviorUpdate,transportLinesUpdate,electricHeatFluidCircuitUpdate,electricNetworkUpdate,fluidFlowUpdate,luaGarbageIncremental" \
  --title-override "cryo_comp" \
  --summary-table-file true
