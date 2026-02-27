variable "resource_group_name" {
  description = "Name of the Azure Resource Group"
  type        = string
  default     = "rg-microservices-platform"
}

variable "location" {
  description = "Azure region to deploy resources"
  type        = string
  default     = "norwayeast"
}

variable "acr_name" {
  description = "Name of Azure Container Registry - must be globally unique"
  type        = string
  default     = "acrmicroservicesplatform"
}

variable "aks_cluster_name" {
  description = "Name of the AKS cluster"
  type        = string
  default     = "aks-microservices-platform"
}

variable "log_analytics_workspace_name" {
  description = "Name of Log Analytics Workspace"
  type        = string
  default     = "law-microservices-platform"
}
