import streamlit as st
from textToCypherQuery import TextToCypher
from log import Logger
from streamlit_agraph import agraph, Node, Edge, Config
import json

text_to_cypher = TextToCypher()
logger = Logger.getlogger()

def response_generator(user_input):
    global text_to_cypher
    text_to_cypher_output = text_to_cypher.run(user_input)
    logger.info(f"id of text to cypher class is {text_to_cypher}")
    logger.info(f":::::::::::returning the output:::::::{text_to_cypher_output}")
    return text_to_cypher_output

def create_graph_data(output_data):
    nodes = []
    edges = []
    business_dict = {}

    for item in output_data["results"]:
        consumer_id = str(item["consumer_id"])
        consumer_name = item["name"]
        business_name = item["business_name"]

        nodes.append(Node(id=consumer_id, label=consumer_name, size=25))

        if business_name not in business_dict:
            business_dict[business_name] = True
            nodes.append(Node(id=business_name, label=business_name, size=30, color="#FF5733"))

        edges.append(Edge(source=consumer_id, target=business_name, label="HAS_BUSINESS_OF", type="CURVE_SMOOTH"))
    
    return nodes, edges

st.title("Simple chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "graphs" not in st.session_state:
    st.session_state.graphs = []

for idx, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if idx < len(st.session_state.graphs):
            nodes, edges = st.session_state.graphs[idx]
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
                key=f"agraph_{idx}"
            )
            agraph(nodes=nodes, edges=edges, config=config)

if prompt := st.chat_input("Enter your query"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = response_generator(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.write("Raw Response:", response)

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
            #st.write("Nodes:", nodes)
            #st.write("Edges:", edges)
        else:
            st.write("The 'results' key is not a list.")
    else:
        st.write("The 'results' key is missing or response is not a dictionary.")

    # Re-render the current graphs after appending to session state
    for idx, message in enumerate(st.session_state.messages):
        if idx < len(st.session_state.graphs):
            nodes, edges = st.session_state.graphs[idx]
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
                key=f"agraph_{idx}"
            )
            agraph(nodes=nodes, edges=edges, config=config)





























# import streamlit as st
# from textToCypherQuery import TextToCypher
# from log import Logger
# from streamlit_agraph import agraph, Node, Edge, Config
# import json

# text_to_cypher = TextToCypher()
# logger = Logger.getlogger()

# def response_generator(user_input):
#     global text_to_cypher
#     text_to_cypher_output = text_to_cypher.run(user_input)
#     logger.info(f"id of text to cypher class is {text_to_cypher}")
#     logger.info(f":::::::::::returning the output:::::::{text_to_cypher_output}")
#     return text_to_cypher_output

# def create_graph_data(output_data):
#     nodes = []
#     edges = []
#     business_dict = {}

#     for item in output_data["results"]:
#         consumer_id = str(item["consumer_id"])
#         consumer_name = item["name"]
#         business_name = item["business_name"]

#         nodes.append(Node(id=consumer_id, label=consumer_name, size=25))

#         if business_name not in business_dict:
#             business_dict[business_name] = True
#             nodes.append(Node(id=business_name, label=business_name, size=30, color="#FF5733"))

#         edges.append(Edge(source=consumer_id, target=business_name, label="HAS_BUSINESS_OF", type="CURVE_SMOOTH"))
    
#     return nodes, edges

# st.title("Simple chat")

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# if "graphs" not in st.session_state:
#     st.session_state.graphs = []

# for idx, message in enumerate(st.session_state.messages):
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])
#         if idx < len(st.session_state.graphs):
#             nodes, edges = st.session_state.graphs[idx]
#             config = Config(
#                 width=1000,
#                 height=800,
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
#             with st.container():
#                 agraph(nodes=nodes, edges=edges, config=config)

# if prompt := st.chat_input("Enter your query"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     response = response_generator(prompt)
#     with st.chat_message("assistant"):
#         st.markdown(response)
#     st.session_state.messages.append({"role": "assistant", "content": response})
#     st.write("Raw Response:", response)

#     if isinstance(response, str):
#         try:
#             response = json.loads(response)
#         except json.JSONDecodeError as e:
#             st.write("Error decoding JSON:", e)
#             response = {}

#     if isinstance(response, dict) and "results" in response:
#         st.write("Results Key Found:", response["results"])
#         if isinstance(response["results"], list):
#             nodes, edges = create_graph_data(response)
#             st.session_state.graphs.append((nodes, edges))
#             st.write("Nodes:", nodes)
#             st.write("Edges:", edges)
#         else:
#             st.write("The 'results' key is not a list.")
#     else:
#         st.write("The 'results' key is missing or response is not a dictionary.")

