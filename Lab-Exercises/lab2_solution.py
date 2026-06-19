cluster_config = {
    "cluster_name": "dhaka-prod-east",
    "total_max_slots": 8,
    "active_nodes": ["10.0.1.15", "10.0.1.16", "10.0.1.17", "10.0.1.18", "10.0.1.19"],
}


def calculate_capacity(config):
    active_node_count = 0
    for _node in config["active_nodes"]:
        active_node_count += 1

    utilization_percent = (active_node_count / config["total_max_slots"]) * 100

    print(f"Cluster: {config['cluster_name']}")
    print(f"Active Nodes: {active_node_count}")
    print(f"Total Max Slots: {config['total_max_slots']}")
    print(f"Utilization: {utilization_percent:.2f}%")


calculate_capacity(cluster_config)
