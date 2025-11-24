# Fibulopedia - Quick Start Guide

## Installation & Setup

### 1. Prerequisites
- Python 3.10 or higher
- pip (Python package installer)

### 2. Install Dependencies

Open PowerShell in the project directory and run:

```powershell
pip install -r requirements.txt
```

### 3. Verify Installation

Check that all files are in place:
- `app.py` - Main entry point
- `src/` - Core application code
- `pages/` - Streamlit pages
- `content/` - Data files (JSON)
- `assets/` - Styles and images
- `tests/` - Unit tests

### 4. Run the Application

Start the Streamlit app:

```powershell
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## Testing

Run the unit tests:

```powershell
pytest tests/
```

Run tests with coverage:

```powershell
pytest tests/ --cov=src --cov-report=html
```

## Project Structure

```
fibula_wiki_2/
├── app.py                          # Main Streamlit entry point
├── pages/                          # Multi-page app pages
│   ├── 1_Home.py
│   ├── 2_Weapons.py
│   ├── 3_Equipment.py
│   ├── 4_Spells.py
│   ├── 5_Monsters.py
│   ├── 6_Quests.py
│   ├── 7_Map.py
│   ├── 8_Server_Info.py
│   ├── 9_Search.py
│   └── 10_About.py
├── src/                            # Core application logic
│   ├── __init__.py
│   ├── config.py                   # Configuration and constants
│   ├── models.py                   # Data models (dataclasses)
│   ├── logging_utils.py            # Logging configuration
│   ├── services/                   # Business logic layer
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   ├── weapons_service.py
│   │   ├── equipment_service.py
│   │   ├── spells_service.py
│   │   ├── monsters_service.py
│   │   ├── quests_service.py
│   │   ├── server_info_service.py
│   │   └── search_service.py
│   └── ui/                         # UI components and layouts
│       ├── __init__.py
│       ├── components.py
│       └── layout.py
├── content/                        # Static data files
│   ├── weapons.json
│   ├── equipment.json
│   ├── spells.json
│   ├── monsters.json
│   ├── quests.json
│   └── server_info.json
├── assets/                         # Static assets
│   ├── styles.css
│   ├── logo_placeholder.txt        # Replace with logo_fibulopedia.png
│   └── map_placeholder.txt         # Replace with map.png
├── tests/                          # Unit tests
│   ├── __init__.py
│   ├── test_data_loader.py
│   ├── test_weapons_service.py
│   └── test_search_service.py
├── .streamlit/                     # Streamlit configuration
│   └── config.toml
├── requirements.txt
├── README.md
├── CHANGELOG.md
├── TODO.md
└── .gitignore
```

## Adding Content

### Add New Weapons

Edit `content/weapons.json` and add entries following this format:

```json
{
  "id": "weapon_xxx",
  "type": "sword",
  "name": "New Sword",
  "attack": 50,
  "defense": 30,
  "weight": 45.0,
  "dropped_by": ["Monster Name"],
  "buy_from": [{"npc": "Seller", "price": 1000}],
  "sell_to": [{"npc": "Buyer", "price": 500}],
  "description": "Description here"
}
```

### Add Images

1. **Logo**: Add `logo_fibulopedia.png` to `assets/` folder
   - Recommended: 200x200 pixels, PNG format
   
2. **Map**: Add `map.png` to `assets/` folder
   - Recommended: High resolution PNG of Tibia 7.1 map

### Customize Theme

Edit `assets/styles.css` or `.streamlit/config.toml` to change colors and styling.

## Common Tasks

### Update Server Information

Edit `content/server_info.json` to update rates, links, or description.

### Add New Pages

1. Create new page file in `pages/` directory
2. Name it with number prefix: `11_NewPage.py`
3. Update `src/config.py` NAVIGATION_ITEMS if needed

### Modify Search Behavior

Edit `src/services/search_service.py` to customize search algorithms or result ranking.

## Troubleshooting

### Import Errors

If you see import errors, ensure you're running commands from the project root directory:

```powershell
cd fibula_wiki_2
streamlit run app.py
```

### Port Already in Use

If port 8501 is already in use, specify a different port:

```powershell
streamlit run app.py --server.port 8502
```

### Data Not Loading

Check that all JSON files in `content/` are valid:
- No trailing commas
- Proper quotes (double quotes only)
- All required fields present

## Development

### Code Style

The project follows PEP8 standards. Use a linter:

```powershell
pip install flake8
flake8 src/ tests/
```

### Type Checking

Use mypy for static type checking:

```powershell
pip install mypy
mypy src/
```

## Deployment

### Deploy to Streamlit Cloud

1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Configure secrets if needed
4. Deploy!

### Deploy with Docker

Create a Dockerfile:

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

Build and run:

```powershell
docker build -t fibulopedia .
docker run -p 8501:8501 fibulopedia
```

## Support

- Check TODO.md for planned features
- Review CHANGELOG.md for version history
- Consult README.md for detailed information

## License

This is an unofficial fan project for the Fibula Project community.
Tibia is a registered trademark of CipSoft GmbH.
