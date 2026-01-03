class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph = defaultdict(list)
        cities = []

        for path in paths:
            start, dest = path
            graph[dest].append(start)
            cities.extend(graph[dest])

        for city in graph.keys():
            if city not in cities:
                return city