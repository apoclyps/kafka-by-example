Configuring the Kafka Manager
=============================

To setup Kafka Manager, navigate to `http://localhost:9000` and complete the following steps:

-	Select `Cluster` and `Add Cluster`
-	Enter a cluster name e.g. `events_cluster`
-	Enter a cluster ZooKeeper Host e.g. `zookeeper:2181`
-	Select a Kafka version matching the kafka image e.g. 0.10.1 or the highest available.
-	Save changes

### advanced

To enable metrics and consumers you will need to provide the following configuration:

-	Enable `Enable JMX Polling (Set JMX_PORT env variable before starting kafka server)`
-	Enable `Poll consumer information (Not recommended for large # of consumers)`
-	Enable `Enable Active OffsetCache (Not recommended for large # of consumers)`
-	Enable `Display Broker and Topic Size (only works after applying this patch)`

This will present a confirmation showing that the cluster has been recreated.

You can then create additional topics by navigating to `Topics` and adding new topics with your desired name, replication factor, and number of partitions.
