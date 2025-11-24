# Fibulopedia Roadmap & TODO

## Phase 1: Core Foundation ✅ (v0.1.0)

- [x] Project structure and configuration
- [x] Data models for all entities
- [x] Service layer for business logic
- [x] UI components and layout utilities
- [x] All main pages (Weapons, Equipment, Spells, Monsters, Quests, Map, Server Info)
- [x] Home hub page
- [x] Global search functionality
- [x] Dark fantasy theme with custom CSS
- [x] Example static content
- [x] Basic unit tests

## Phase 2: Enhanced Data Relations (v0.2.0)

- [ ] Internal linking system between entities
  - [ ] Click on monster name → navigate to monster detail
  - [ ] Click on item in loot → navigate to item detail
  - [ ] Click on NPC name → show NPC info (if available)
- [ ] Detailed entity pages with back-linking
  - [ ] Show which monsters drop this weapon
  - [ ] Show which quests reward this item
  - [ ] Show which spells can be used by each vocation
- [ ] Cross-reference validation (ensure referenced entities exist)
- [ ] Breadcrumb navigation for detail pages

## Phase 3: Multi-Language Support (v0.3.0)

- [ ] Language selection UI (dropdown in sidebar)
- [ ] Internationalization (i18n) infrastructure
  - [ ] Extract all UI strings to language files
  - [ ] Create `content/languages.json` with translations
- [ ] Language-specific content loading
  - [ ] `content/en/`, `content/pl/`, `content/sv/`, `content/pt_br/`
- [ ] Persist language preference in session state
- [ ] Translation guide for contributors

## Phase 4: Content Management (v0.4.0)

- [ ] Admin authentication system
- [ ] Content editor interface
  - [ ] Add/edit/delete weapons
  - [ ] Add/edit/delete equipment
  - [ ] Add/edit/delete spells
  - [ ] Add/edit/delete monsters
  - [ ] Add/edit/delete quests
- [ ] Content validation before saving
- [ ] Backup system for content files
- [ ] Change history/audit log

## Phase 5: Interactive Map (v0.5.0)

- [ ] Interactive map viewer (using Folium or custom solution)
- [ ] Clickable markers for:
  - [ ] Monster spawn locations
  - [ ] Quest locations
  - [ ] NPC locations
  - [ ] Dungeon entrances
- [ ] Map layers (toggle different information types)
- [ ] Zoom and pan functionality
- [ ] Map coordinate display

## Phase 6: Live Server Integration (v0.6.0)

- [ ] API endpoints for live server data
  - [ ] Online players count
  - [ ] Server status (online/offline)
  - [ ] Recent deaths
  - [ ] Highscores
- [ ] Database integration option (PostgreSQL/SQLite)
- [ ] Real-time updates using WebSocket
- [ ] Player character lookup

## Phase 7: Community Features (v0.7.0)

- [ ] User accounts and authentication
- [ ] Favorite items/spells/monsters
- [ ] Personal notes on entities
- [ ] Comment system for quests
- [ ] Rating system for guides
- [ ] Community-contributed content (with moderation)

## Phase 8: Advanced Features (v0.8.0)

- [ ] Character build planner
  - [ ] Equipment set builder
  - [ ] Skill calculator
  - [ ] Damage calculator
- [ ] Hunt analyzer
  - [ ] Calculate profit from monster hunts
  - [ ] Loot statistics
- [ ] Quest tracker
  - [ ] Mark quests as completed
  - [ ] Step-by-step walkthrough
- [ ] Export/import data functionality

## Technical Improvements (Ongoing)

- [ ] Performance optimization
  - [ ] Cache frequently accessed data
  - [ ] Lazy loading for large datasets
  - [ ] Image optimization
- [ ] Expanded test coverage
  - [ ] Integration tests
  - [ ] UI tests
  - [ ] Load testing
- [ ] CI/CD pipeline
  - [ ] Automated testing on commit
  - [ ] Automated deployment
- [ ] Docker containerization
- [ ] Enhanced error handling and user feedback
- [ ] Accessibility improvements (WCAG compliance)
- [ ] SEO optimization

## Content Expansion (Ongoing)

- [ ] Complete weapon database
- [ ] Complete equipment database
- [ ] Complete spell database
- [ ] Complete monster database
- [ ] Complete quest database
- [ ] NPC database
- [ ] Item database (general items, not just equipment)
- [ ] Rune information
- [ ] Potion information
- [ ] City guides
- [ ] Training areas guide

## Ideas for Future Consideration

- [ ] Mobile app (React Native or Flutter)
- [ ] Discord bot integration
- [ ] Wiki-style article system for guides and tips
- [ ] Video tutorial embedding
- [ ] Screenshot gallery
- [ ] Server event calendar
- [ ] Trade market (if applicable to server)
- [ ] Guild system integration
- [ ] Achievement system
