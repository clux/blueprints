# Benchmarking scripts

benchmarking wrapper around [`belt`](https://github.com/florishafkenscheid/belt) and visualisations via [`belt-charts`](https://github.com/abucnasty/belt-charts)

## Usage

Configure `bench.sh` with your benchmark params and game wrapper command (i use mimalloc + gamemode on linux).

```sh
./bench.sh save-subfolder-containing-saves 'optional-prefix*'
```

```sh
./chart.sh
```
