cluster_config = {
    "cluster_name": "dhaka-prod-east",
    "total_max_slots": 8,
    "active_nodes": ["10.0.1.15", "10.0.1.16", "10.0.1.17", "10.0.1.18", "10.0.1.19"]
}

def calculate_capacity(config):
    active_count = len(config["active_nodes"])
    total_slots = config["total_max_slots"]
    utilization = (active_count / total_slots) * 100
    
    print(f"Cluster: {config['cluster_name']}")
    print(f"Active Nodes: {active_count}/{total_slots}")
    print(f"Utilization: {utilization:.2f}%")

# Execute the audit tool
calculate_capacity(cluster_config)
