# Container terminology

**container**
- a lightweight mechanism for isolating running processes
- the runtime instantiation of a *container image* (see below)
- **Containerization**: encapsulating or packaging up software code and all its dependencies so that it can run uniformly and consistently on any infrastructure.
  - The goal is portability. Containers solve the problem of: "well, it runs on my machine."
- Versus VMs
  - Containers offer the same isolation, scalability, and disposability of VMs
  - Unlike virtual machines where only hardware is virtualized, containers share the host OS kernel.
  - Because they don’t carry the payload of their own OS instance, they’re lighter weight (that is, they take up less space) than VMs.


**container image**
- binary that includes all of the requirements for running a single container
- a file which is pulled down from a Registry Server and used locally as a mount point when starting Containers.
- Technically, it is much more complicated than a single file on a Registry Server. When people use the term “container image,” they often mean to imply Repository and referring to a bundle of multiple container Image Layers as well as metadata which provides extra information about the layers.


**container repository (Docker repository)**
- A collection of related container images and tags identifying them.
- A registry contains a collection of one or more image repositories. Each image repository contains one or more tagged images.
- A container registry is organized into container repositories, where a repository holds all the versions of a specific image.


**container registry (or container registry server)**
- A content server that can store and service images from Docker repositories.
- A registry server is essentially a fancy file server that is used to store docker repositories.
- Typically, the registry server is specified as a normal DNS name and optionally a port number to connect to. Much of the value in the docker ecosystem comes from the ability to push and pull repositories from registry servers.
- Examples:
  - **Dockerhub**: Docker's public registry; docker interacts with this registry by default
  Other companies host paid online Docker registries for public use:
  - **ECR** Amazon Elastic Container Registry
  - **GCR** Google Container Registry
  - **ACR**: Azure Container Registry
  - **OCR** OpenShift Container Registry (RedHat)
    - a container image registry integrated with the Openshift Container Platform
    - adds the ability to automatically provision new image repositories on demand. This provides users with a built-in location for their application builds to push the resulting images.
  - Red Hat also offers a standalone enterprise Registry Server with Quay Enterprise, as well as cloud based, public and private repositories on **Quay.io**.

**container runtime**
- responsible for all the parts of running a container that isn't actually running the program itself.
- runtimes implement varying levels of features, but technically, if it runs a container, then it's a container runtime.

**container engine**
- a piece of software that accepts user requests, including command line options, pulls images, and from the end user’s perspective runs the container.
- Examples:
  - docker
  - RKT
  - CRI-O
  - LXD
  Also, many cloud providers, Platforms as a Service (PaaS), and Container Platforms have their own built-in container engines which consume Docker or OCI compliant Container Images. Having an industry standard Container Image Format allows interoperability between all of these different platforms.
- most container engines don’t actually run the containers, they rely on an OCI compliant runtime like runc

**Difference between a container engine and a container runtime**
A container engine is a end-user and sysadmin tool to manage containers.  Some engines, such as podman, are also developer tools to build containers. CRI-O does not provide features to build containers because Kubernetes doesn't need them.

A container runtime is a low-level helper tool to setup containers using Linux Kernel primitives such as namespaces and cgroups. You can think about a container runtime as a chroot command on steroids. It just creates a stronger sandbox than a chroot jail and does that using features from a standard Linux Kernel.

take a Container Image and turn it into a Container (aka running processes). How this happens is governed by the scope of the OCI

**docker daemon**
A constant background process that helps to manage/create Docker images, containers, networks, and storage volumes.

**podman**
- daemon-less container engine for developing, managing, and running OCI Containers on your Linux System.
- **Versus Docker**
  - Both use the runC runtime
  - Docker uses a daemon; Podman doesn't. Podman directly interacts with image registry, containers and image storage.
  - Docker containers can only be run as root; with podman, containers can either be run as root or in rootless mode.
  - Podman only runs on Linux
  - There is compatibility between Podman and Docker images.


# Kubernetes Terminology

**Cluster**
 a logically connected group of computers (called nodes)

