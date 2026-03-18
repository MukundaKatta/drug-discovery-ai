"""Tests for DrugDiscovery."""
import pytest
from src.drugdiscovery import DrugDiscovery

def test_init():
    obj = DrugDiscovery()
    stats = obj.get_stats()
    assert stats["total_ops"] == 0

def test_operation():
    obj = DrugDiscovery()
    result = obj.parse_smiles(input="test")
    assert result["processed"] is True
    assert result["operation"] == "parse_smiles"

def test_multiple_ops():
    obj = DrugDiscovery()
    for m in ['parse_smiles', 'build_graph', 'predict_properties']:
        getattr(obj, m)(data="test")
    assert obj.get_stats()["total_ops"] == 3

def test_caching():
    obj = DrugDiscovery()
    r1 = obj.parse_smiles(key="same")
    r2 = obj.parse_smiles(key="same")
    assert r2.get("cached") is True

def test_reset():
    obj = DrugDiscovery()
    obj.parse_smiles()
    obj.reset()
    assert obj.get_stats()["total_ops"] == 0

def test_stats():
    obj = DrugDiscovery()
    obj.parse_smiles(x=1)
    obj.build_graph(y=2)
    stats = obj.get_stats()
    assert stats["total_ops"] == 2
    assert "ops_by_type" in stats
