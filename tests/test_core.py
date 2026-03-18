"""Tests for DrugDiscoveryAi."""
from src.core import DrugDiscoveryAi
def test_init(): assert DrugDiscoveryAi().get_stats()["ops"] == 0
def test_op(): c = DrugDiscoveryAi(); c.search(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = DrugDiscoveryAi(); [c.search() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = DrugDiscoveryAi(); c.search(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = DrugDiscoveryAi(); r = c.search(); assert r["service"] == "drug-discovery-ai"
