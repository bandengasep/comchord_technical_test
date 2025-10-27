# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains data for a ComChord Data Internship technical test. The project involves analyzing conversational data from 1:1 meetings between a manager (Sarah Chen) and her direct reports to create a data dashboard and insights.

**Time Constraint**: The main task should take a maximum of 4 hours of focused time.

## Data Structure

### Primary Data: 1-to-1 Conversations
Located in `1-to-1 convos/` directory:
- **Alex Rodriguez (Product Manager)**: 4 conversation transcripts dated Sept 14, 21, 28, and Oct 6, 2025
- **Javier Morales (QA Lead)**: 3 conversation transcripts dated Sept 7, 22, and Oct 7, 2025

Each transcript follows this structure:
- Participants and roles
- Date/time/format metadata
- Full conversational transcript in dialogue format
- Covers topics including: project updates, OKRs, blockers, career development, team dynamics

### Bonus Data: Team Conversations
Located in `bonus materials/` directory:
- Team workshop transcripts from "Code Review Weekly Workshop" sessions
- Dated Sept 9, 16, 23, 2022
- Multi-speaker format with timestamps and speaker IDs
- Topics include: dependency updates, code review practices, maintainer responsibilities

## Project Objectives

1. **Primary Goal**: Create a data dashboard designed for Sarah (the manager) to visualize insights from the 1:1 conversations with her direct reports
2. **Secondary Output**: Produce a short report explaining:
   - Dashboard design choices
   - Difficulties encountered
   - Future areas of exploration beyond the time constraint
3. **Bonus**: Consider how the dashboard might change when incorporating team conversation data

## Key Analysis Areas

Based on the conversation content, relevant features to extract and visualize include:

### For Alex (Product Manager):
- Project status and progress tracking (mobile redesign, API integrations)
- OKR performance metrics (user engagement, search adoption, customer satisfaction)
- Blockers and challenges (prioritization struggles, vendor responsiveness, resource constraints)
- Growth areas (strategic thinking, stakeholder management, competitive intelligence)
- Manager actions/support (Q4 planning opportunity, data science team support)

### For Javier (QA Lead):
- Quality metrics (bug escape rate, test coverage, test pass rate)
- Automation progress (shift-left strategy, flaky test remediation, API vs UI testing)
- Technical challenges (tooling evaluation, technical debt, multi-version compatibility)
- Hiring status and team capacity
- Career development focus (technical certifications vs management track)

### Cross-cutting Themes:
- Communication styles (Alex: collaborative and uncertain; Javier: methodical and technical)
- Manager coaching approaches with each direct report
- Action items and follow-ups from each meeting
- Sentiment and engagement levels over time

## Development Approach

When building the dashboard solution:

1. **Text Processing**: Parse transcript files to extract structured data (dates, speakers, topics, sentiment, action items)
2. **Feature Engineering**: Identify quantifiable metrics from qualitative conversation data
3. **Visualization Selection**: Choose appropriate chart types for manager-level insights (trend lines, status indicators, progress trackers)
4. **User-Centric Design**: Focus on Sarah's needs as a manager making decisions about team support and resource allocation

## Technical Considerations

- Transcript formats vary between 1:1 conversations (clean dialogue) and team conversations (timestamped with speaker IDs)
- Text files use UTF-8 encoding (some with BOM markers)
- Dates use various formats (e.g., "September 14, 2025" vs "Sep 09, 2022")
- No existing code or package structure - this is a greenfield project
- Generative AI is explicitly encouraged for expediting the development process


## Current Implementation Status

### Completed Deliverables

**✅ Interactive Dashboard** (`dashboard.py`)
- Streamlit-based web application
- 8 key visualization types: sentiment trends, OKR progress, communication patterns, action items, blockers, topics, and growth areas
- Interactive filters for date range and direct report selection
- AI-generated insights with automatic strengths/concerns detection
- Deployed locally at http://localhost:8501

**✅ Synthetic Data Generator** (`generate_synthetic_data.py`)
- Creates 7 CSV files with realistic data based on actual conversation analysis
- Dimensions: meetings, topics, action items, metrics, blockers, growth areas, communication patterns
- Run with: `"/mnt/c/Users/User/anaconda3/envs/nbs-msba/python.exe" generate_synthetic_data.py`

