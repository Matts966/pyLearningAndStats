import networkx as nx
a = nx.DiGraph() # グラフオブジェクトの生成

# nodeの定義
a.add_node('a')
a.add_node('b')
a.add_node('c')
a.add_node('d')
a.add_node('e')

# edgeの追加
a.add_edge('a', 'c')
a.add_edge('b', 'c')
a.add_edge('b', 'd')
a.add_edge('b', 'e')

graphs = [a]# , b, c, d, e, f, g, h]

def prSH(graph):
    print('----result of ', next((k for k, v in list(locals().items()) if v == graph)), '----')
    print('pagerank : ', nx.pagerank(graph, alpha=1.0))
    print('sf=0.85  : ', nx.pagerank(graph, alpha=0.85))

    h, a = nx.hits(graph)
    print('HITS hub : ', h)
    print('HITS auth: ', a)
    print()

if __name__ == '__main__':
    for graph in graphs:
        prSH(graph)

