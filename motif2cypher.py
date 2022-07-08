from dotmotif import Motif
from dotmotif.executors.Neo4jExecutor import Neo4jExecutor
import sys

print(Neo4jExecutor.motif_to_cypher(Motif(sys.stdin.read())))