#     # Re-render the current graphs after appending to session state
#     for idx, message in enumerate(st.session_state.messages):
#         if idx < len(st.session_state.graphs):
#             nodes, edges = st.session_state.graphs[idx]
#             config = Config(
#                 width=1000,
#                 height=800,
#                 directed=True,
#                 nodeHighlightBehavior=True,
#                 highlightColor="#F7A7A6",
#                 collapsible=True,
#                 node={'labelProperty': 'label', 'color': 'color', 'size': 'size', 'renderLabel': True},
#                 link={'labelProperty': 'label'},
#                 physics=True,
#                 hierarchical=False,
#                 linkLength=400,
#                 gravity=-800,
#                 key=f"agraph_{idx}"
#             )
#             with st.container():
#                 agraph(nodes=nodes, edges=edges, config=config)















































# import streamlit as st
# import random
# import time
# from textToCypherQuery import TextToCypher
# from log import Logger
# import streamlit as st
# from streamlit_agraph import agraph, Node, Edge, Config
# import json

# text_to_cypher = TextToCypher()
# logger = Logger.getlogger()

# def response_generator(user_input):
#     global text_to_cypher
#     # try:
#     text_to_cypher_output = text_to_cypher.run(user_input)
#     logger.info(f"id of text to cypher class is {text_to_cypher}")
#     logger.info(f":::::::::::returning the output:::::::{text_to_cypher_output}")
#     return text_to_cypher_output
        
#     # except Exception as e:
#     #     logger.info(f":::error in process_text_to_cypher::::{e}")
#     #     return str(e)

# def create_graph_data(output_data):
#     nodes = []
#     edges = []
#     business_dict = {}  # Dictionary to track unique businesses

#     for item in output_data["results"]:
#         consumer_id = str(item["consumer_id"])
#         consumer_name = item["name"]
#         business_name = item["business_name"]

#         # Add consumer node
#         nodes.append(Node(id=consumer_id, label=consumer_name, size=25))

#         # Add business node if it doesn't already exist
#         if business_name not in business_dict:
#             business_dict[business_name] = True
#             nodes.append(Node(id=business_name, label=business_name, size=30, color="#FF5733"))

#         # Add edge from consumer to business
#         edges.append(Edge(source=consumer_id, target=business_name, label="HAS_BUSINESS_OF", type="CURVE_SMOOTH"))
    
#     return nodes, edges


        
# st.title("Simple chat")

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []
    
# if "graph_data" not in st.session_state:
#     st.session_state.graph_data = {"nodes": [], "edges": []}


# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # Accept user input
# if prompt := st.chat_input("Enter your query"):
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     # Display user message in chat message container
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     response = response_generator(prompt)
#     # Display assistant response in chat message container
#     with st.chat_message("assistant"):
#         st.markdown(response)
#         #response = st.write(response_generator(prompt))
#     # Add assistant response to chat history
#     st.session_state.messages.append({"role": "assistant", "content": response})
#     st.write("Raw Response:", response)
#     if isinstance(response, str):
#         try:
#             response = json.loads(response)
#         except json.JSONDecodeError as e:
#             st.write("Error decoding JSON:", e)
#             response = {}

    
#     if isinstance(response, dict):
#         if "results" in response:
#             st.write("Results Key Found:", response["results"])
#             if isinstance(response["results"], list):
#                 nodes, edges = create_graph_data(response)
                
#                 # Debug: Print nodes and edges to check their structure
#                 st.write("Nodes:", nodes)
#                 st.write("Edges:", edges)

