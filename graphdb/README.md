
  * After a casual chat with John and Donald, I prepared this brief introduction for team's reference.

# 1. Introduction

## 📖 Graph DB

* https://aws.amazon.com/nosql/graph/
* https://neo4j.com/docs/getting-started/appendix/graphdb-concepts/

* A graph database (Graph DB) is primarily used to store and analyze data with complex relationships between entities, making it ideal for scenarios like social network analysis, fraud detection, recommendation engines, knowledge graphs, and network mapping where understanding connections between data points is crucial; essentially, whenever you need to quickly traverse through multiple levels of relationships within your data.


* Key points about graph databases:
  * Data representation:
   * * Data is structured as nodes (entities) and edges (relationships) which allows for easy visualization of connections. 
  * Flexible schema:
   * * Unlike relational databases, graph databases can easily adapt to changing data relationships without needing major schema modifications. 
  * Efficient traversal:
   * * Graph queries can efficiently navigate through complex relationships, allowing you to quickly find connections between seemingly distant data points. 


* Recognizing the Power of Graph Databases and Knowledge Graphs
  * https://www.dbta.com/Editorial/Trends-and-Applications/Recognizing-the-Power-of-Graph-Databases-and-Knowledge-Graphs-166816.aspx
  
  * https://www.databridgemarketresearch.com/reports/global-graph-database-market?srsltid=AfmBOoobGWsrzBeiOVtEoBvLHa3F4YNKhujobDKSH7tZsVnFiy08pFvR
  
  * https://db-engines.com/en/ranking
    * Neo4j
    * Memgraph



# 2. Use Cases

## 🐍 Key Use Cases in Retail Industry
1. [ ] Recommendations, such as product-, coupon-, and content- recommendations
2. [ ] Real-time pricing engines
3. [ ] Customer 360 for personalized experiences, loyalty programs, and call centers
5. [ ] Logistics for ecommerce order delivery
7. [ ] Supply chain visibility and traceability
8. [ ] Network and IT infrastructure monitoring to ensure system uptime and uncover attack paths


## 📖 Walmart

* **Real-Time Recommendations**
* Walmart became the world’s largest retailer by understanding its customers’ needs better than any competitor. An important tool in achieving that understanding is the Neo4j graph database.
* Walmart’s Brazilian ecommerce group wanted to understand the behavior and preferences of its online buyers with enough speed and in enough depth to make real- time, personalized “you may also like” recommendations. However, Walmart quickly recognized that it would be difficult to deliver such functionality using traditional relational database technology.
* “A relational database wasn’t satisfying our requirements about performance and simplicity, due to the complexity of our queries,” said Marcos Wada, software developer at Walmart.
* To address this, Marcos’s team decided to use Neo4j, the leading graph database. Matching a customer’s historical and session data is trivial for graph databases, enabling them to easily outperform relational and other NoSQL data products.
* Walmart deployed Neo4j in its remarketing application run by the company’s ecommerce IT team based in Brazil, and it has been using Neo4j in production since early 2013. Neo4j enables Walmart to understand online shoppers’ behavior, as well as the relationship between customers and products. As a result, the retailer has also been able to up- and cross-sell major product lines in core markets.
* “With Neo4j we could substitute a complex batch process that we used to prepare our relational database with a simple and **real-time graph database**. We could build a simple and real-time recommendation system with low latency queries,” Marcos said.

## 📖 eBay

* Even before its acquisition by global ecommerce leader eBay, London-based Shutl sought to give people the fastest possible delivery of their online purchases. Customers loved the one-day service, and it grew quickly. However, the platform Shutl built to support same-day delivery couldn’t keep up with the exponential growth.
* The service platform needed a revamp in order to support the explosive growth in data and new features. The MySQL queries being used created a code base that was too slow and too complex to maintain. The queries used to select the best courier were simply taking too long, and Shutl needed a solution to maintain a competitive service. The development team believed a graph database could be added to the existing Service-Oriented Architecture (SOA) to solve the performance and scalability challenges.
* eBay selected Neo4j for its flexibility, speed and ease of use. Its property graph model harmonized with the domain being modeled, and the schema-flexible nature of the database allowed easy extensibility, speeding up development. In addition, it overcame the speed and scalability limitations of the previous solution.
* “Our Neo4j solution is literally **thousands of times faster than the prior MySQL solution**, with queries that **require 10-100 times less code**. At the same time, Neo4j allowed us to add functionality that was previously not possible,” said Volker Pacher, Senior Developer for eBay.
* The Cypher graph query language allowed queries to be expressed in a very compact and intuitive form, speeding development. The team was also able to take advantage of existing code, using a Ruby library for Neo4j that also supports Cypher.
* Implementation was completed on schedule in just a year. Queries are now easy and fast. The result is a scalable platform that supports expansion of the business, including the growth it is now experiencing as the platform behind eBay Now.

