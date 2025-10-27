# 1:1 Meeting Insights Dashboard - Technical Report

**Author:** Timothy
**Date:** October 27, 2025
**Project:** ComChord Data Internship Technical Test

---

## Overview

This project delivers an interactive dashboard designed for Sarah Chen, a Senior Director of Product, to visualize insights from her 1:1 meetings with direct reports Alex Rodriguez (Product Manager) and Javier Morales (QA Lead). The dashboard transforms qualitative conversation data into actionable metrics that help Sarah track team health, identify blockers, and make informed coaching decisions.

After analyzing seven 1:1 conversation transcripts, I identified key patterns: Alex shows strong growth potential but struggles with prioritization and stakeholder management, while Javier demonstrates deep technical expertise but faces challenges with timeline commitments and outcome-focused communication. The dashboard surfaces these insights through targeted visualizations that support Sarah's differentiated management approach for each direct report.

**Technical Stack:** Python, Pandas, Plotly, Streamlit

---

## Dashboard Design Choices

### Target User Needs

Sarah's primary needs as a manager include:
- **Monitoring team morale** - Is sentiment improving or declining?
- **Tracking accountability** - Are action items being completed?
- **Identifying blockers** - What's preventing progress?
- **Assessing growth** - Are individuals developing in their target areas?
- **Making comparisons** - How do her two direct reports differ in engagement and communication style?

The dashboard was designed with these questions at the forefront, prioritizing manager-level insights over granular details.

### Visualization Rationale

**1. Sentiment Trend Line**
*Why:* Line charts effectively show trends over time. Sarah can quickly see if recent meetings have been more positive (Alex's improving trajectory) or show friction (Javier's lower scores).
*Design Choice:* Color-coded by direct report with a neutral baseline reference line for context.

**2. OKR Progress Charts (Actual vs. Target)**
*Why:* Dual-line charts clearly show performance gaps. For Alex's metrics (User Engagement at 14.8% vs. 15% target), Sarah can see he's nearly on track. For Javier's flaky test count (78 vs. 50 target), the gap signals ongoing challenges.
*Design Choice:* Actual values in solid blue, targets in dashed red for instant visual comparison.

**3. Communication Pattern Metrics**
*Why:* Hedge words count reveals confidence levels. Javier's high hedge word usage (28-35 per meeting) compared to Alex's (4-8) indicates hesitancy and aligns with observed communication friction.
*Design Choice:* Line chart with annotation explaining "Lower = More Confident" to guide interpretation.

**4. Action Item Status (Pie Chart)**
*Why:* Pie charts excel at showing composition. Sarah can instantly see that 56% of actions are completed, with clear visual distinction between Completed (green), In Progress (yellow), and Pending (red).
*Design Choice:* Status-based color coding with recent action list below for drill-down context.

**5. Blocker Tracking (Bar Chart + List)**
*Why:* Combines quantitative overview (Active vs. Resolved counts) with qualitative details (specific blocker descriptions). Critical for Sarah to prioritize where to intervene.
*Design Choice:* Severity indicators (red/yellow/green dots) help Sarah triage which blockers need immediate attention.

**6. Topic Frequency (Horizontal Bar Chart)**
*Why:* Quickly reveals what dominates meeting time. "Test Automation" appearing most frequently for Javier signals an ongoing struggle, while Alex's varied topics show broader project scope.
*Design Choice:* Horizontal orientation with color gradient makes it easy to scan priorities.

### Information Hierarchy

The dashboard follows a top-down priority structure:
1. **Executive metrics** (top row) - 4 KPIs for at-a-glance health check
2. **Trends** (row 2) - Sentiment and communication patterns over time
3. **Performance** (row 3) - OKR tracking with tabs for each direct report
4. **Tactical details** (rows 4-5) - Topics, actions, blockers, and growth areas
5. **AI-generated insights** (footer) - Automated strengths and concerns summary

**Interactive Filters:** Sidebar allows Sarah to filter by date range or focus on individual direct reports, enabling both high-level team view and deep-dive individual analysis.

---

## Difficulties Encountered

### 1. Qualitative to Quantitative Conversion

