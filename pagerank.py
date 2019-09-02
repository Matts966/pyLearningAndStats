import networkx as nx
import matplotlib.pyplot as plt

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


b = nx.DiGraph() # グラフオブジェクトの生成
# nodeの定義
b.add_node('a')
b.add_node('b')
b.add_node('c')
b.add_node('d')
b.add_node('e')
b.add_node('f')
b.add_node('g')
b.add_node('h')
# edgeの追加
b.add_edge('d', 'a')
b.add_edge('e', 'b')
b.add_edge('f', 'c')
b.add_edge('g', 'c')
b.add_edge('h', 'c')


c = nx.DiGraph() # グラフオブジェクトの生成
# nodeの定義
c.add_node('a1')
c.add_node('a2')
c.add_node('a3')
c.add_node('b1')
c.add_node('b2')
c.add_node('b3')
# edgeの追加
c.add_edge('a1', 'b1')
c.add_edge('a1', 'b2')
c.add_edge('a1', 'b3')
c.add_edge('a2', 'b1')
c.add_edge('a2', 'b2')
c.add_edge('a2', 'b3')
c.add_edge('a3', 'b1')
c.add_edge('a3', 'b2')
c.add_edge('a3', 'b3')


d = nx.DiGraph() # グラフオブジェクトの生成
# nodeの定義
d.add_node('c1')
d.add_node('c2')
d.add_node('c3')
d.add_node('c4')
d.add_node('c5')
d.add_node('d')
# edgeの追加
d.add_edge('c1', 'd')
d.add_edge('c2', 'd')
d.add_edge('c3', 'd')
d.add_edge('c4', 'd')
d.add_edge('c5', 'd')


e = nx.DiGraph() # グラフオブジェクトの生成
# nodeの定義
e.add_node('a')
e.add_node('b')
e.add_node('c')
e.add_node('d')
e.add_node('e')
e.add_node('f')
e.add_node('g')
e.add_node('h')
# edgeの追加
e.add_edge('a', 'b')
e.add_edge('a', 'c')
e.add_edge('b', 'd')
e.add_edge('b', 'e')
e.add_edge('c', 'f')
e.add_edge('c', 'g')
e.add_edge('d', 'h')
e.add_edge('d', 'a')
e.add_edge('e', 'h')
e.add_edge('e', 'a')
e.add_edge('f', 'a')
e.add_edge('g', 'a')
e.add_edge('h', 'a')



f = nx.DiGraph() # グラフオブジェクトの生成
# nodeの定義
f.add_node('a')
f.add_node('b')
f.add_node('c')
f.add_node('d')
f.add_node('e')
f.add_node('f')
f.add_node('g')
f.add_node('h')
# edgeの追加
f.add_edge('a', 'b')
f.add_edge('a', 'c')
f.add_edge('b', 'd')
f.add_edge('b', 'e')
f.add_edge('c', 'f')
f.add_edge('c', 'g')
f.add_edge('d', 'h')
f.add_edge('d', 'a')
f.add_edge('e', 'h')
f.add_edge('e', 'a')
f.add_edge('f', 'g')
f.add_edge('g', 'f')
f.add_edge('h', 'a')


g = nx.DiGraph() # グラフオブジェクトの生成
# nodeの定義
g.add_node('a')
g.add_node('b')
g.add_node('c')
# edgeの追加
g.add_edge('a', 'b')
g.add_edge('b', 'a')
g.add_edge('a', 'c')
g.add_edge('c', 'a')
g.add_edge('c', 'c')



h = nx.DiGraph() # グラフオブジェクトの生成
# nodeの定義
h.add_node('a')
h.add_node('b')
h.add_node('c')
h.add_node('d')
h.add_node('e')
# edgeの追加
h.add_edge('a', 'b')
h.add_edge('a', 'c')
h.add_edge('a', 'd')
h.add_edge('b', 'c')
h.add_edge('c', 'b')
h.add_edge('c', 'd')
h.add_edge('d', 'c')
h.add_edge('e', 'b')
h.add_edge('e', 'c')
h.add_edge('e', 'd')

graphs = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h}




def prSH(name, graph):
    print('---- result of', name, '----')

    try:
        pagerank = nx.pagerank(graph, alpha=1.0)
    except:
        pagerank = 0
    surf = nx.pagerank(graph, alpha=0.85)
    print('name', 'pagerank : ', pagerank)
    print('name', 'sf=0.85  : ', surf)
    h, a = nx.hits(graph)
    print('name', 'HITS hub : ', h)
    print('name', 'HITS auth: ', a)
    print()

    fig = plt.figure()
    fig.suptitle('---- result of ' + name + ' ----')
    count = 1
    for k, d in {'pagerank':pagerank, 'sf=0.85':surf, 'HITS hub':h, 'HITS auth':a}.items():
        if d == 0:
            count += 1
            continue

        plt.subplot(2, 2, count)
        plt.subplots_adjust(wspace=0.4, hspace=0.6)
        plt.title(k)
        plt.bar(range(len(d)), list(d.values()),
                tick_label=list(d.keys()))
        count += 1
    plt.savefig(name+'.png')
    plt.show()

if __name__ == '__main__':
    for name, graph in graphs.items():
        prSH(name, graph)
