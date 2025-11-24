"""
Reusable UI components for Fibulopedia.

This module contains functions for creating consistent UI elements
such as cards, tables, badges, and other visual components used
throughout the application.
"""

import streamlit as st
import pandas as pd
from typing import Any, Optional

from src.config import Theme


def create_card(
    title: str,
    content: str,
    icon: str = "",
    link: Optional[str] = None,
    button_text: str = "View"
) -> None:
    """
    Create a styled card component.
    
    Args:
        title: Card title text.
        content: Card body content.
        icon: Optional emoji icon to display.
        link: Optional page link for navigation.
        button_text: Text for the navigation button.
    
    Example:
        >>> create_card("Weapons", "Browse all weapons", "⚔️", "Weapons")
    """
    with st.container():
        st.markdown(
            f"""
            <div class="card">
                <h3>{icon} {title}</h3>
                <p>{content}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        if link:
            if st.button(button_text, key=f"btn_{title}", use_container_width=True):
                st.switch_page(f"pages/{link}.py")


def create_hub_card(title: str, icon: str, description: str, page: str) -> None:
    """
    Create a clickable hub card for the home page.
    
    Args:
        title: Card title.
        icon: Emoji icon.
        description: Card description text.
        page: Target page name for navigation.
    
    Example:
        >>> create_hub_card("Weapons", "⚔️", "Browse weapons", "2_Weapons")
    """
    with st.container():
        st.markdown(
            f"""
            <div class="compact-hub-card">
                <div class="compact-hub-icon">{icon}</div>
                <div class="compact-hub-title">{title}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        # Use unique key based on page name
        if st.button(f"Go to {title}", key=f"hub_{page}", use_container_width=True, type="secondary"):
            st.switch_page(f"pages/{page}.py")


def create_stat_badge(label: str, value: Any, color: str = Theme.PRIMARY_COLOR) -> str:
    """
    Create an HTML badge for displaying stats.
    
    Args:
        label: Badge label text.
        value: Badge value.
        color: Background color for the badge.
    
    Returns:
        HTML string for the badge.
    
    Example:
        >>> badge = create_stat_badge("HP", 100)
        >>> st.markdown(badge, unsafe_allow_html=True)
    """
    return f"""
    <span class="stat-badge" style="background-color: {color};">
        <strong>{label}:</strong> {value}
    </span>
    """


def create_type_badge(type_name: str) -> str:
    """
    Create a colored badge for entity types.
    
    Args:
        type_name: The type name (weapon, spell, monster, etc.).
    
    Returns:
        HTML string for the type badge.
    
    Example:
        >>> badge = create_type_badge("sword")
        >>> st.markdown(badge, unsafe_allow_html=True)
    """
    # Color mapping for different types
    type_colors = {
        "sword": "#4a90e2",
        "axe": "#e24a4a",
        "club": "#8b4513",
        "distance": "#50c878",
        "spell": "#9370db",
        "monster": "#ff6347",
        "quest": "#ffd700",
        "helmet": "#708090",
        "armor": "#778899",
        "legs": "#696969",
        "boots": "#8b7355",
        "shield": "#4682b4",
        "ring": "#daa520",
        "amulet": "#da70d6"
    }
    
    color = type_colors.get(type_name.lower(), Theme.SECONDARY_COLOR)
    
    return f"""
    <span class="type-badge" style="background-color: {color};">
        {type_name}
    </span>
    """


def create_data_table(
    data: list[dict[str, Any]],
    columns: Optional[list[str]] = None,
    sortable: bool = True
) -> None:
    """
    Create a sortable data table using pandas DataFrame.
    
    Args:
        data: List of dictionaries containing row data.
        columns: Optional list of column names to display. If None, all columns shown.
        sortable: Whether to enable interactive sorting.
    
    Example:
        >>> weapons_data = [{"name": "Sword", "attack": 30}]
        >>> create_data_table(weapons_data)
    """
    if not data:
        st.info("No data available.")
        return
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Filter columns if specified
    if columns:
        df = df[[col for col in columns if col in df.columns]]
    
    # Display the table
    if sortable:
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.table(df)


def create_detail_section(title: str, content: dict[str, Any]) -> None:
    """
    Create a detail section for displaying entity information.
    
    Args:
        title: Section title.
        content: Dictionary of field names and values to display.
    
    Example:
        >>> details = {"Name": "Dragon", "HP": 1000, "EXP": 500}
        >>> create_detail_section("Monster Details", details)
    """
    st.subheader(title)
    
    with st.container():
        for key, value in content.items():
            if isinstance(value, list) and value:
                st.markdown(f"**{key}:** {', '.join(str(v) for v in value)}")
            elif value:
                st.markdown(f"**{key}:** {value}")


def create_search_result_item(
    entity_type: str,
    name: str,
    snippet: Optional[str] = None,
    entity_id: Optional[str] = None
) -> None:
    """
    Create a search result item display.
    
    Args:
        entity_type: Type of entity (weapon, spell, etc.).
        name: Name of the entity.
        snippet: Optional text snippet showing context.
        entity_id: Optional entity ID for linking.
    
    Example:
        >>> create_search_result_item("weapon", "Dragon Slayer", "A powerful sword...")
    """
    # Icon mapping for entity types
    type_icons = {
        "weapon": "⚔️",
        "equipment": "🛡️",
        "spell": "✨",
        "monster": "👹",
        "quest": "📜"
    }
    
    icon = type_icons.get(entity_type.lower(), "📄")
    type_badge_html = create_type_badge(entity_type)
    
    with st.container():
        st.markdown(
            f"""
            <div class="search-result-item">
                <div class="search-result-header">
                    <span class="search-result-icon">{icon}</span>
                    <strong class="search-result-name">{name}</strong>
                    {type_badge_html}
                </div>
                <p class="search-result-snippet">{snippet if snippet else ''}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


def create_info_box(message: str, box_type: str = "info") -> None:
    """
    Create a styled information box.
    
    Args:
        message: The message to display.
        box_type: Type of box (info, success, warning, error).
    
    Example:
        >>> create_info_box("Data loaded successfully!", "success")
    """
    if box_type == "info":
        st.info(message)
    elif box_type == "success":
        st.success(message)
    elif box_type == "warning":
        st.warning(message)
    elif box_type == "error":
        st.error(message)


def create_filter_sidebar(
    filters: dict[str, list[str]],
    filter_key_prefix: str = "filter"
) -> dict[str, str]:
    """
    Create a sidebar with filter options.
    
    Args:
        filters: Dictionary mapping filter names to their option lists.
        filter_key_prefix: Prefix for session state keys.
    
    Returns:
        Dictionary of selected filter values.
    
    Example:
        >>> filters = {"Type": ["sword", "axe", "club"]}
        >>> selected = create_filter_sidebar(filters)
    """
    selected_filters = {}
    
    with st.sidebar:
        st.subheader("Filters")
        
        for filter_name, options in filters.items():
            key = f"{filter_key_prefix}_{filter_name.lower()}"
            selected = st.selectbox(
                filter_name,
                options=["All"] + options,
                key=key
            )
            selected_filters[filter_name] = selected if selected != "All" else None
    
    return selected_filters


def display_loading_spinner(message: str = "Loading...") -> Any:
    """
    Display a loading spinner context manager.
    
    Args:
        message: Message to display while loading.
    
    Returns:
        Streamlit spinner context manager.
    
    Example:
        >>> with display_loading_spinner("Loading weapons..."):
        ...     weapons = load_weapons()
    """
    return st.spinner(message)
