# Fibulopedia

**Fibulopedia** is an unofficial guide and wiki for the Fibula Project, a Tibia 7.1 style Open Tibia Server (OTS). This is a data-driven web application built with Streamlit that provides comprehensive information about weapons, equipment, spells, monsters, quests, and more.

## Features

- **Weapons**: Browse all weapons with sortable tables and advanced filtering
- **Equipment**: View equipment organized by slots (helmet, armor, legs, boots, shield, ring, amulet)
- **Spells**: Search spells by vocation, level, mana cost, and incantation
- **Monsters**: Check monster stats including HP, EXP, loot, and locations
- **Quests**: Discover available quests with locations and rewards
- **Map**: View the classic Tibia 7.1 map
- **Server Info**: Learn about server rates, rules, and general information
- **Advanced Search**: Global search across all content types

## Project Structure

```
fibula_wiki_2/
├── app.py                      # Main Streamlit entry point
├── pages/                      # Streamlit multi-page app pages
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
├── src/                        # Core application logic
│   ├── config.py              # Configuration and constants
│   ├── models.py              # Data models (dataclasses)
│   ├── logging_utils.py       # Logging configuration
│   ├── services/              # Business logic layer
│   │   ├── data_loader.py
│   │   ├── weapons_service.py
│   │   ├── equipment_service.py
│   │   ├── spells_service.py
│   │   ├── monsters_service.py
│   │   ├── quests_service.py
│   │   ├── server_info_service.py
│   │   └── search_service.py
│   └── ui/                    # UI components and layouts
│       ├── components.py
│       └── layout.py
├── content/                    # Static data files
│   ├── weapons.json
│   ├── equipment.json
│   ├── spells.json
│   ├── monsters.json
│   ├── quests.json
│   └── server_info.json
├── assets/                     # Static assets
│   ├── styles.css
│   ├── logo_fibulopedia.png
│   └── map.png
├── tests/                      # Unit tests
│   ├── test_data_loader.py
│   ├── test_weapons_service.py
│   └── test_search_service.py
├── requirements.txt
├── CHANGELOG.md
├── TODO.md
└── README.md
```

## Installation

1. **Clone the repository** (or navigate to the project directory)

2. **Create a virtual environment** (recommended):
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

## Running the Application

To start the Streamlit application:

```powershell
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## Development

### Code Quality Standards

This project follows strict coding standards:

- **Type hints** on all public functions and methods
- **Docstrings** for all modules, classes, and public functions
- **Logging** instead of print statements
- **Modular architecture** with clear separation of concerns
- **PEP8** compliance

### Running Tests

To run the unit tests:

```powershell
pytest tests/
```

### Adding New Content

Content is stored as JSON files in the `content/` directory. To add new items:

1. Open the relevant JSON file (e.g., `content/weapons.json`)
2. Add your new entry following the existing structure
3. Ensure all required fields are present
4. Restart the application to see changes

### Customizing the Theme

The visual theme can be customized in two places:

1. **assets/styles.css**: Modify CSS variables and styles
2. **src/config.py**: Update theme configuration values

## Future Roadmap

See `TODO.md` for planned features including:

- Internal linking between entities (e.g., click monster name to see monster details)
- Multi-language support (Polish, Swedish, Brazilian Portuguese)
- Content editor for administrators
- Interactive map with clickable markers
- API integration with live server data
- User authentication and favorite items

## License

This is an unofficial fan project. Tibia is a registered trademark of CipSoft GmbH.

## Credits

Created for the Fibula Project community.
