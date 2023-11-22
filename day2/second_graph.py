import streamlit as st
import graphviz

st.title("사용자 정의 그래프 만들기!")
# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge('run', 'intr')
graph.edge('intr', 'runbl')
graph.edge('runbl', 'run')
graph.edge('run', 'kernel')

st.graphviz_chart(graph)

graph = graphviz.Digraph()
edge_set = st.text_input("예시와 같이 from>to와 같이 입력하고, edge는 컴마를 기준으로 구분해주세요.", value = "a>b,b>c,c>a")
st.caption("띄어쓰기는 모두 무시됩니다. ")
edge_set = edge_set.replace(" ", "")
edges = edge_set.split(",")
for edge in edges:
    fr = edge.split(">")[0]
    to = edge.split(">")[1]
    # st.write(fr, to)
    graph.edge(fr, to)

# Streamlit에 그래프 표시
st.graphviz_chart(graph)

