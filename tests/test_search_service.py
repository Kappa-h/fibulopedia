"""
Unit tests for search_service module.

Tests the global search functionality across all content types.
"""

import pytest
from unittest.mock import patch, MagicMock

from src.models import Weapon, EquipmentItem, Spell, Monster, Quest, SearchResult
from src.services.search_service import (
    create_snippet,
    search_all,
    search_by_entity_type
)


class TestCreateSnippet:
    """Tests for create_snippet function."""
    
    def test_snippet_with_query_found(self):
        """Test creating snippet when query is found in text."""
        text = "This is a long text about dragons and their treasures"
        query = "dragon"

        snippet = create_snippet(text, query, max_length=30)
        assert "dragon" in snippet.lower()
        # Snippet includes context around match plus ellipsis, can be ~40% longer
        assert len(snippet) <= 50

    def test_snippet_query_not_found(self):
        """Test creating snippet when query is not found."""
        text = "This is some text"
        query = "notfound"
        
        snippet = create_snippet(text, query, max_length=20)
        assert len(snippet) <= 25  # Allow for ellipsis
    
    def test_snippet_empty_text(self):
        """Test creating snippet with empty text."""
        snippet = create_snippet("", "query", max_length=50)
        assert snippet == ""
    
    def test_snippet_short_text(self):
        """Test creating snippet with text shorter than max_length."""
        text = "Short text"
        snippet = create_snippet(text, "text", max_length=50)
        assert snippet == text


class TestSearchAll:
    """Tests for search_all function."""
    
    @patch('src.services.search_service.weapons_service.search_weapons')
    @patch('src.services.search_service.equipment_service.search_equipment')
    @patch('src.services.search_service.spells_service.search_spells')
    @patch('src.services.search_service.monsters_service.search_monsters')
    @patch('src.services.search_service.quests_service.search_quests')
    def test_search_all_with_results(
        self,
        mock_search_quests,
        mock_search_monsters,
        mock_search_spells,
        mock_search_equipment,
        mock_search_weapons
    ):
        """Test global search returning results from multiple sources."""
        # Setup mock data
        mock_search_weapons.return_value = [
            Weapon(
                id="w1", type="sword", name="Dragon Sword", attack=50,
                defense=25, weight=40.0, dropped_by=[], buy_from=[], sell_to=[]
            )
        ]
        mock_search_equipment.return_value = []
        mock_search_spells.return_value = [
            Spell(
                id="s1", name="Dragon Fire", incantation="exori flam",
                vocation="Sorcerer", level=30, mana=50,
                effect="Burns enemies with dragon fire"
            )
        ]
        mock_search_monsters.return_value = [
            Monster(
                id="m1", name="Dragon", hp=1000, exp=700,
                loot="Gold, Dragon Scale", location="Dragon Lair"
            )
        ]
        mock_search_quests.return_value = []
        
        results = search_all("dragon")
        
        assert len(results) > 0
        assert any(r.entity_type == "weapon" for r in results)
        assert any(r.entity_type == "spell" for r in results)
        assert any(r.entity_type == "monster" for r in results)
    
    @patch('src.services.search_service.weapons_service.search_weapons')
    @patch('src.services.search_service.equipment_service.search_equipment')
    @patch('src.services.search_service.spells_service.search_spells')
    @patch('src.services.search_service.monsters_service.search_monsters')
    @patch('src.services.search_service.quests_service.search_quests')
    def test_search_all_no_results(
        self,
        mock_search_quests,
        mock_search_monsters,
        mock_search_spells,
        mock_search_equipment,
        mock_search_weapons
    ):
        """Test global search with no matching results."""
        mock_search_weapons.return_value = []
        mock_search_equipment.return_value = []
        mock_search_spells.return_value = []
        mock_search_monsters.return_value = []
        mock_search_quests.return_value = []
        
        results = search_all("nonexistent")
        assert len(results) == 0
    
    def test_search_all_empty_query(self):
        """Test global search with empty query."""
        results = search_all("")
        assert len(results) == 0


class TestSearchByEntityType:
    """Tests for search_by_entity_type function."""
    
    @patch('src.services.search_service.weapons_service.search_weapons')
    def test_search_weapons_only(self, mock_search_weapons):
        """Test searching only weapons."""
        mock_search_weapons.return_value = [
            Weapon(
                id="w1", type="sword", name="Test Sword", attack=30,
                defense=20, weight=40.0, dropped_by=[], buy_from=[], sell_to=[]
            )
        ]
        
        results = search_by_entity_type("sword", "weapon")
        
        assert len(results) > 0
        assert all(r.entity_type == "weapon" for r in results)
    
    @patch('src.services.search_service.spells_service.search_spells')
    def test_search_spells_only(self, mock_search_spells):
        """Test searching only spells."""
        mock_search_spells.return_value = [
            Spell(
                id="s1", name="Fireball", incantation="exori flam",
                vocation="Sorcerer", level=20, mana=40,
                effect="Shoots a fireball"
            )
        ]
        
        results = search_by_entity_type("fire", "spell")
        
        assert len(results) > 0
        assert all(r.entity_type == "spell" for r in results)
    
    @patch('src.services.search_service.monsters_service.search_monsters')
    def test_search_monsters_only(self, mock_search_monsters):
        """Test searching only monsters."""
        mock_search_monsters.return_value = [
            Monster(
                id="m1", name="Dragon", hp=1000, exp=700,
                loot="Gold", location="Cave"
            )
        ]
        
        results = search_by_entity_type("dragon", "monster")
        
        assert len(results) > 0
        assert all(r.entity_type == "monster" for r in results)
    
    def test_search_invalid_entity_type(self):
        """Test searching with invalid entity type."""
        results = search_by_entity_type("query", "invalid_type")
        assert len(results) == 0


if __name__ == "__main__":
    pytest.main([__file__])