The primary challenge was extracting measurable metrics from natural conversation data. Unlike structured data sources, the transcripts required interpretation:
- **Sentiment scores** - Conversations contain nuance. Alex saying "I'm a little nervous but really excited" about Q4 planning mixes anxiety with enthusiasm. I designed a 0-1 sentiment scale where context determines scoring.
- **Action item extraction** - Identifying commitments required parsing phrases like "I'll work on that" vs. "I should probably..." (lower commitment level).
- **Progress tracking** - Quantifying subjective statements like Javier's "we're making steady, incremental progress" on automation required mapping to measurable coverage percentages.

### 2. Time Constraints and Prototyping Strategy

Given the 4-hour constraint, I adopted a **synthetic data approach** for rapid prototyping:
- First, I thoroughly analyzed the conversation transcripts to understand themes, metrics, and patterns
- Then, I designed a data schema capturing 7 key dimensions (meetings, topics, actions, metrics, blockers, growth, communication)
- Generated synthetic CSV files reflecting realistic values based on actual conversation content
- Built the dashboard against this clean structure

**Trade-off:** While this enabled fast iteration on visualizations, the dashboard currently uses synthetic data rather than parsed transcripts. This demonstrates the data model and visualization strategy but requires a parser implementation for production use.

### 3. Balancing Comprehensiveness vs. Clarity

Initially, I considered 15+ potential visualizations, but quickly realized this would overwhelm Sarah. Key decisions:
- **Excluded:** Word clouds (too vague), network graphs (over-complex for 2 people), detailed conversation replays (too granular)
- **Included:** Metrics directly tied to Sarah's decision-making needs
- **Result:** 8 core visualization types that tell a complete story without cognitive overload

---

## Future Explorations

### Near-Term Enhancements (Within Original Scope)

**1. Parse Real Transcripts**
Implement NLP pipeline to automatically extract the 7 data dimensions from `.txt` files:
- Date/participant parsing from headers
- Sentiment analysis using keyword dictionaries or transformer models (e.g., VADER, DistilBERT)
- Action item detection via pattern matching ("I'll...", "you should...", "let's...")
- Topic modeling using TF-IDF or LDA clustering

**2. Advanced Metrics**
- **Question ratio analysis** - Manager questions vs. direct report questions as coaching indicator
- **Topic evolution tracking** - Show how specific issues (e.g., "automation timeline") progress across meetings
- **Meeting preparation assistant** - "Based on patterns, suggest discussing X with Javier next week"

**3. Bonus: Team Conversation Integration**
Analyze the Code Review Workshop transcripts to compare:
- Individual behavior in 1:1s vs. team settings
- Whether 1:1 concerns surface in team discussions
- Multi-speaker dynamics and contribution patterns

### Medium-Term Features (Beyond Test Scope)

**1. Predictive Analytics**
- Promotion readiness scoring based on growth trajectory
- Project risk prediction using blocker persistence and sentiment trends
- Attrition risk flagging from declining engagement patterns

**2. Comparative Benchmarking**
- Compare Sarah's direct reports to anonymized peer data
- Industry benchmark integration for OKR performance

**3. Export and Sharing**
- PDF report generation for sharing with leadership
- Email summary automation
- Calendar integration for meeting prep reminders

### Long-Term Vision (Production System)

**1. LLM-Powered Capabilities**
- Conversational Q&A: "How is Alex doing on stakeholder management?"
- Auto-generated meeting summaries
- Coaching recommendation engine

**2. Multi-Manager Platform**
- Scale beyond Sarah to support entire organization
- Privacy-preserving aggregate analytics for senior leadership
- Best practice sharing across managers

**3. Real-Time Integration**
- Live transcript processing during video calls
- Slack/Teams bot for action item tracking
- Automated follow-up reminders

---

## Conclusion

This dashboard demonstrates that rich managerial insights can be systematically extracted from unstructured 1:1 conversations. By focusing on Sarah's specific needs—tracking morale, accountability, blockers, and individual growth—the design prioritizes actionable intelligence over comprehensive data dumps.

The synthetic data approach enabled rapid prototyping within time constraints while establishing a clear data model for future transcript parsing. Key learnings include the importance of user-centric visualization choices, the challenge of quantifying qualitative interactions, and the value of iterative design in dashboard development.

**Next immediate step:** Implement the transcript parser to replace synthetic data with real conversation analysis, unlocking the full potential of this analytical framework.