**✅ Generated Datasets** (7 CSV files)
- `data_meetings.csv` - Meeting metadata (date, duration, sentiment)
- `data_topics.csv` - Discussion topics with priority levels
- `data_action_items.csv` - Action items with owner and status tracking
- `data_metrics.csv` - OKR/metric progress with actual vs. target values
- `data_blockers.csv` - Challenges with severity and resolution status
- `data_growth_areas.csv` - Individual development focus areas
- `data_communication.csv` - Communication pattern metrics (questions, hedge words, response lengths)

**✅ Technical Report** (`TECHNICAL_REPORT.md`)
- 2-page documentation of dashboard design choices
- Explains visualization rationale, difficulties encountered, and future explorations
- Includes specific examples from conversation analysis

**✅ Project Documentation**
- `README.md` - GitHub-ready project overview with installation instructions
- `requirements.txt` - Python dependencies for deployment
- `CLAUDE.md` - This file, providing project context

### Implementation Approach

**Strategy: Synthetic Data POC**
Rather than immediately parsing transcripts, the project uses a two-phase approach:
1. **Phase 1 (Completed)**: Analyze conversations → design data schema → generate synthetic data → build dashboard
2. **Phase 2 (Future)**: Build transcript parser → extract real data → replace synthetic CSVs

**Rationale**: This approach enables rapid prototyping of visualizations within the 4-hour constraint while establishing a clear data model for future implementation.

### Key Insights from Conversation Analysis

**Alex Rodriguez (Product Manager):**
- High growth potential, shows improving sentiment trajectory
- Struggles: Prioritization, saying "no" to stakeholders, vendor assertiveness
- Strengths: Data-driven, user-focused, responsive to coaching
- OKRs: User engagement (14.8% vs 15% target), Search adoption (23.5% vs 25%), Customer satisfaction (94% vs 90% ✓)

**Javier Morales (QA Lead):**
- Deep technical expertise, methodical approach
- Challenges: Timeline commitments, outcome-focused communication, high hedge word usage (28-35 per meeting)
- Strengths: Quality metrics, API test coverage increasing (210 vs 200 target ✓)
- Key blocker: Test automation project lacks clear timeline after ~1 year

**Sarah's Management Style:**
- Differentiated approach: Coaching with Alex, directive with Javier
- Tracks action item follow-through (56% completion rate)
- Focuses on both tactical execution and career development

## Development Environment

### Essential Commands

**Run Dashboard:**
```bash
"/mnt/c/Users/User/anaconda3/envs/nbs-msba/Scripts/streamlit.exe" run dashboard.py
```

**Generate Data:**
```bash
"/mnt/c/Users/User/anaconda3/envs/nbs-msba/python.exe" generate_synthetic_data.py
```

**Install Dependencies:**
```bash
pip install -r requirements.txt
```

### Working with the Dashboard

The dashboard code is organized into sections:
1. **Data Loading** (lines 20-30) - Cached CSV loading and date parsing
2. **Filters** (lines 35-65) - Sidebar controls for date range and direct report
3. **Metrics Row** (lines 75-95) - Top-level KPIs
4. **Visualizations** (lines 100-390) - Eight core chart sections
5. **Insights** (lines 395-450) - AI-generated strengths and concerns

**Customization Tips:**
- Modify thresholds in the insights section (lines 405-447) to adjust sensitivity
- Add new metrics by extending the synthetic data generator and updating dashboard filters
- Change color schemes in Plotly chart definitions (search for `color_discrete_map`)

### File Dependencies

Dashboard requires all 7 CSV files in the same directory:
```
dashboard.py  →  requires  →  data_meetings.csv
                             data_topics.csv
                             data_action_items.csv
                             data_metrics.csv
                             data_blockers.csv
                             data_growth_areas.csv
                             data_communication.csv
```

## Next Steps for Future Development

### Priority 1: Parse Real Transcripts
Build `parse_transcripts.py` to extract structured data from `.txt` files:
- Parse meeting metadata from headers
- Extract topics, action items, and metrics mentioned in conversations
- Implement sentiment analysis (keyword-based or transformer model)
- Generate the same 7 CSV files from real data

### Priority 2: Enhanced Analytics
- Topic evolution tracking across multiple meetings
- Automatic action item extraction using NLP patterns
- Question ratio analysis (manager vs. direct report)
- Meeting preparation recommendations

### Priority 3: Bonus Materials Integration
- Parse team workshop transcripts
- Compare 1:1 vs. team dynamics
- Add separate dashboard view for team conversations