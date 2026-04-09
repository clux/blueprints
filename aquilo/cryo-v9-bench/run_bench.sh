#!/bin/bash
set -exo pipefail

FACTORIO=/media/euclid/SteamLibrary/steamapps/common/Factorio/bin/x64/factorio

NAME="cryo-5stack"
BENCHMARK=~/.factorio/saves/${NAME}

# 4x30m benchmark
TICKS=108000
RUNS=4

LD_PRELOAD=/usr/lib/libmimalloc.so MIMALLOC_PAGE_RESET=0 MIMALLOC_LARGE_OS_PAGES=1 gamemoderun belt benchmark "${BENCHMARK}" --factorio-path=${FACTORIO} --ticks=${TICKS} --runs=${RUNS} --run-order random --output . --verbose-metrics wholeUpdate,gameUpdate,planetsUpdate,controlBehaviorUpdate,transportLinesUpdate,electricHeatFluidCircuitUpdate,electricNetworkUpdate,heatNetworkUpdate,fluidFlowUpdate,entityUpdate,particleUpdate,spacePlatforms,consistencyScraper,logisticManagerUpdate,constructionManagerUpdate,pathFinder,trains,trainPathFinder,commander,chartRefresh,luaGarbageIncremental,chartUpdate,scriptUpdate,tileHeatingUpdate

ITEMS="cryogenic-science-pack"
belt sanitize "${BENCHMARK}" --factorio-path="${FACTORIO}" --items "${ITEMS}" --verbose --ticks="${TICKS}"
