import json
from pathlib import Path


def build_graph(site) -> None:
    graph = {'edges': [], 'nodes':[]}
    for page in site['pages']:
        graph['nodes'].append({
            'id': page['idx'],
            'path': page['url'],
            'label': page['title'] or "",
        })

        for link in page['backlinks']:
            graph['edges'].append({
                'source': link['idx'],
                'target': page['idx'],
            })
    site['graph']['data'] = graph


def save_graph(site) -> None:
    path = Path(site['graph']['dst']).absolute()
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(site['graph']['data']))


def apply(site) -> None:
    build_graph(site)
    save_graph(site)
