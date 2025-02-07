import anytree

# Create the root node
root = anytree.Node("metric_customer_acquisition_and_retention")

# Create the child nodes
clv_node = anytree.Node("metric_clv", parent=root)
customer_retention_node = anytree.Node("metric_customer_retention_rate", parent=root)
campaign_conversion_node = anytree.Node("metric_campaign_conversion", parent=root)

# Create the grandchild nodes
aov_node = anytree.Node("metric_aov", parent=clv_node)
repeat_purchase_node = anytree.Node("repeat_purchase_rate", parent=clv_node)
recent_purchase_recency_node = anytree.Node("metric_recent_purchase_recency", parent=clv_node)

churn_rate_node = anytree.Node("metric_churn_rate", parent=customer_retention_node)
engagement_score_node = anytree.Node("metric_engagement_score", parent=customer_retention_node)

product_affinity_node = anytree.Node("metric_product_affinity", parent=engagement_score_node)
engagement_channel_effectiveness_node = anytree.Node("metric_engagement_channel_effectiveness", parent=engagement_score_node)

arpu_node = anytree.Node("metric_arpu", parent=campaign_conversion_node)

# Visualize the tree
for pre, fill, node in anytree.RenderTree(root):
    print("%s%s" % (pre, node.name))