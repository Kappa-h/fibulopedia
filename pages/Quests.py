"""
Quests page for Fibulopedia.

This page displays all available quests with their locations and rewards.
Future versions will include step-by-step walkthroughs.
"""

import streamlit as st
import pandas as pd

from src.services.quests_service import load_quests, search_quests, get_quest_locations
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
setup_page_config("Quests", "📜")
load_custom_css()
create_sidebar_navigation()


def main() -> None:
    """Main function to render the quests page."""
    logger.info("Rendering quests page")
    
    # Page header
    create_page_header(
        title="Quests",
        subtitle="Explore available quests, their locations and rewards",
        icon="📜"
    )
    
    # Search and filter section
    col1, col2, col3 = st.columns([3, 1, 1])
    
    with col1:
        search_query = st.text_input(
            "Search quests",
            placeholder="Search by name, location, or reward...",
            key="quest_search"
        )
    
    with col2:
        locations = ["All"] + get_quest_locations()
        selected_location = st.selectbox(
            "Filter by location",
            options=locations,
            key="quest_location_filter"
        )
    
    with col3:
        sort_by = st.selectbox(
            "Sort by",
            options=["Name", "Location"],
            key="quest_sort"
        )
    
    # Load and filter quests
    if search_query:
        quests = search_quests(search_query)
    else:
        quests = load_quests()
    
    # Apply location filter
    if selected_location != "All":
        quests = [q for q in quests if q.location == selected_location]
    
    # Display count
    st.markdown(f"**Found {len(quests)} quest(s)**")
    
    if not quests:
        st.info("No quests found matching your criteria.")
        create_footer()
        return
    
    # Convert to DataFrame for display
    quests_data = []
    for quest in quests:
        quests_data.append({
            "ID": quest.id,
            "Name": quest.name,
            "Location": quest.location,
            "Description": quest.short_description[:50] + "..." if len(quest.short_description) > 50 else quest.short_description,
            "Reward": quest.reward[:30] + "..." if len(quest.reward) > 30 else quest.reward
        })
    
    df = pd.DataFrame(quests_data)
    
    # Sort DataFrame
    sort_column_map = {
        "Name": "Name",
        "Location": "Location"
    }
    sort_column = sort_column_map[sort_by]
    df = df.sort_values(by=sort_column, ascending=True)
    
    # Display table
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "ID": None,  # Hide ID column
        }
    )
    
    # Quest detail section
    st.markdown("---")
    st.subheader("Quest Details")
    st.markdown("Select a quest to view full details:")
    
    quest_id = st.selectbox(
        "Select quest",
        options=[q.id for q in quests],
        format_func=lambda x: next((q.name for q in quests if q.id == x), x),
        key="quest_detail_select"
    )
    
    if quest_id:
        selected_quest = next((q for q in quests if q.id == quest_id), None)
        
        if selected_quest:
            st.markdown(f"### {selected_quest.name}")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**Location:** {selected_quest.location}")
                st.markdown(f"**Reward:** {selected_quest.reward}")
                
                if selected_quest.difficulty:
                    st.markdown(f"**Difficulty:** {selected_quest.difficulty}")
            
            with col2:
                st.markdown("**Description:**")
                st.markdown(selected_quest.short_description)
                
                if selected_quest.steps:
                    st.markdown("**Steps:**")
                    for i, step in enumerate(selected_quest.steps, 1):
                        st.markdown(f"{i}. {step}")
    
    # Footer
    create_footer()


if __name__ == "__main__":
    main()
