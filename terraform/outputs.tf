output "acr_login_server" {
    description = "ACR login server URL"
    value = azurerm_container_registry.main.login_server
}

output "aks_cluster_name" {
    description = "AKS cluster name"
    value = azurerm_kubernetes_cluster.main.name
}

output "resource_group_name" {
    description = " Resource group name"
    value = azurerm_resource_group.main.name
}

output "key_vault_name" {
    value = azurerm_key_vault_main.name
}
