__author__ = 'mohamed_abdul_huq_ismail'

class Graph:
    nodes = None
    size = 0
    edges = 0

    def __init__(self):
        self.nodes = {}
    
    def addNode(self,s):
        self.nodes[s.topic] = s
        self.size += 1
        
    def getNode(self,s):
        try:
            return self.nodes[s]
        except KeyError:
            return None
    
    def addEdge(self,s,t):
        if t not in s.children:
            s.children.append(t)
            self.edges += 1

    def addQuestions(self,s,question):
        s.questions.append(question)

    def printGraph(self):
        for n in self.nodes:
            print self.nodes.index(n)
            print 'Parent: {}'.format(n.topic)
            for child in n.children:
                print 'Child {}'.format(child.topic)
            print 'Questions {}'.format(n.questions)
        
class Node:
    topic = ''
    children = None
    questions = None
    def __init__(self,topic):
        self.topic = topic
        self.children = []
        self.questions = []
        
def constructTree(g,topics):
    parent = None
    p = []

    for i in range(1,len(topics)):
        if topics[i] == '(':
            parent = topics[i-1]
            if parent not in p:
                p.append(parent)
        elif topics[i] == ')':
            if parent == p[len(p)-1]:
                p.pop()
            if len(p) != 0:
                parent = p[len(p) - 1]
        else:
            g.addEdge(g.getNode(parent),g.getNode(topics[i]))
        

def addPropertyQuestions(g,questions):
    for q in questions:
        x = q.split(':')
        g.addQuestions(g.getNode(x[0]),x[1].strip())

def findQuestions(g,topic,query):
    try:
        topicsChecked = set([])
        queue = []
        queryCount = 0
        queue.append(topic)

        while len(queue) != 0:
            t = queue.pop(0)
            topicsChecked.add(t)
            for q in t.questions:
                if q[:len(query)] == query:
                    queryCount += 1
            for c in t.children:
                if c not in topicsChecked:
                    queue.append(c)

        return queryCount

    except:
        return 0

def countQueries(g,queries):
    for q in queries:
        q = q.split(' ',1)
        print findQuestions(g,g.getNode(q[0]),q[1])
    
if __name__ == '__main__':
    # Read input from stdin
    numberOfTopics = int(raw_input())
    parseTree = raw_input().split()
    numberOfQuestions = int(raw_input())
    questions = []
    for i in range(numberOfQuestions):
        questions.append(raw_input())
    numberOfQueries = int(raw_input())
    queries = []
    for i in range(numberOfQueries):
        queries.append(raw_input())
    
    topics = [x for x in parseTree if x !='(' and x != ')']
    topics = set(topics)
    # Build topic graph by adding nodes
    g = Graph()
    for t in topics:
        n = Node(t)
        g.addNode(n)

    # Add edges between parent and child
    # A directed graph having a relation of parent -> child.
    constructTree(g,parseTree)

    # Add questions to the topics node.
    addPropertyQuestions(g,questions)

    # Count number of queries matching the questions in the given topics and
    # subtopics.
    countQueries(g,queries)
    #g.printGraph()