## 📖 WestJet
Website Ref: https://neo4j.com/customer-stories/westjet/

Discover how one of Canada’s largest airlines transformed flight scheduling into a seamless, customer-friendly experience.
*     5 million: relationships connecting 500,000 nodes in flight schedule graph
*     530%: faster for IT team to update online flight schedule with Neo4j Enterprise
*     30 million:  WestJet passengers served annually by 2028



# 3. Memgraph Databases with GQLAlchemy and Cypher (query language)

In the playground, I prepared several notebooks to focus on different topics:
1. [Memgraph-Cypher](notebook/Memgraph-Cypher.ipynb) to work on Memgraph Lab and introduce Cypher query language for Graph database. 
2. [Memgraph-GqlAlchemy](notebook/Memgraph-GqlAlchemy.ipynb) to use GqlAlchemy with Python to work on Memgraph DB.
3. [Memgraph-ORE Data](notebook/Memgraph-ORE Data.ipynb) to use subset of ORE data with Memgraph DB.
4. [Memgraph-Langchain](notebook/Memgraph-Langchain.ipynb) to show integration among Memgraph db and langchain/langchain-openai.
5. [Memgraph-GqlAlchemy](notebook/Memgraph-GqlAlchemy.ipynb) to play deeper understandings about GqlAlchemy and Cypher.


## 📖 Description

1. Create a graph model from a dataset.
2. Run Memgraph with Docker.
3. Connect to it from a Jupyter Notebook with the help of GQLAlchemy.
4. Perform simple queries.
5. Explore the movies dataset consisting of two CSV files.


## 🐍 Requirements
- [Jupyter](https://jupyter.org/install)
- [Docker](https://docs.docker.com/get-docker/)
- [CMake](https://cmake.org/install/)
- [Memgraph Platform](https://memgraph.com/docs/memgraph/installation)
- [GQLAlchemy](https://pypi.org/project/gqlalchemy/)
- [Pandas](https://pypi.org/project/pandas/)


All info about the versions can be found in the [requirements.txt](requirements.txt) file.


## 🏃 Play around Memgraph
1. setting up environment.
      ```bash
      brew install --cask cmake
      ```
   check cmaker version : cmake --version

      ```bash
      pip install gqlalchemy==1.1.5
      ```
   
2. Start Jupyter Notebook and navigate to the workshop folder.
      ```bash
      jupyter notebook
      ```
3. Start Memgraph platform in docker

   ```bash
   docker run -it -p 7687:7687 -p 7444:7444 -p 3000:3000 memgraph/memgraph-platform:2.4.0
   ```
   Or quickly run Memgraph Platform (Memgraph database + MAGE library + Memgraph Lab) on Linux/MacOS:
   ```bash
   curl https://install.memgraph.com | sh
   ```

4. Copy the data files to docker from data folder
```bash
cd data/
docker cp movies.csv <CONTAINER_ID>:movies.csv
docker cp ratings.csv <CONTAINER_ID>:ratings.csv
docker cp sites.csv <CONTAINER_ID>:sites.csv
docker cp articles.csv <CONTAINER_ID>:articles.csv
docker cp sales.csv <CONTAINER_ID>:sales.csv


docker cp sales.csv <CONTAINER_ID>:sales.csv
docker cp employee.csv <CONTAINER_ID>:employee.csv
docker cp product.csv <CONTAINER_ID>:product.csv
docker cp site.csv <CONTAINER_ID>:site.csv
docker cp inventory.csv <CONTAINER_ID>:inventory.csv
```

5. Check out Memgraph Lab at localhost:3000.


6. play with the notebooks.
* [1-Memgraph-Cypher](notebook/1-Memgraph-Cypher.ipynb)
* [2-Memgraph-GqlAlchemy](notebook/2-Memgraph-GqlAlchemy.ipynb)
* [3-Memgraph-OREData](notebook/3-Memgraph-OREData.ipynb)
* [4-Memgraph-Langchain](notebook/4-Memgraph-Langchain.ipynb)
* [5-Memgraph-GqlAlchemy](notebook/5-Memgraph-GqlAlchemy.ipynb)


8. Check out Memgraph Lab at localhost:3000.
