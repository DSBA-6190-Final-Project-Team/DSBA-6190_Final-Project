# Load Testting 

The Locust tool has distributed load testing capabilites, so the load test for this prohect was run using two Amazon Cloud 9 instances. One instance acted as the Master node, the other instance the Slave node. The Slave node instance used a **m4.2xlarge** instance,  which has 8 CPUs. All 8 CPUS werere used as a Slave  nodes, yielding 8 load testing actors. 
