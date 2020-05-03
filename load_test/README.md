# Load Testing 

Load testing was performed using the [Locust](https://locust.io/) open source load testing tool.  The load test was performed by using Locust to swarm the REST API. Every successful POST to the REST API would also use the deployed model endpoint to generate a prediction. Therefore, swarming the REST API would directly increase the invokation load on the endpoint. Once the number of invokations on an instance reached a pre-defined level, the endpoint would automatically generate a second instance for that endpoint, to handle the increased load. This test was to ensure that this scale-up would automatically occur.

In order to reach the Requests per Second (RPS) needed for this project one standard machine would not be sufficient. The Locust tool has distributed load testing capabilites, so the load test for this prohect was run using two Amazon Cloud 9 instances. One instance acted as the Master node, the other instance the Slave node. The Slave node instance used a **m4.2xlarge** instance,  which has 8 CPUs. All 8 CPUS werere used as a Slave nodes, yielding 8 load testing actors. 

The load test proceeded as a step function. The maximum number of users modeled was 1,200. To reach a max level of 1,200 users, every 10 minutes the test would increase 400 users. Each user was swarming the REST API every 0.1 to 0.5 seconds.

![Number of Users]("../presentation/slide_imgs/load_test_locust_number_of_users.png")