**Node**
- A server that hosts applications in a Kubernetes cluster.
- May be a VM or physical machine. Each node has the services necessary to run pods and is managed by the master components. The services on a node include Docker, kubelet and kube-proxy.

**Master Node**
- A node server that manages the control plane in a Kubernetes cluster; provide basic cluster services such as APIs or controllers.

- Master components, together called the **Control Plane**, responsible for making global decisions about the cluster and they detect and respond to cluster events.
  - ETCD
  - Kube-apiserver
  - Kube-control-manager
  - Kube-schdeduler


**Worker Node**
execute workloads for the cluster. Application pods are scheduled here


**Pod**
- a group of one or more containers, with shared storage/network resources, and a specification for how to run the containers.
- one or more containers deployed together on one host, and the smallest compute unit that can be defined, deployed, and managed.
- provides a way to set environment variables, mount storage, and feed other info into a container
- Can hold any number of containers, but usually only two. We pretend that one of those doesn't exist.
- A pod is connected via an overlay network to the rest of the environment.
- Pods are the rough equivalent of a machine instance (physical or virtual) to a container. - Each pod is allocated its own internal IP address, therefore owning its entire port space, and containers within pods can share their local storage and networking.
- Pods have a lifecycle; they are defined, then they are assigned to run on a node, then they run until their container(s) exit or they are removed for some other reason. Pods, depending on policy and exit code, may be removed after exiting, or may be retained in order to enable access to the logs of their containers.
- Pods are responsible for running containers. Every Pod holds at least one container, and controls the execution of that container. When the containers exit, the Pod dies too.


**namespace**
- a kubernetes mechanism to scope and group resources in a cluster.
- Each namespace has its own resources, policies, and constraints/quotas
- Allows an individual or group of users to organize and manage their content in isolation from others
- Services, pods, replication controllers, and volumes can easily cooperate within a namespace,  but the namespace provides a degree of isolation from the other parts of the cluster.
- Namespaces provide a unique scope for:
  * Named resources to avoid basic naming collisions.
  * Delegated management authority to trusted users.
  * The ability to limit community resource consumption.
- Default namespaces:
- `default`: namespace for objects with no other namespace
- `kube-system`: reserved for objects created by kubernetes system itself
- `kube-public:` convention to provide resource information to allusers
- `kube-node-lease`: for lease objects associated with each node.


**volumes**
Providers expose both persistent and ephemeral storage:
 - cloud block storage
 - ceph
 - gluster


**Resource**
any kind of component definition managed by Kubernetes.
Contains the configuration of the managed component and the current state of the component


**init container**
- Specialized container that runs before app containers in a pod.
- Can contain utilities or setup scripts not present in an app image.
- Allow you to reorganize setup scripts and binding code.
- Uses:
  - Contain and run utilities that are not desirable to include in the app Container image for security reasons.
  - Contain utilities or custom code for setup that is not present in an app image. For example, there is no requirement to make an image FROM another image just to use a tool like sed, awk, python, or dig during setup.
  - Use Linux namespaces so that they have different filesystem views from app containers, such as access to Secrets that application containers are not able to access.


- Init containers are exactly like regular containers, except:
  * Init containers always run to completion.
    - init containers do not support lifecycle, livenessProbe, readinessProbe, or startupProbe because they must run to completion before the Pod can be ready.
  * Each init container must complete successfully before the next one starts.
    - if you specify multiple init containers for a Pod, Kubelet runs each init container sequentially. Each init container must succeed before the next can run. When all of the init containers have run to completion, Kubelet initializes the application containers for the Pod and runs them as  usual.


**ReplicaSet**
- Ensures that a specified number of replicas of a pod are running at all times.
- Considered a “low-level” type in Kubernetes: users often work with higher-level abstractions like Deployments and DaemonSets. Required only when custom update orchestration is needed.
- Ensures that a set of identically configured Pods are running at the desired replica count. If a Pod drops off, the ReplicaSet brings a new one online as a replacement.


