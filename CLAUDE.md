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


## Development Environment

### Essential Commands

**Python Environment:** Use the nbs-msba conda environment for all Python operations:
```bash
"/mnt/c/Users/User/anaconda3/envs/nbs-msba/python.exe" <script>.py
```

**Streamlit Applications:**
```bash
"/mnt/c/Users/User/anaconda3/envs/nbs-msba/Scripts/streamlit.exe" run <app>.py
```