from dotmotif import Motif
from dotmotif.executors.Neo4jExecutor import Neo4jExecutor
from dotmotif.executors.NeuPrintExecutor import NeuPrintExecutor
import sys
import argparse

if __name__ == "__main__":
    """
    Pass a motif file as an argument to this script as `-f`. If no file
    is passed, the script will attempt to read from stdin.

    You can also pass `--neuprint` to use the NeuPrint executor.

    """
    parser = argparse.ArgumentParser(
        description="Convert a dotmotif motif to a cypher query"
    )
    parser.add_argument(
        "-f", "--file", help="File to read from. If not passed, read from stdin."
    )
    parser.add_argument(
        "-o",
        "--output",
        help="File to write to. If not specified, output will be written to stdout.",
    )
    parser.add_argument(
        "--neuprint", help="Use the NeuPrint executor", action="store_true"
    )
    args = parser.parse_args()

    if args.file:
        with open(args.file) as f:
            motif = Motif(f.read())
    else:
        motif = Motif(sys.stdin.read())

    if args.neuprint:
        E = NeuPrintExecutor
    else:
        E = Neo4jExecutor

    cypher = E.motif_to_cypher(motif)
    if args.output:
        with open(args.output, "w") as f:
            f.write(cypher)
    else:
        print(cypher)
