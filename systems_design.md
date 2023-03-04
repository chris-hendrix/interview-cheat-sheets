# Systems Design
Resources:
- [System design primer](https://github.com/donnemartin/system-design-primer)
- [Harvard lecture](https://www.youtube.com/watch?v=-W9F__D3oY4)
- [Scalability for dummies](https://web.archive.org/web/20220530193926/https://www.lecloud.net/tagged/scalability)

## [High level trade-offs](https://github.com/donnemartin/system-design-primer#performance-vs-scalability)

Performance vs scalability
- Performance: fast for a single user
- Scalability: fast for a heavy load of users

Latency vs throughput
- Latency: time between request and response
- Throughput: requests per second
- Aim for maximum throughput with acceptable latency

Availability vs consistency (CAP theorem, see below)

## [CAP Theorem](https://github.com/donnemartin/system-design-primer#availability-vs-consistency)
### Availability vs consistency
- Request data from one of two servers, choose two of three (C/P or A/P)
  1. **(C)onsitency**: up-to-date data or error
  2. **(A)vailability**: maybe not up-to-date data, no error
  3. **(P)artition tolerance**: continues to function when one server goes down
- Options
  - CP: for atomic reads/writes (operation 2 cannot start until operation 1 finishes)
  - AP: ok for eventual consistency or system needs to continue functioning

### Consistency patterns
- Weak: after a write, reads will eventually catch up (ie cache)
- Eventual: after a write, reads will catchup in milliseconds (ie DNS updating host IP takes a little time)
- Strong: after a write, reads synchronously see it (ie transactions)

### Availability patterns (HA)
- Failover
  - Master-slave: downtime when promoting slave to master
  - Master-master: load split between masters, one takes over if the other fails
  - Disadvantages: more hardware and complexity, writes lost during switching
- Replication (see database section)
  - Master-slave replication
  - Master-master replication
- Calculation
  - Measured in # of 9s (99.9% and 99.99%)
  - Series: `A = A(1) * A(2)`
  - Parallel: `A = (1 - A(1)) * (1 - A(2))`

## [DNS (domain name system)](https://github.com/donnemartin/system-design-primer#domain-name-system)
- Maps domain name to IPv4 address (user goes to google.com -> DNS returns IPv4 > page loads)
- ISP (for example) has cache, on miss, go to root DNS server
- Managed DNS services (CloudFlare) can route traffic via round robin, latency times, and geo-location
- Disadvantages: slight delay, DNS servers are complex and managed by large entities, DDoS attacks

## [CDN (content delivery network)](https://github.com/donnemartin/system-design-primer#content-delivery-network)
- Proxy servers that store static content (HTML photos)
- Benefits: content from nearby servers, reduces load on your servers
- Disadvantages: costly, stale data (TTL too long), change URL to point to static content
- Push CDN: 1) updates with server changes, 2) good for small traffic with slow changing content
- Pull CDN: 1) updates when first user requests content, then cached (expires after set time, TTL), 2) can be redundant (expiration but not updated), 3) good for high traffic 


## [Load balancer, reverse-proxy](https://github.com/donnemartin/system-design-primer#load-balancer)
- Distribute incoming traffic to appropriate servers AND/OR databases
- Benefits
  - Stops traffic from unhealthy/overloaded resources
  - Eliminates single point of failure
  - Can decrypt/encrypt at interface rather than downstream
  - Can keep track of sessions (cookies) if server doesn't
- Methods: random, least loaded, session/cookies, round robin, weighted RR
- Allows horizontal scaling: great, but adds complexity (more servers, more updating)
- Disadvantages: can become a bottleneck, increases complexity, can be single point of failure
- **Layer 4**: middleman that looks at ports, keeps mapping table (client/server) to determine ports, does not read packet data
  - Pros: Simpler, efficient, NAT (switches client/server to correct port)
  - Cons: not smart, no microservices, no cache (need to know content)
- **Layer 7**: middleman that looks at data, directs to server based on the data
  - Pros: smart, caching, microservices
  - Cons: expensive (looks at data), terminates TLS (decrypts), two TCP connections
