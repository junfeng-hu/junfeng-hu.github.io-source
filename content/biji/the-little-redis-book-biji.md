Title: The Little Redis Book 笔记
Date: 2015-04-15 12:25:16
Author: junfeng
Category: 笔记
Tags: Redis, learning

query limitations, data structures and Redis' way to store data in memory

###strings
use cases: storing objects (complex or not) and counters

###hashes
hash suits for structed objects
hash implemention

###sets
in op is O(1)?

use cases: Sets are great for tagging or tracking any other properties
of a value for which duplicates don't make any sense
(or where we want to apply set operations such as intersections and unions).

###sorted sets
hashes are like strings but with fields,
then sorted sets are like sets but with a score

use cases:

- leaderboard system
- anything you want sorted by an some integer,
  and be able to efficiently manipulate based on that score,

###Pseudo Multi Key Queries
using hashes to make querying a little easier

###References and Indexes
manage/update/delete these references manually is defficult

###Round Trips and Pipelining

###Transactions
Every Redis command is atomic, including the ones that do multiple things.
Additionally, Redis has support for transactions when using multiple commands.

Redis is actually single-threaded,
which is how every command is guaranteed to be atomic

starts *multi* then some *commands* ends with exec or discard


###Expiration
commands:
- EXPIRE
- EXPIREAT
- TTL
- PERSIST
- SETEX

ideal caching engine

###Lua Scripting
keys with a TTL won't expire half-way through script execution

*lua-time-limit* defines how long a Lua script is allowed to
execute before being terminated. Default is 5 seconds.

###Replication
Redis replication doesn't yet provide automated failover,
If the master dies, a slave needs to be manually promoted

Some commands are more expensive than others (sort for example)
and offloading their execution to a slave can keep the overall
system responsive to incoming queries

###Backups
disable both snapshotting and the append-only file (aof) on
the master and let a slave take care of this

###Redis Cluster
Not only will this offer horizontal scaling, including rebalancing,
but it'll also provide automated failover for high availability.

###End
*Redis is easy to learn*

*the real benefits Redis has to offer with its simplicity*