**Replication Controllers**
- Replication controllers provide a method for managing an arbitrary number of pods.
- Contains a pod template, which can be replicated any number of times.
Through the replication controller, Kubernetes will manage your pods’ lifecycle, including scaling up and down, rolling deployments, and monitoring.


**Replicaset vs. Replication Controller**
- Functionally similar, almost identical. Both maintain a number of replicas and have same two features: scale up/down and auto restart
- ReplicaSet is newer, considered a “next-generation replication controller”. Using ReplicaSet (with a Deployment) is more common design pattern, because it is more declarative.
- Main differences: selector types, and updating the pods. 
  - A replication controller only supports equality-based selector requirements (=,==,!=). A replica set supports set-based selector requirements (in, notin and exists). The former allows filtering by label keys and values. The latter gives more flexibility
  -  `rollout` command is used for updating the replica set; `rolling-update` command is used for updating the replication controller.


**DaemonSet**
- can be used to run replicas of a pod on a specific node or all nodes in a cluster
- have many uses — one frequent pattern is to use them to install or configure software on each host node
- Use daemonsets to create shared storage, run a logging pod on every node in your cluster, or deploy a monitoring agent on every node.
- A DaemonSet ensures that all (or some) Nodes run a copy of a Pod. As nodes are added to the cluster, Pods are added to them. As nodes are removed from the cluster, those Pods are garbage collected. Deleting a DaemonSet will clean up the Pods it created.


**Deployment**
- a higher-order abstraction that controls deploying and maintaining a set of Pods. Behind the scenes
- it uses a ReplicaSet to keep the Pods running, but it offers sophisticated logic for deploying, updating, and scaling a set of Pods within a cluster.
- instructs Kubernetes how to create and update instances of your applications
- Kubernetes master schedules the application instances included int hat Deplyment to run on individual Nodes in the cluster.
- If the Node hosting an instance goes down or is deleted, the Deployment controller replaces the instace with an instace  another Node in the cluster.
- Support rolling updates and rollbacks
- Can be paused
- two Kubernetes Deployment Types
  - Blue Green (B/G) - Deploy all at once
  - Canary - Deploy one at a time incrementally


**Operator**
Kubernetes native applications
Administration, shell scripts, and automation software (like Ansible) are now in Kubernetes pods
integrate natively with Kubernetes concepts and APIs
extend the OpenShift API
encode operational knowledge
can be written in Ansible


**Secret**
- used to hold sensitive information such as passwords, tokens, certificates, etc.
- Secrets are Base-64 encoded “at rest”, but the data is automatically decoded when attached to a pod
- Secrets can be attached as files or environment variables
- Use add-on encryption providers for unlocking your data
- Secrets can be attached to Pods at runtime so that sensitive configuration data can be stored securely in the cluster.

**Job**
used to create pods for a specified reason (one time only)


**Service**
- A logical set of pods.
- Provides a single IP address, DNS name, and port number by which pods can be accessed.
- Tells the rest of the Kubernetes environment (including other pods and replication controllers) what services your application provides.
- Persistent: While pods come and go, the service IP addresses and ports remain the same.
- Proide service discovery:
  - If service A wants to communicate with service B without having to know endpoints (the ip addresses for each pod), they can do so a way to communicate
- **Types**:
  - ClusterIP (default)
  - NodePort:
  - LoadBalancer: Exposes the Service externally using a load balancer. NodePort and ClusterIP Services, to which the external load balancer routes, are automatically created.
  - ExternalName: Maps the internal service name to an external fully qualified domain name


**Ingress**
- exposes HTTP and HTTPS traffic from outside the cluster to services within the cluster.
- **Features**:
  - Externally reachable URLs
  - Load balance traffic
  - Terminate SSL/TLS
  - Virtual hosting


**Route**
- allow for network access to pods from users and applications outside the OpenShift instance.
- A route object consists of a host name, a route name, a service selector, and optional security configurations. An OpenShift router consumes routes and is a deployment of one or more pods that forwards network traffic to the proper pods.

**Service versus Route**


**configmap**
used to store the node configuration in the cluster

**build**
is the process of transforming input parameters into a resulting object.

