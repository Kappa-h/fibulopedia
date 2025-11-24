"""
Monsters page for Fibulopedia.

This page displays all monsters with their HP, EXP, loot, and locations.
Users can search monsters and plan their hunting strategies.
"""

import streamlit as st
import pandas as pd

from src.services.monsters_service import load_monsters, search_monsters, get_locations
from src.ui.layout import (
    setup_page_config,
    load_custom_css,
    create_page_header,
    create_sidebar_navigation,
    create_footer
)
from src.logging_utils import setup_logger

logger = setup_logger(__name__)

# Configure page
setup_page_config("Monsters", "👹")
load_custom_css()
create_sidebar_navigation()


def main() -> None:
    """Main function to render the monsters page."""
    logger.info("Rendering monsters page")
    
    # Page header
    create_page_header(
        title="Monsters",
        subtitle="Check monsters, their HP, EXP and valuable loot",
        icon="👹"
    )
    
    # Search and filter section
    col1, col2, col3 = st.columns([3, 1, 1])
    
    with col1:
        search_query = st.text_input(
            "Search monsters",
            placeholder="Search by name, location, or loot...",
            key="monster_search"
        )
    
    with col2:
        locations = ["All"] + get_locations()
        selected_location = st.selectbox(
            "Filter by location",
            options=locations,
            key="monster_location_filter"
        )
    
    with col3:
        sort_by = st.selectbox(
            "Sort by",
            options=["Name", "HP", "EXP", "Location"],
            key="monster_sort"
        )
    
    # Load and filter monsters
    if search_query:
        monsters = search_monsters(search_query)
    else:
        monsters = load_monsters()
    
    # Apply location filter
    if selected_location != "All":
        monsters = [m for m in monsters if m.location == selected_location]
    
    # Display count
    st.markdown(f"**Found {len(monsters)} monster(s)**")
    
    if not monsters:
        st.info("No monsters found matching your criteria.")
        create_footer()
        return
    
    # Convert to DataFrame for display
    monsters_data = []
    for monster in monsters:
        monsters_data.append({
            "ID": monster.id,
            "Name": monster.name,
            "HP": monster.hp,
            "EXP": monster.exp,
            "Location": monster.location,
            "Loot": monster.loot[:50] + "..." if len(monster.loot) > 50 else monster.loot
        })
    
    df = pd.DataFrame(monsters_data)
    
    # Sort DataFrame
    sort_column_map = {
        "Name": "Name",
        "HP": "HP",
        "EXP": "EXP",
        "Location": "Location"
    }
    sort_column = sort_column_map[sort_by]
    df = df.sort_values(by=sort_column, ascending=(sort_by in ["Name", "Location"]))
    
    # Display table
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "ID": None,  # Hide ID column
            "HP": st.column_config.NumberColumn(
                "HP",
                help="Hit points",
                format="%d"
            ),
            "EXP": st.column_config.NumberColumn(
                "EXP",
                help="Experience points",
                format="%d"
            )
        }
    )
    
    # Monster detail section
    st.markdown("---")
    st.subheader("Monster Details")
    st.markdown("Select a monster to view full details:")
    
    monster_id = st.selectbox(
        "Select monster",
        options=[m.id for m in monsters],
        format_func=lambda x: next((m.name for m in monsters if m.id == x), x),
        key="monster_detail_select"
    )
    
    if monster_id:
        selected_monster = next((m for m in monsters if m.id == monster_id), None)
        
        if selected_monster:
            st.markdown(f"### {selected_monster.name}")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**HP:** {selected_monster.hp}")
                st.markdown(f"**EXP:** {selected_monster.exp}")
                st.markdown(f"**Location:** {selected_monster.location}")
                
                if selected_monster.difficulty:
                    st.markdown(f"**Difficulty:** {selected_monster.difficulty}")
            
            with col2:
                st.markdown("**Loot:**")
                st.markdown(selected_monster.loot)
    
    # Footer
    create_footer()


if __name__ == "__main__":
    main()
