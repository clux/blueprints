#!/bin/bash
set -euxo pipefail

FACTORIO=/media/euclid/SteamLibrary/steamapps/common/Factorio/bin/x64/factorio

BENCHMARK=~/.factorio/saves/${1}

# 5x180s benchmark
TICKS=10800
# TICKS=108000
RUNS=5

# 17% better performance from using my standard factorio wrapper on belt
LD_PRELOAD=/usr/lib/libmimalloc.so MIMALLOC_PAGE_RESET=0 MIMALLOC_LARGE_OS_PAGES=1 gamemoderun belt benchmark "${BENCHMARK}" --factorio-path=${FACTORIO} --ticks=${TICKS} --runs=${RUNS} --run-order random --output . --verbose-metrics wholeUpdate,gameUpdate,planetsUpdate,controlBehaviorUpdate,transportLinesUpdate,electricHeatFluidCircuitUpdate,electricNetworkUpdate,heatNetworkUpdate,fluidFlowUpdate,entityUpdate,particleUpdate,spacePlatforms,consistencyScraper,logisticManagerUpdate,constructionManagerUpdate,pathFinder,trains,trainPathFinder,commander,chartRefresh,luaGarbageIncremental,chartUpdate,scriptUpdate,tileHeatingUpdate

# --verbose-metrics wholeUpdate,latencyUpdate,gameUpdate,planetsUpdate,controlBehaviorUpdate,transportLinesUpdate,lightningUpdate,mapGenerator,collectorNavMesh,collectorNavMeshPathfinding,collectorNavMeshRaycast,crcComputation,luaGarbageIncremental

python main_graph.py -f ./results.csv