- **Reverse proxy**: basically a Layer 7 load balancer but also useful for just one server, NGINX
- Resources:
  - [Layer 4 vs Layer 7](https://youtu.be/aKMLgFVxZYk)

## [Web application architecture (microservices)](https://github.com/donnemartin/system-design-primer#application-layer)
- Web request process
  1. **Client** visits amazon.com
  2. **Presentation layer** serves the frontend files (HTML)
  3. **Business layer** handles API requests, serves data
- Separate web layer from platform (business logic) layer
  - Pros: independently scalable, reduces redundant code, can separate heavy calcs from serving the frontend
  - Cons: more complex, not available in a monolith
- **Microservices**: bunch of independent platform layer servers doing different things
- **Service discovery**: help services find each other by keeping track of registered names, addresses, and ports by using in memory key-value store (ie Zookeeper)
- Resources
  - [Web Application Architecture: How the Web Works](https://www.altexsoft.com/blog/engineering/web-application-architecture-how-the-web-works/)
  - [NextJs Application Architecture for best performance](https://medium.com/@sushinpv/nextjs-application-architecture-for-best-performance-8f1d22e33ba1)
  - [Introduction to Apache ZooKeeper](https://www.allprogrammingtutorials.com/tutorials/introduction-to-apache-zookeeper.php)

## [Database](https://github.com/donnemartin/system-design-primer#database)
### SQL
**ACID** is a set of properties of relational database transactions (CRUD)
- **Atomicity**: transaction succeeds or fails completely
- **Consistency**: transaction keeps db state valid (ie cascade deleting)
- **Isolation**: concurrent transactions have same results as if they occurred sequentially
- **Durability**: save/recoverable after each transaction

Scaling techniques
- Replication
  - **Master-slave replication**: read/write to master, read from slaves
  - **Master-master replication**: read/write to both masters, update/replicate between them
  - *Pros*: provides failover, multiple master provides HA
  - *Cons*
    - loss of writes if master fails before replication
    - writes are replayed to replicas, which could slow reads
    - more slaves = more replication = more lag
    - more complexity
    - *Master-slave*: takes time to promote slave
    - *Master-master*: violates ACID (loosely consistent while updating), need load balancer, conflict resolution increases as write nodes increase (increases latency)
- Federation
  - Splits dbs by function (ie forums, users, and products)
  - *Pros*: less read/write traffic to each, less replication lag, writes can happen in parallel (increasing throughput), more manageable cache for each (more cache hits)
  - *Cons*: not effective for all schemas (ie one table way larger than other), additional code for logic, joins need a server link, more hardware and complexity
- Sharding
  - Splits dbs by subsets of the same table (horizontal, ie moving rows to different dbs)
  - Can split users by name (A-F, G-Y), geolocation, or consistent hashing (random)
  - *Pros*: similar to federation
  - *Cons*: bunch of power users could be on a single shard, joins and redistribution are complex
- Denormalization
  - *Pros*: improves read performance by eliminating expensive joins with redundant data
  - *Cons*: duplicate data that needs to be synced, might perform worse than normalized if write-heavy
  - [Materialized views](https://en.wikipedia.org/wiki/Materialized_view) can keep data up to date
- SQL tuning
  - Uncover and fix bottleneck queries
  - **Benchmark** by simulating high load, **profile** by using slow query log
  - Strategies
    - Tighten schema: use `VARCHAR` instead of `CHAR`, store locations of blobs, etc
    - Use good indices: allows for faster joins (B-tree), could slow writes (index generation)
    - Avoid expensive joins: denormalize where necessary
    - Partition tables: put table hot spots in a different table to keep it in memory
    - Tune the query cache: query is the key, result is the value, could cause performance issues, good for data that doesn't change often

### NoSQL
- Data is denormalized, joins done in the codebase
- Favors **BASE** over ACID
  - **Basically available**: availability guaranteed
  - **Soft state**: state could change without transactions because of
  - **Eventual consistency**: without input, the system will become consistent
- Types
  - **Key-value store**: hash table, used for in-memory cache (Redis) 
  - **Document store**: key-value store with documents (ie JSON) stored as values, allows for "column" flexibility, some providers (MongoDB) provide a query language
  - **Wide column store**: nested mapping using column families, offers HA and scalability, `value=data[row][super_col][sub_col]`
  - **Graph database**: graph used to optimize many-to-many relationships, nodes contain the data, main use is social networks (ie aggregate number of friends)
- SQL vs NoSQL

  | Reasons for SQL | Reasons for NoSQL |
  | --- | --- |
  | Data is structured/relational, schema is strict, requires complex joins | Data is not structured/relational, schema is strict, requires complex joins |
  | Data can be scaled using SQL scaling patterns | Data needs versatile options for scaling |
  | Don't need to handle PBs of data | Need to handle PBs of data |
  | Want established documentation and design patterns | Do not want as established documentation and design patterns | 
  | Data workload is not super-heavy | Data workload is heavy |
  | Don't need to handle heavy read/writes with a large dataset | Need to handle heavy read/writes with a large dataset |
- Applications for NoSQL
  - Rapid ingest of log data
  - Leaderboard data (Redis sorted set)
  - Temporary data (shopping card)
  - Frequently accessed tables
  - Metadata/lookup tables

## [Cache](https://github.com/donnemartin/system-design-primer#cache)
### Strategies
- Goal: balance reads/writes across all partitions
- Strategies: client (browser), CDN, web server (ie page content via reverse-proxy like NGINX), database (some cache natively in default config), application (see below)
- Application caching: key-value store (Redis) in RAM (faster than disk) between app and db, uses algorithms (LRU) to invalidate cold data and keep hot data in ram
- **Caching db queries**: query is the key, cons: hard to handle complex queries, data change might invalidate a bunch of cached queries
- **Caching app objects**: assemble objects from db, remove object from cache if data has changed, async processing, examples: user sessions, rendered pages
- **Cons**: maintain consistency between cache and db, updating the cache is a complex problem

### Updating
- **Read through, cache-aside (lazy loading)**: check cache, miss, read data, then store in cache
  - Pros: fast reads, only requested data which limits cache storage
  - Cons: miss results in 3 trips (delays), data can become stale unless using TTL, node failure clears out everything
- **Write-through**: app uses cache as the main db, app writes to cache, cache then writes to db
  - Pros: fast reads (but slow updates after write), data is not stale
  - Cons: node failure clears everything, most data written may never be read (mitigated with TTL)
- **Write-behind/back**: write to cache, write hits queue, write asynchronously to db
  - Pros: improves write performance
  - Cons: data loss if failure while things are in queue, more complex than others
- **Refresh ahead**: db updates cache before expiration based on prediction
  - Pros: can reduce latency vs read-through
  - Cons: bad predictions make it worse than no cache


## Asynchronism
- **Message queue**: user tweets -> hits queue (but maybe appears on own user's view) -> message is processed and other users can view the tweet
- **Task queue**: queue is built and then tasks are fired (ie sending a bunch of emails)
- **Back pressure**: resistance to the flow of data, if server receives 100rps from client, but can only process 75rps, need to limit the client
- **Cons**: queues for small calcs add delays and complexity

## [Communication](https://github.com/donnemartin/system-design-primer#communication)
- **HTTP (hypertext transfer protocol)**: protocol for communication between client and server
- **TCP (transmission control protocol)**: connection between sender/receiver over an IP network, terminated via two way handshake
  - Reliability over speed (guaranteed to reach destination in order)
  - Examples: chat (Whatsapp), FTP, SMTP (emails)
- **UDP (user datagram protocol)**: connectionless, datagrams (like packets) might reach destination
  - Speed over reliability
  - Examples: online games, DNS, streaming, live broadcasts (Zoom)
- **RPC (remote procedure call)**: client's code calls function that runs on another server
  - more control how client accesses data, altho clients become tightly coupled to server
  - REST is probably the better option
- **REST (representational state transfer)**: focused on exposing data and minimizes the coupling between client/server
  - Cons: client may need multiple round trips to render, payload may increase over time

## [Security](https://github.com/donnemartin/system-design-primer#security)
- Encrypt in transit and at rest
- Sanitize user input to prevent XSS (injecting scripts into sent input) and SQL injection (sanitized by using query parameters)
- Give users the least privilege
