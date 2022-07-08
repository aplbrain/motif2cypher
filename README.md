# motif2cypher

A command-line executable to convert [DotMotif](https://github.com/aplbrain/dotmotif) syntax to Cypher (for use with Neo4j)

## Usage

```shell
python3 motif2cypher.py < tri.motif
```

## Arguments

| Argument        | Description                                                                                          |
| --------------- | ---------------------------------------------------------------------------------------------------- |
| `-f`,`--file`   | The input (`*.motif`) file to read from. If this is not specified, the program will read from stdin. |
| `-o`,`--output` | The output file to write to. If this is not specified, the program will write to stdout.             |
| `--neuprint`    | If this is specified, the program will write the output using the neuPrint data schema.              |
