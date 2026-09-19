from typing import TypedDict
from langgraph.graph import END, StateGraph


# white Board
class State(TypedDict):
    number: int
    
# nodes
def double(state: State) -> dict:
    boardnumber = state['number']
    newnumber = boardnumber * 2
    print(f"double: {boardnumber} * 2 = {newnumber}")
    return {'number': newnumber}    

def finish(state: State) -> dict:
    boardnumber = state['number']
    print(f"finish: {boardnumber}")
    return {'number': boardnumber }

# decision function/ helper function
def decision(state: State) -> str:
    if state['number'] < 100:
        return 'double'
    else:
        return 'finish'
    
    
# create graph 

builder = StateGraph(State)     # initilized the graph
builder.add_node('double', double)  # add node
builder.add_node('finish', finish)  # add node

# entry point
builder.set_entry_point('double')
builder.add_conditional_edges(
    'double',
    decision,
    {'double': 'double', 'finish': 'finish'}
)

builder.add_edge('finish', END)  # add edge to end

graph = builder.compile()  # compile the graph


if __name__ == '__main__':
    result = graph.invoke({'number': 5})