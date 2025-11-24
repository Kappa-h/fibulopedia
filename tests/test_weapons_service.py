"""
Unit tests for weapons_service module.

Tests the weapons service functionality including loading,
searching, filtering, and retrieving weapon data.
"""

import pytest
from unittest.mock import patch, MagicMock

from src.models import Weapon
from src.services.weapons_service import (
    load_weapons,
    get_weapon_by_id,
    filter_weapons_by_type,
    search_weapons,
    get_weapon_types
)


# Mock data for testing
MOCK_WEAPONS = [
    Weapon(
        id="weapon_001",
        type="sword",
        name="Serpent Sword",
        attack=46,
        defense=26,
        weight=42.0,
        dropped_by=["Dragon", "Dragon Lord"],
        buy_from=[],
        sell_to=[{"npc": "Rashid", "price": 900}],
        description="A powerful sword"
    ),
    Weapon(
        id="weapon_002",
        type="sword",
        name="Bright Sword",
        attack=41,
        defense=20,
        weight=42.0,
        dropped_by=["Hero"],
        buy_from=[],
        sell_to=[{"npc": "Rashid", "price": 500}],
        description="A shining blade"
    ),
    Weapon(
        id="weapon_003",
        type="axe",
        name="Knight Axe",
        attack=45,
        defense=20,
        weight=85.0,
        dropped_by=["Orc Warlord"],
        buy_from=[{"npc": "Weapon Shop", "price": 2000}],
        sell_to=[{"npc": "Weapon Shop", "price": 500}],
        description="A heavy battle axe"
    ),
]


class TestLoadWeapons:
    """Tests for load_weapons function."""
    
    @patch('src.services.weapons_service.load_json')
    def test_load_weapons_success(self, mock_load_json):
        """Test successful loading of weapons."""
        mock_load_json.return_value = [
            {
                "id": "weapon_001",
                "type": "sword",
                "name": "Test Sword",
                "attack": 30,
                "defense": 20,
                "weight": 40.0,
                "dropped_by": ["Monster"],
                "buy_from": [],
                "sell_to": []
            }
        ]
        
        weapons = load_weapons()
        assert len(weapons) > 0
        assert isinstance(weapons[0], Weapon)
    
    @patch('src.services.weapons_service.load_json')
    def test_load_weapons_empty(self, mock_load_json):
        """Test loading with no data."""
        mock_load_json.return_value = []
        
        weapons = load_weapons()
        assert weapons == []
    
    @patch('src.services.weapons_service.load_json')
    def test_load_weapons_invalid_data(self, mock_load_json):
        """Test loading with invalid data structure."""
        mock_load_json.return_value = None
        
        weapons = load_weapons()
        assert weapons == []


class TestGetWeaponById:
    """Tests for get_weapon_by_id function."""
    
    @patch('src.services.weapons_service.load_weapons')
    def test_get_existing_weapon(self, mock_load_weapons):
        """Test retrieving an existing weapon by ID."""
        mock_load_weapons.return_value = MOCK_WEAPONS
        
        weapon = get_weapon_by_id("weapon_001")
        assert weapon is not None
        assert weapon.name == "Serpent Sword"
    
    @patch('src.services.weapons_service.load_weapons')
    def test_get_nonexistent_weapon(self, mock_load_weapons):
        """Test retrieving a weapon that doesn't exist."""
        mock_load_weapons.return_value = MOCK_WEAPONS
        
        weapon = get_weapon_by_id("weapon_999")
        assert weapon is None


class TestFilterWeaponsByType:
    """Tests for filter_weapons_by_type function."""
    
    @patch('src.services.weapons_service.load_weapons')
    def test_filter_by_sword(self, mock_load_weapons):
        """Test filtering weapons by sword type."""
        mock_load_weapons.return_value = MOCK_WEAPONS
        
        swords = filter_weapons_by_type("sword")
        assert len(swords) == 2
        assert all(w.type == "sword" for w in swords)
    
    @patch('src.services.weapons_service.load_weapons')
    def test_filter_by_axe(self, mock_load_weapons):
        """Test filtering weapons by axe type."""
        mock_load_weapons.return_value = MOCK_WEAPONS
        
        axes = filter_weapons_by_type("axe")
        assert len(axes) == 1
        assert axes[0].type == "axe"
    
    @patch('src.services.weapons_service.load_weapons')
    def test_filter_nonexistent_type(self, mock_load_weapons):
        """Test filtering by a type that doesn't exist."""
        mock_load_weapons.return_value = MOCK_WEAPONS
        
        weapons = filter_weapons_by_type("bow")
        assert len(weapons) == 0


class TestSearchWeapons:
    """Tests for search_weapons function."""
    
    @patch('src.services.weapons_service.load_weapons')
    def test_search_by_name(self, mock_load_weapons):
        """Test searching weapons by name."""
        mock_load_weapons.return_value = MOCK_WEAPONS
        
        results = search_weapons("Serpent")
        assert len(results) == 1
        assert results[0].name == "Serpent Sword"
    
    @patch('src.services.weapons_service.load_weapons')
    def test_search_by_type(self, mock_load_weapons):
        """Test searching weapons by type."""
        mock_load_weapons.return_value = MOCK_WEAPONS
        
        results = search_weapons("sword")
        assert len(results) >= 2
    
    @patch('src.services.weapons_service.load_weapons')
    def test_search_by_monster(self, mock_load_weapons):
        """Test searching weapons by monster name."""
        mock_load_weapons.return_value = MOCK_WEAPONS
        
        results = search_weapons("Dragon")
        assert len(results) >= 1
        assert any("Dragon" in w.dropped_by for w in results)
    
    @patch('src.services.weapons_service.load_weapons')
    def test_search_empty_query(self, mock_load_weapons):
        """Test searching with empty query returns all weapons."""
        mock_load_weapons.return_value = MOCK_WEAPONS
        
        results = search_weapons("")
        assert len(results) == len(MOCK_WEAPONS)
    
    @patch('src.services.weapons_service.load_weapons')
    def test_search_no_results(self, mock_load_weapons):
        """Test searching with query that matches nothing."""
        mock_load_weapons.return_value = MOCK_WEAPONS
        
        results = search_weapons("nonexistent")
        assert len(results) == 0


class TestGetWeaponTypes:
    """Tests for get_weapon_types function."""
    
    @patch('src.services.weapons_service.load_weapons')
    def test_get_weapon_types(self, mock_load_weapons):
        """Test retrieving all weapon types."""
        mock_load_weapons.return_value = MOCK_WEAPONS
        
        types = get_weapon_types()
        assert "sword" in types
        assert "axe" in types
        assert len(types) == 2  # Only sword and axe in mock data


if __name__ == "__main__":
    pytest.main([__file__])
