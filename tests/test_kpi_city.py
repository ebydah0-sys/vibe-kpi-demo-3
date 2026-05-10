import pytest
import sqlite3
import os
import sys
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from kpi_city import city_kpi

@pytest.fixture
def setup_test_db():
    db_path = os.path.join('data', 'db', 'analytics.db')
    
    if not os.path.exists(db_path):
        pytest.skip("Database not found. Run ETL script first.")
    
    yield
    
def test_city_kpi_happy_path(setup_test_db, capsys):
    city_kpi("Mumbai")
    captured = capsys.readouterr()
    
    assert "City: Mumbai" in captured.out
    assert "Total Customers:" in captured.out
    assert "Average Monthly Spend:" in captured.out
    assert "Churn Rate:" in captured.out

def test_city_kpi_sql_injection_protection(setup_test_db, capsys):
    city_kpi("Mumbai' OR 1=1 --")
    captured = capsys.readouterr()
    
    assert "No data found for city: Mumbai' OR 1=1 --" in captured.out
    assert "Total Customers:" not in captured.out