#                 if nodes and edges: 
#                     config = Config(
#                             width=1000,  # Increase the width
#                             height=800,  # Increase the height
#                             directed=True,
#                             nodeHighlightBehavior=True,
#                             highlightColor="#F7A7A6",
#                             collapsible=True,
#                             node={'labelProperty': 'label', 'color': 'color', 'size': 'size', 'renderLabel': True},  # Use color and size
#                             link={'labelProperty': 'label'},
#                             physics=True,  # Enable physics for better layout
#                             hierarchical=False,
#                             linkLength=1000,  # Increase link length for better spacing
#                             gravity=-400,  # Adjust gravity for better node separation
#                         )                    
#                     agraph(nodes=nodes, edges=edges, config=config)
#                 else:
#                     st.write("No nodes or edges to display.")
#             else:
#                 st.write("The 'results' key is not a list.")
#         else:
#             st.write("The 'results' key is missing.")
#     else:
#         st.write("Response is not a dictionary.")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    # if isinstance(response, dict) and "results" in response:
    #     nodes, edges = create_graph_data(response)
    #     config = Config(
    #             width=1000,  # Increase the width
    #             height=800,  # Increase the height
    #             directed=True,
    #             nodeHighlightBehavior=True,
    #             highlightColor="#F7A7A6",
    #             collapsible=True,
    #             node={'labelProperty': 'label', 'color': 'color', 'size': 'size', 'renderLabel': True},  # Use color and size
    #             link={'labelProperty': 'label'},
    #             physics=True,  # Enable physics for better layout
    #             hierarchical=False,
    #             linkLength=400,  # Increase link length for better spacing
    #             gravity=-400,  # Adjust gravity for better node separation
    #         )
    #     agraph(nodes=nodes, edges=edges, config=config)
    
    # nodes = []
    # edges = []
    # business_id = 8  # Assuming all consumers belong to business_id 8
    # business_node = Node(id=str(business_id), label=f"Business {business_id}", size=40, color="#9370DB")
    # nodes.append(business_node)

    # for consumer in response:
    #     consumer_node = Node(id=str(consumer["c.consumer_id"]), label=consumer["c.name"], size=30, color="#FF4500")
    #     nodes.append(consumer_node)
    #     edge = Edge(source=str(business_id), target=str(consumer["c.consumer_id"]), label="RELATED_TO")
    #     edges.append(edge)

    # # Create the configuration for the graph
    # config = Config(
    #     width=1000,  # Increase the width
    #     height=800,  # Increase the height
    #     directed=True,
    #     nodeHighlightBehavior=True,
    #     highlightColor="#F7A7A6",
    #     collapsible=True,
    #     node={'labelProperty': 'label', 'color': 'color', 'size': 'size', 'renderLabel': True},  # Use color and size
    #     link={'labelProperty': 'label'},
    #     physics=True,  # Enable physics for better layout
    #     hierarchical=False,
    #     linkLength=400,  # Increase link length for better spacing
    #     gravity=-400,  # Adjust gravity for better node separation
    # )

    # # Display the graph in the Streamlit app
    # agraph(nodes=nodes, edges=edges, config=config)































# import streamlit as st
# from streamlit_agraph import agraph, Node, Edge, Config

# # Example data
# result = [
#     {
#         "c.consumer_id": 92,
#         "c.name": "Starr Hamblington",
#         "c.gender": "Genderqueer",
#         "c.email": "shamblington2j@stumbleupon.com",
#         "c.age": 50,
#         "b.business_id": 1
#     },
#     {
#         "c.consumer_id": 5,
#         "c.name": "Erika Iacovides",
#         "c.gender": "Female",
#         "c.email": "eiacovides4@mac.com",
#         "c.age": 40,
#         "b.business_id": 1
#     },
#     {
#         "c.consumer_id": 66,
#         "c.name": "Juana Brader",
#         "c.gender": "Genderqueer",
#         "c.email": "jbrader1t@timesonline.co.uk",
#         "c.age": 29,
#         "b.business_id": 1
#     },
#     {
#         "c.consumer_id": 12,
#         "c.name": "Kathie Dax",
#         "c.gender": "Female",
#         "c.email": "kdaxb@pagesperso-orange.fr",
#         "c.age": 41,
#         "b.business_id": 1
#     }
# ]

# # Create nodes and edges
# nodes = []
# edges = []
# business_id = 8  # Assuming all consumers belong to business_id 8
# business_node = Node(id=str(business_id), label=f"Business {business_id}", size=40, color="#9370DB")
# nodes.append(business_node)

# for consumer in result:
#     consumer_node = Node(id=str(consumer["c.consumer_id"]), label=consumer["c.name"], size=30, color="#FF4500")
#     nodes.append(consumer_node)
#     edge = Edge(source=str(business_id), target=str(consumer["c.consumer_id"]), label="RELATED_TO")
#     edges.append(edge)

# # Create the configuration for the graph
# config = Config(
#     width=1000,  # Increase the width
#     height=800,  # Increase the height
#     directed=True,
#     nodeHighlightBehavior=True,
#     highlightColor="#F7A7A6",
#     collapsible=True,
#     node={'labelProperty': 'label', 'color': 'color', 'size': 'size', 'renderLabel': True},  # Use color and size
#     link={'labelProperty': 'label'},
#     physics=True,  # Enable physics for better layout
#     hierarchical=False,
#     linkLength=400,  # Increase link length for better spacing
#     gravity=-400,  # Adjust gravity for better node separation
# )

# # Display the graph in the Streamlit app
# st.title("Consumers and Business Relationship Graph")
# agraph(nodes=nodes, edges=edges, config=config)































