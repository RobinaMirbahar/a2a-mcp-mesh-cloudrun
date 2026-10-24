from a2a_mcp_mesh.mcp_servers.alloydb_vector_mcp import search_alloydb_runbooks_scann
from a2a_mcp_mesh.mcp_servers.spanner_graph_mcp import query_service_blast_radius_gql


def test_search_alloydb_runbooks_scann():
    result = search_alloydb_runbooks_scann(
        error_signature="DEADLINE_EXCEEDED: gRPC channel pool exhausted on spanner-ledger-session",
        service_tier="TIER_1_FINANCIAL",
    )
    assert result["runbook_id"] == "RB-SPANNER-GRPC-POOL-204"
    assert result["service_tier"] == "TIER_1_FINANCIAL"
    assert result["similarity_score"] > 0.90
    assert len(result["required_safety_checks"]) >= 2


def test_query_service_blast_radius_gql():
    result = query_service_blast_radius_gql(
        service_id="spanner-ledger-session",
        max_hops=3,
    )
    assert result["root_service_id"] == "spanner-ledger-session"
    assert result["hop_count"] == 3
    assert result["impacted_enterprise_tenants"] == 42
    assert "checkout-orchestrator-v2" in result["impacted_downstream_services"]
