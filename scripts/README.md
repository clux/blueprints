# Benchmarking scripts

python scripts to visualise csv data from [`belt`](https://github.com/florishafkenscheid/belt).

## Usage

Configure `start.sh` with your benchmark params and game wrapper command (i use mimalloc + gamemode on linux).

```sh
./start.sh
```

then prepare python deps / virtual env and

```sh
# main graph
python main_graph.py -f results.csv

# breakdown graph of a specific entry
python entity_graph.py --csv specific.csv --output specific-breakdown.png
```
