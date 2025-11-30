from langgraph.graph import StateGraph, START, END
from agents.state import State
from agents.youtube import get_transcript
from agents.notion import make_page_contents
from agents.translate import translate_transcript


def build_graph():
    graph = StateGraph(State)
    
    # add node
    graph.add_node("transcript", get_transcript)
    graph.add_node("translate", translate_transcript)
    graph.add_node("notion", make_page_contents)
    
    # add edge
    graph.add_edge(START, "transcript")
    graph.add_edge("transcript", "translate")
    graph.add_edge("translate", "notion")
    graph.add_edge("notion", END)

    return graph.compile()