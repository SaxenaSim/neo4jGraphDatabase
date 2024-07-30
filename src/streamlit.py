import streamlit as st
from textToCypherQuery import TextToCypher
from log import Logger
from streamlit_agraph import agraph, Node, Edge, Config
import json

# Initialize custom classes
text_to_cypher = TextToCypher()
logger = Logger.getlogger()

# Function to generate response
def response_generator(user_input):
    global text_to_cypher
    text_to_cypher_output = text_to_cypher.run(user_input)
    logger.info(f"id of text to cypher class is {text_to_cypher}")
    logger.info(f":::::::::::returning the output:::::::{text_to_cypher_output}")
    return text_to_cypher_output

# Function to create graph data
def create_graph_data(output_data):
    nodes = []
    edges = []
    business_dict = {}

    for item in output_data["results"]:
        consumer_id = str(item["consumer_id"])
        consumer_name = item["name"]
        business_name = item.get("business_name")

        nodes.append(Node(id=consumer_id, label=consumer_name, size=25))

        if business_name:
            if business_name not in business_dict:
                business_dict[business_name] = True
                nodes.append(Node(id=business_name, label=business_name, size=30, color="#FF5733"))

            edges.append(Edge(source=consumer_id, target=business_name, label="HAS_BUSINESS_OF", type="CURVE_SMOOTH"))
    
    return nodes, edges

st.set_page_config(
    page_title="Natural Language to Graph Visualization",
    page_icon="🌐",
    layout="wide"
)

# Streamlit app layout
st.title("Natural Language to Graph Visualization")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "graphs" not in st.session_state:
    st.session_state.graphs = []

# Display previous messages and graphs
for idx, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
#         if idx < len(st.session_state.graphs):
#             nodes, edges = st.session_state.graphs[idx]
#             config = Config(
#                 width=1000,
#                 height=200,
#                 directed=True,
#                 nodeHighlightBehavior=True,
#                 highlightColor="#F7A7A6",
#                 collapsible=True,
#                 node={'labelProperty': 'label', 'color': 'color', 'size': 'size', 'renderLabel': True},
#                 link={'labelProperty': 'label'},
#                 physics=True,
#                 hierarchical=False,
#                 linkLength=400,
#                 gravity=-400,
#             )
#             agraph(nodes=nodes, edges=edges, config=config)

# Clear session state for new query
if st.session_state.get("new_query"):
    # st.session_state.messages = []
    st.session_state.graphs = []
    st.session_state.new_query = False

# Handle new user input
if prompt := st.chat_input("Enter your query"):
    st.session_state.new_query = True
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = response_generator(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
    # st.write("Raw Response:", response)

    if isinstance(response, str):
        try:
            response = json.loads(response)
        except json.JSONDecodeError as e:
            st.write("Error decoding JSON:", e)
            response = {}

    if isinstance(response, dict) and "results" in response:
        st.write("Results Key Found:", response["results"])
        if isinstance(response["results"], list):
            nodes, edges = create_graph_data(response)
            st.session_state.graphs.append((nodes, edges))
            # Display only the new graph
            config = Config(
                width=1000,
                height=800,
                directed=True,
                nodeHighlightBehavior=True,
                highlightColor="#F7A7A6",
                collapsible=True,
                node={'labelProperty': 'label', 'color': 'color', 'size': 'size', 'renderLabel': True},
                link={'labelProperty': 'label'},
                physics=True,
                hierarchical=False,
                linkLength=400,
                gravity=-400,
                key=f"agraph_new_{len(st.session_state.graphs) - 1}"
            )
            agraph(nodes=nodes, edges=edges, config=config)
        else:
            st.write("The 'results' key is not a list.")
    else:
        st.write("The 'results' key is missing or response is not a dictionary.")



























