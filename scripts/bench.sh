#!/bin/bash
set -exo pipefail

FACTORIO=/media/euclid/SteamLibrary/steamapps/common/Factorio/bin/x64/factorio

BENCHMARK=~/.factorio/saves/${1}

# 5x180s benchmark
# TICKS=10800
# 5m benchmark
# TICKS=18000
# 30m benchmark
TICKS=108000
# 60m benchmark
# TICKS=216000
RUNS=4

# ITEMS="metallurgic-science-pack"
ITEMS="cryogenic-science-pack"
# ITEMS="electromagnetic-science-pack"
# ITEMS="agricultural-science-pack"
# optional file prefix to limit benchmarking within a folder
PATTERN=" "
if [ -n "$2" ]; then
  PATTERN="--pattern=$2 "
fi

# 17% better performance from using my standard factorio wrapper on belt
LD_PRELOAD=/usr/lib/libmimalloc.so MIMALLOC_PAGE_RESET=0 MIMALLOC_LARGE_OS_PAGES=1 gamemoderun belt benchmark "${BENCHMARK}" --factorio-path=${FACTORIO} ${PATTERN} --ticks=${TICKS} --runs=${RUNS} --run-order random --output . --verbose-metrics wholeUpdate,gameUpdate,planetsUpdate,controlBehaviorUpdate,transportLinesUpdate,electricHeatFluidCircuitUpdate,electricNetworkUpdate,heatNetworkUpdate,fluidFlowUpdate,entityUpdate,particleUpdate,spacePlatforms,consistencyScraper,logisticManagerUpdate,constructionManagerUpdate,pathFinder,trains,trainPathFinder,commander,chartRefresh,luaGarbageIncremental,chartUpdate,scriptUpdate,tileHeatingUpdate
belt sanitize "${BENCHMARK}" --factorio-path="${FACTORIO}" --items "${ITEMS}" --verbose --ticks="${TICKS}" ${PATTERN}

# --verbose-metrics wholeUpdate,latencyUpdate,gameUpdate,planetsUpdate,controlBehaviorUpdate,transportLinesUpdate,lightningUpdate,mapGenerator,collectorNavMesh,collectorNavMeshPathfinding,collectorNavMeshRaycast,crcComputation,luaGarbageIncremental

python main_graph.py -f ./results.csv
