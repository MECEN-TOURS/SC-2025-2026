# Contenu séance 05

- `import networkx as nx`
- `nx.Graph` vs `nx.DiGraph`
- Construction par accumulation avec `Graph.add_edge` ou `Graph.add_node`
- Dessin avec `nx.draw_networkx` pour la version simple
- Notion de `hashable` pour pouvoir créer un sommet
- `@dataclass(frozen=True)` pour empêcher les mutations et être hashable
- Recherche d'un chemin avec `nx.shortest_path`
