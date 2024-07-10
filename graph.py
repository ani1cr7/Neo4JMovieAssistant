# Connect to Neo4j
# Create the Neo4jGraph
#from langchain_community.graphs import Neo4jGraph

from py2neo import Graph

# Connect to the Neo4j database (replace with your credentials)
graph = Graph(
    host="3.8#.143.##",
    port=7687,
    user="neo4j",
    password="discard-market-colds"
)

