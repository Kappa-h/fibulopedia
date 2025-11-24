"""
Unit tests for data_loader module.

Tests the generic data loading utilities including JSON loading,
validation, and type conversion functions.
"""

import pytest
import json
from pathlib import Path
import tempfile

from src.services.data_loader import (
    load_json,
    save_json,
    validate_required_fields,
    safe_int,
    safe_float,
    safe_list
)


class TestLoadJson:
    """Tests for load_json function."""
    
    def test_load_valid_json(self):
        """Test loading a valid JSON file."""
        # Create a temporary JSON file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            test_data = [{"id": "1", "name": "Test"}]
            json.dump(test_data, f)
            temp_path = Path(f.name)
        
        try:
            result = load_json(temp_path)
            assert result is not None
            assert isinstance(result, list)
            assert len(result) == 1
            assert result[0]["name"] == "Test"
        finally:
            temp_path.unlink()
    
    def test_load_nonexistent_file(self):
        """Test loading a file that doesn't exist."""
        result = load_json(Path("nonexistent_file.json"))
        assert result is None
    
    def test_load_invalid_json(self):
        """Test loading a file with invalid JSON."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            f.write("{ invalid json }")
            temp_path = Path(f.name)
        
        try:
            result = load_json(temp_path)
            assert result is None
        finally:
            temp_path.unlink()


class TestSaveJson:
    """Tests for save_json function."""
    
    def test_save_valid_data(self):
        """Test saving valid data to JSON."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_path = Path(f.name)
        
        try:
            test_data = {"name": "Test", "value": 123}
            result = save_json(temp_path, test_data)
            assert result is True
            
            # Verify the file was created and contains correct data
            loaded_data = load_json(temp_path)
            assert loaded_data == test_data
        finally:
            if temp_path.exists():
                temp_path.unlink()


class TestValidateRequiredFields:
    """Tests for validate_required_fields function."""
    
    def test_all_fields_present(self):
        """Test validation when all required fields are present."""
        data = {"id": "1", "name": "Test", "value": 100}
        required = ["id", "name", "value"]
        assert validate_required_fields(data, required) is True
    
    def test_missing_field(self):
        """Test validation when a required field is missing."""
        data = {"id": "1", "name": "Test"}
        required = ["id", "name", "value"]
        assert validate_required_fields(data, required) is False
    
    def test_extra_fields(self):
        """Test validation with extra non-required fields."""
        data = {"id": "1", "name": "Test", "extra": "data"}
        required = ["id", "name"]
        assert validate_required_fields(data, required) is True


class TestSafeInt:
    """Tests for safe_int function."""
    
    def test_valid_int(self):
        """Test conversion of valid integer."""
        assert safe_int(42) == 42
        assert safe_int("42") == 42
    
    def test_invalid_int(self):
        """Test conversion of invalid integer with default."""
        assert safe_int("not a number", default=0) == 0
        assert safe_int(None, default=10) == 10
    
    def test_float_to_int(self):
        """Test conversion of float to int."""
        assert safe_int(42.7) == 42
        # String "42.7" cannot be directly converted to int, returns default 0
        assert safe_int("42.7") == 0
        # Use float conversion first if needed
        assert safe_int(float("42.7")) == 42


class TestSafeFloat:
    """Tests for safe_float function."""
    
    def test_valid_float(self):
        """Test conversion of valid float."""
        assert safe_float(42.5) == 42.5
        assert safe_float("42.5") == 42.5
    
    def test_invalid_float(self):
        """Test conversion of invalid float with default."""
        assert safe_float("not a number", default=0.0) == 0.0
        assert safe_float(None, default=1.5) == 1.5
    
    def test_int_to_float(self):
        """Test conversion of int to float."""
        assert safe_float(42) == 42.0


class TestSafeList:
    """Tests for safe_list function."""
    
    def test_valid_list(self):
        """Test conversion of valid list."""
        assert safe_list([1, 2, 3]) == [1, 2, 3]
    
    def test_none_to_list(self):
        """Test conversion of None to empty list."""
        assert safe_list(None) == []
    
    def test_single_value_to_list(self):
        """Test conversion of single value to list."""
        assert safe_list("value") == ["value"]
    
    def test_custom_default(self):
        """Test with custom default list."""
        assert safe_list(None, default=["default"]) == ["default"]


if __name__ == "__main__":
    pytest.main([__file__])
