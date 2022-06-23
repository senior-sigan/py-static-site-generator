from dataclasses import asdict, dataclass
import json
from pathlib import Path
from typing import List


@dataclass
class Edge:
    source: int
    target: int


@dataclass
class Node:
    id: int
    path: str
    label: str


@dataclass
class LinksGraph:
    edges: List[Edge]
    nodes: List[Node]


def build_graph(site) -> None:
    graph = LinksGraph(edges=[], nodes=[])
    for page in site['pages']:
        graph.nodes.append(Node(
            id=page['idx'],
            path=page['url'],
            label=page['title'] or ""
        ))

        for link in page['backlinks']:
            graph.edges.append(Edge(
                source=link['idx'],
                target=page['idx'],
            ))
    site['graph']['data'] = asdict(graph)


def save_graph(site) -> None:
    path = Path(site['graph']['dst']).absolute()
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(site['graph']['data']))


def apply(site) -> None:
    build_graph(site)
    save_graph(site)
