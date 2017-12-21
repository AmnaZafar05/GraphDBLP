All the function for our project are contained in the file Modules.py.

## Load Data and create a graph

For the creation of a graph we had load the json file and we had create two dictionary through some function and dictionary. </br>
* **pubblicationDictionary(json)**: This function return a dictionary with the name of the Author and his ID. We have used this information 
to construct the nodes of the Graph, where the ID of the Author is the ID of the Node and the name of the Author is an attribute of the node. </br>
* **Jaccard(a,b)**: This function return the jaccard similarity of two list </br>

Then we had create another two dictionary: </br>
* **dew= {}**: Is a dictionary that use the pubblicationDictionary(json) result to obtain a list of pubblication for each author. The element from this dictionary 
are the input of Jaccard similary function. </br>
* **dict_publ={}**: Is a dictionary that we have used to create edge. In particular, in this dictionary the keys are the pubblication for each 
pubblication the values are the Author *(tuples: (AuthorName,AuthorID))* that had collaborate on that respective publication.

Finally, we have used all this dictionaries in function of networkx library to create nodes and weighted edge.

## Statistics and subgraph

All the plot and function for this part are explained in REPORT.pdf. </br>
The second task that we had to complete was, given an author in input, create the subgraph induced by the nodes that have hop distance 
at most equal to value *d*. </br>
To do it, we used two function: </br>
* **hop_distance(G,start,end)**: This function returns the length of networkx shortest path function from start node to end node passed by input.
* **author_dist(author, d)**: This function given in input an author name and hop distance *d*, and return the subgraph with hop distance 
equal to d from author node. Thus we have plotted the subgraph.

## Generalized version of Erdos Number

In this part we had write our version of Dijkstra's algorithm
