"""
Spells page for Fibulopedia.

This page displays all spells with filtering by vocation and level.
Users can view spell incantations, mana costs, and effects.
"""

import streamlit as st
import pandas as pd

from src.services.spells_service import load_spells, search_spells, get_vocations, filter_spells_by_vocation
from src.ui.layout import (
    setup_page_config,
    load_custom_css,
    create_page_header,
    create_sidebar_navigation,
    create_footer
)
from src.ui.components import create_type_badge
from src.logging_utils import setup_logger

logger = setup_logger(__name__)

# Configure page
setup_page_config("Spells", "✨")
load_custom_css()
create_sidebar_navigation()


def main() -> None:
    """Main function to render the spells page."""
    logger.info("Rendering spells page")
    
    # Page header
    create_page_header(
        title="Spells",
        subtitle="Discover all spells and their incantations",
        icon="✨"
    )
    
    # Search and filter section
    col1, col2, col3 = st.columns([3, 1, 1])
    
    with col1:
        search_query = st.text_input(
            "Search spells",
            placeholder="Search by name, incantation, effect, or vocation...",
            key="spell_search"
        )
    
    with col2:
        vocations = ["All"] + get_vocations()
        selected_vocation = st.selectbox(
            "Filter by vocation",
            options=vocations,
            key="spell_vocation_filter"
        )
    
    with col3:
        sort_by = st.selectbox(
            "Sort by",
            options=["Name", "Level", "Mana", "Vocation"],
            key="spell_sort"
        )
    
    # Load and filter spells
    if search_query:
        spells = search_spells(search_query)
    else:
        spells = load_spells()
    
    # Apply vocation filter
    if selected_vocation != "All":
        spells = [s for s in spells if s.vocation == selected_vocation or s.vocation == "All"]
    
    # Display count
    st.markdown(f"**Found {len(spells)} spell(s)**")
    
    if not spells:
        st.info("No spells found matching your criteria.")
        create_footer()
        return
    
    # Convert to DataFrame for display
    spells_data = []
    for spell in spells:
        spells_data.append({
            "ID": spell.id,
            "Name": spell.name,
            "Incantation": spell.incantation,
            "Vocation": spell.vocation,
            "Level": spell.level,
            "Mana": spell.mana,
            "Effect": spell.effect[:50] + "..." if len(spell.effect) > 50 else spell.effect
        })
    
    df = pd.DataFrame(spells_data)
    
    # Sort DataFrame
    sort_column_map = {
        "Name": "Name",
        "Level": "Level",
        "Mana": "Mana",
        "Vocation": "Vocation"
    }
    sort_column = sort_column_map[sort_by]
    df = df.sort_values(by=sort_column, ascending=(sort_by in ["Name", "Vocation"]))
    
    # Display table
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "ID": None,  # Hide ID column
            "Incantation": st.column_config.TextColumn(
                "Incantation",
                help="Magic words to cast the spell"
            ),
            "Level": st.column_config.NumberColumn(
                "Level",
                help="Required level",
                format="%d"
            ),
            "Mana": st.column_config.NumberColumn(
                "Mana",
                help="Mana cost",
                format="%d"
            )
        }
    )
    
    # Spell detail section
    st.markdown("---")
    st.subheader("Spell Details")
    st.markdown("Select a spell to view full details:")
    
    spell_id = st.selectbox(
        "Select spell",
        options=[s.id for s in spells],
        format_func=lambda x: next((s.name for s in spells if s.id == x), x),
        key="spell_detail_select"
    )
    
    if spell_id:
        selected_spell = next((s for s in spells if s.id == spell_id), None)
        
        if selected_spell:
            st.markdown(f"### {selected_spell.name}")
            st.markdown(create_type_badge(selected_spell.vocation), unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**Incantation:** `{selected_spell.incantation}`")
                st.markdown(f"**Vocation:** {selected_spell.vocation}")
                st.markdown(f"**Required Level:** {selected_spell.level}")
                st.markdown(f"**Mana Cost:** {selected_spell.mana}")
            
            with col2:
                if selected_spell.type:
                    st.markdown(f"**Type:** {selected_spell.type}")
                st.markdown(f"**Effect:** {selected_spell.effect}")
    
    # Footer
    create_footer()


if __name__ == "__main__":
    main()