**label**
- A key-value pair that can be assigned to any Kubernetes resource.
- Used by Selectors to filter eligible resources for scheduling and other operations. Two types of label selectors:
  - equality-based: `environment = production`, `tier != frontend`
  - set-based: `environment in (production, qa)`, `tier notin (frontend, backend)`
- Essentially, “nametags” to identify things. Can query based on labels.
- Open-ended: You can use them to indicate roles, stability, or other important attributes.
- Do not provide uniqueness.
- Annotations are just like labels, but can't be used to identify and select objects


**buildconfig**
definition of the entire build process.

**Controller**
a Kubernetes process that watches resources and makes changes attempting to move the current state towards the desired state.

**Security context constraints**
allow administrators to control permissions for pods;
a security mechanism that restricts access to resources, but not to operations in OpenShift.

**Taints and tolerations**
controls which pods should (or should not) be scheduled on a node.

**Imagestream**
provide an abstraction for referencing container images from within OpenShift Container Platform
Image streams can be used to automatically perform an action when new images are created. Builds and deployments can watch an image stream to receive notifications when new images are added, and react by performing a build or deployment.


**CRDs**
CustomResourceDefinitions, or CRDs, provide an extension mechanism that cluster operators and developers can use to create their own resource types.


**ELK stack**
- Useful for viewing logs aggregated from hosts and applications, regardless of whether they come from multiple containers or deleted pods
- `elasticsearch` used for aggregated logging
- `Kibana` web UI for Elasticsearch

**Fluentd**
Gathers logs from nodes and feeds them to Elasticsearch

**OpenShift metrics collection facilities**

A. The OpenShift node exposes metrics that Prometheus collects and stores
B. CPU and memory-based metrics are viewable from the Red Hat OpenShift Container Platform web console and are available for use by Horizontal Pod Autoscalers (HPAs)
C. Prometheus Metrics is a metrics engine that stores data persistently


**Recommended monitoring components** (per the official OpenShift docs)
`Prometheus`: collect and store metrics from the components that we want to watch.
`Grafana`: visualize the data we've collected from our system using dashboards
`Alertmanager`: sends alerts when there is a critical issue.


**Prometheus Operator**
creates, configures, and manages Prometheus and Alertmanager instances. It also automatically generates monitoring target configurations based on familiar Kubernetes label queries.

**CI/CD**
**Jenkins** - The most popular CI/CD Engine
**Tekton** - A full-lifecycle, flexible, extensible, script-based and GUI-based CI/CD workflow - without an engine
Knative Serving: Enables autoscaling and event-driven behavior from over 200+ sources in the programming language of choice


**Operator Lifecycle Manager**
aids cluster administrators in installing, upgrading, and granting access to Operators running on their OpenShift Container Platform cluster.

**internal registry address**
docker-registry.default.svc.cluster.local:5000

Two methods to authenticate to OpenShift
OAuth
TLS Certificates



# Openshift Terminology

**Openshift Project**
a kubernetes namespace with additional annotations
Projects can have a separate name, displayName, and description.

OpenShift 4.x master nodes are only supported to run on Red Hat Enterprise Linux CoreOS. Worker nodes run any environment that Red Hat Enterprise Linux runs on.
OpenShift can run images from any container registry, including these three examples.
A. Red Hat Container Catalog
B. Private container registries
C. OpenShift internal container registry

Deployment Config
A. Have triggers that drive automated deployments in response to events
B. Allow rollbacks to a previous version, either manually or automatically in case of deployment failure
C. Allow manual replication scaling and autoscaling

three deployment strategies
Recreate
Rolling
Custom

commands \ used for troubleshooting in OpenShift
oc status
oc get events
oc describe

command used to update the application version
oc set image

Three features of .kube/config
A. Keep cluster's login URL
B. Keep session token
C. Keep information about current project

port is used by default in the login URL
6443

kube-proxy process runs on every node

Which format is NOT supported by oc -o?
A. JSON
B. YAML
C. JSONPATH
D. XML
Answer: D

Red Hat OpenShift uses Ansible for operating system upgrades
