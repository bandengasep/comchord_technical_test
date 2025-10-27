"""
Generate synthetic dataset for 1:1 conversation dashboard POC
Based on insights from Sarah's meetings with Alex and Javier
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

# Set random seed for reproducibility
np.random.seed(42)

# Date range for meetings (Sept - Oct 2025)
start_date = datetime(2025, 9, 1)
end_date = datetime(2025, 10, 15)

# ===== 1. MEETING METADATA =====
meetings = [
    # Alex's meetings
    {"date": "2025-09-14", "direct_report": "Alex Rodriguez", "role": "Product Manager", "duration_mins": 60, "sentiment_score": 0.65},
    {"date": "2025-09-21", "direct_report": "Alex Rodriguez", "role": "Product Manager", "duration_mins": 55, "sentiment_score": 0.55},
    {"date": "2025-09-28", "direct_report": "Alex Rodriguez", "role": "Product Manager", "duration_mins": 60, "sentiment_score": 0.70},
    {"date": "2025-10-06", "direct_report": "Alex Rodriguez", "role": "Product Manager", "duration_mins": 65, "sentiment_score": 0.75},
    # Javier's meetings
    {"date": "2025-09-07", "direct_report": "Javier Morales", "role": "QA Lead", "duration_mins": 55, "sentiment_score": 0.40},
    {"date": "2025-09-22", "direct_report": "Javier Morales", "role": "QA Lead", "duration_mins": 60, "sentiment_score": 0.35},
    {"date": "2025-10-07", "direct_report": "Javier Morales", "role": "QA Lead", "duration_mins": 58, "sentiment_score": 0.45},
]

# ===== 2. TOPICS DISCUSSED =====
topics = [
    # Alex's topics
    {"meeting_date": "2025-09-14", "direct_report": "Alex Rodriguez", "topic": "Mobile Redesign", "time_spent_mins": 15, "priority": "High"},
    {"meeting_date": "2025-09-14", "direct_report": "Alex Rodriguez", "topic": "Feature Prioritization", "time_spent_mins": 12, "priority": "High"},
    {"meeting_date": "2025-09-14", "direct_report": "Alex Rodriguez", "topic": "OKR Progress", "time_spent_mins": 10, "priority": "Medium"},
    {"meeting_date": "2025-09-14", "direct_report": "Alex Rodriguez", "topic": "API Integration", "time_spent_mins": 8, "priority": "Medium"},
    {"meeting_date": "2025-09-14", "direct_report": "Alex Rodriguez", "topic": "Career Development", "time_spent_mins": 15, "priority": "Medium"},

    {"meeting_date": "2025-09-21", "direct_report": "Alex Rodriguez", "topic": "Mobile Redesign", "time_spent_mins": 20, "priority": "High"},
    {"meeting_date": "2025-09-21", "direct_report": "Alex Rodriguez", "topic": "Search Feature Adoption", "time_spent_mins": 15, "priority": "High"},
    {"meeting_date": "2025-09-21", "direct_report": "Alex Rodriguez", "topic": "Stakeholder Management", "time_spent_mins": 10, "priority": "Medium"},

    {"meeting_date": "2025-09-28", "direct_report": "Alex Rodriguez", "topic": "OKR Progress", "time_spent_mins": 18, "priority": "High"},
    {"meeting_date": "2025-09-28", "direct_report": "Alex Rodriguez", "topic": "Q4 Planning", "time_spent_mins": 15, "priority": "High"},
    {"meeting_date": "2025-09-28", "direct_report": "Alex Rodriguez", "topic": "Mobile Redesign", "time_spent_mins": 12, "priority": "Medium"},

    {"meeting_date": "2025-10-06", "direct_report": "Alex Rodriguez", "topic": "Q4 Planning", "time_spent_mins": 25, "priority": "High"},
    {"meeting_date": "2025-10-06", "direct_report": "Alex Rodriguez", "topic": "Performance Issues", "time_spent_mins": 15, "priority": "Medium"},

    # Javier's topics
    {"meeting_date": "2025-09-07", "direct_report": "Javier Morales", "topic": "Test Automation", "time_spent_mins": 20, "priority": "High"},
    {"meeting_date": "2025-09-07", "direct_report": "Javier Morales", "topic": "Quality Metrics", "time_spent_mins": 10, "priority": "Medium"},
    {"meeting_date": "2025-09-07", "direct_report": "Javier Morales", "topic": "Bug Analysis", "time_spent_mins": 12, "priority": "High"},
    {"meeting_date": "2025-09-07", "direct_report": "Javier Morales", "topic": "Hiring", "time_spent_mins": 8, "priority": "Medium"},
    {"meeting_date": "2025-09-07", "direct_report": "Javier Morales", "topic": "Career Development", "time_spent_mins": 5, "priority": "Low"},

    {"meeting_date": "2025-09-22", "direct_report": "Javier Morales", "topic": "Test Automation", "time_spent_mins": 25, "priority": "High"},
    {"meeting_date": "2025-09-22", "direct_report": "Javier Morales", "topic": "Flaky Tests", "time_spent_mins": 15, "priority": "High"},
    {"meeting_date": "2025-09-22", "direct_report": "Javier Morales", "topic": "Quality Metrics", "time_spent_mins": 8, "priority": "Low"},

    {"meeting_date": "2025-10-07", "direct_report": "Javier Morales", "topic": "Test Automation", "time_spent_mins": 22, "priority": "High"},
    {"meeting_date": "2025-10-07", "direct_report": "Javier Morales", "topic": "Hiring", "time_spent_mins": 12, "priority": "Medium"},
    {"meeting_date": "2025-10-07", "direct_report": "Javier Morales", "topic": "Tooling Evaluation", "time_spent_mins": 10, "priority": "Medium"},
]

# ===== 3. ACTION ITEMS =====
action_items = [
    # Alex's action items
    {"created_date": "2025-09-14", "direct_report": "Alex Rodriguez", "action": "Create prioritization scoring model", "owner": "Alex", "status": "Completed", "completed_date": "2025-09-20"},
    {"created_date": "2025-09-14", "direct_report": "Alex Rodriguez", "action": "Follow up with API vendor", "owner": "Alex", "status": "Completed", "completed_date": "2025-09-15"},
    {"created_date": "2025-09-14", "direct_report": "Alex Rodriguez", "action": "Launch in-app messaging for search", "owner": "Alex", "status": "Completed", "completed_date": "2025-09-18"},
    {"created_date": "2025-09-14", "direct_report": "Alex Rodriguez", "action": "Read 'Crucial Conversations' book", "owner": "Alex", "status": "In Progress", "completed_date": None},
    {"created_date": "2025-09-14", "direct_report": "Alex Rodriguez", "action": "Get data science team support", "owner": "Sarah", "status": "Completed", "completed_date": "2025-09-16"},

    {"created_date": "2025-09-21", "direct_report": "Alex Rodriguez", "action": "Design UI mockups for search filters", "owner": "Alex", "status": "Completed", "completed_date": "2025-09-27"},
    {"created_date": "2025-09-21", "direct_report": "Alex Rodriguez", "action": "A/B test search feature variations", "owner": "Alex", "status": "In Progress", "completed_date": None},

    {"created_date": "2025-09-28", "direct_report": "Alex Rodriguez", "action": "Draft Q4 OKRs", "owner": "Alex", "status": "In Progress", "completed_date": None},
    {"created_date": "2025-09-28", "direct_report": "Alex Rodriguez", "action": "Present Q4 plan to leadership", "owner": "Alex", "status": "Pending", "completed_date": None},

    {"created_date": "2025-10-06", "direct_report": "Alex Rodriguez", "action": "Finalize Q4 presentation deck", "owner": "Alex", "status": "Pending", "completed_date": None},

    # Javier's action items
    {"created_date": "2025-09-07", "direct_report": "Javier Morales", "action": "Send automation roadmap Confluence link", "owner": "Javier", "status": "Completed", "completed_date": "2025-09-08"},
    {"created_date": "2025-09-07", "direct_report": "Javier Morales", "action": "Send certification proposal", "owner": "Javier", "status": "Pending", "completed_date": None},
    {"created_date": "2025-09-07", "direct_report": "Javier Morales", "action": "Add checkout bug to regression suite", "owner": "Javier", "status": "Completed", "completed_date": "2025-09-10"},
    {"created_date": "2025-09-07", "direct_report": "Javier Morales", "action": "Complete final interviews for QA hire", "owner": "Javier", "status": "Completed", "completed_date": "2025-09-12"},

    {"created_date": "2025-09-22", "direct_report": "Javier Morales", "action": "Reduce flaky test count by 30%", "owner": "Javier", "status": "In Progress", "completed_date": None},
    {"created_date": "2025-09-22", "direct_report": "Javier Morales", "action": "Evaluate Playwright vs Cypress", "owner": "Javier", "status": "In Progress", "completed_date": None},

    {"created_date": "2025-10-07", "direct_report": "Javier Morales", "action": "Finalize QA hire offer", "owner": "Javier", "status": "Pending", "completed_date": None},
    {"created_date": "2025-10-07", "direct_report": "Javier Morales", "action": "Document shift-left testing strategy", "owner": "Javier", "status": "Pending", "completed_date": None},
]

# ===== 4. OKRS / METRICS =====
metrics = [
    # Alex's metrics
    {"date": "2025-09-14", "direct_report": "Alex Rodriguez", "metric": "User Engagement Increase", "target": 15.0, "actual": 10.0, "unit": "%"},
    {"date": "2025-09-21", "direct_report": "Alex Rodriguez", "metric": "User Engagement Increase", "target": 15.0, "actual": 12.0, "unit": "%"},
    {"date": "2025-09-28", "direct_report": "Alex Rodriguez", "metric": "User Engagement Increase", "target": 15.0, "actual": 13.5, "unit": "%"},
    {"date": "2025-10-06", "direct_report": "Alex Rodriguez", "metric": "User Engagement Increase", "target": 15.0, "actual": 14.8, "unit": "%"},

    {"date": "2025-09-14", "direct_report": "Alex Rodriguez", "metric": "Search Feature Adoption", "target": 25.0, "actual": 15.0, "unit": "%"},
    {"date": "2025-09-21", "direct_report": "Alex Rodriguez", "metric": "Search Feature Adoption", "target": 25.0, "actual": 18.0, "unit": "%"},
    {"date": "2025-09-28", "direct_report": "Alex Rodriguez", "metric": "Search Feature Adoption", "target": 25.0, "actual": 21.0, "unit": "%"},
    {"date": "2025-10-06", "direct_report": "Alex Rodriguez", "metric": "Search Feature Adoption", "target": 25.0, "actual": 23.5, "unit": "%"},

    {"date": "2025-09-14", "direct_report": "Alex Rodriguez", "metric": "Customer Satisfaction", "target": 90.0, "actual": 92.0, "unit": "%"},
    {"date": "2025-09-21", "direct_report": "Alex Rodriguez", "metric": "Customer Satisfaction", "target": 90.0, "actual": 93.0, "unit": "%"},
    {"date": "2025-09-28", "direct_report": "Alex Rodriguez", "metric": "Customer Satisfaction", "target": 90.0, "actual": 92.5, "unit": "%"},
    {"date": "2025-10-06", "direct_report": "Alex Rodriguez", "metric": "Customer Satisfaction", "target": 90.0, "actual": 94.0, "unit": "%"},

    # Javier's metrics
    {"date": "2025-09-07", "direct_report": "Javier Morales", "metric": "Code Coverage", "target": 85.0, "actual": 78.0, "unit": "%"},
    {"date": "2025-09-22", "direct_report": "Javier Morales", "metric": "Code Coverage", "target": 85.0, "actual": 79.0, "unit": "%"},
    {"date": "2025-10-07", "direct_report": "Javier Morales", "metric": "Code Coverage", "target": 85.0, "actual": 80.5, "unit": "%"},

    {"date": "2025-09-07", "direct_report": "Javier Morales", "metric": "P0 User Flow Coverage", "target": 95.0, "actual": 95.0, "unit": "%"},
    {"date": "2025-09-22", "direct_report": "Javier Morales", "metric": "P0 User Flow Coverage", "target": 95.0, "actual": 96.0, "unit": "%"},
    {"date": "2025-10-07", "direct_report": "Javier Morales", "metric": "P0 User Flow Coverage", "target": 95.0, "actual": 97.0, "unit": "%"},

    {"date": "2025-09-07", "direct_report": "Javier Morales", "metric": "Flaky Test Count", "target": 50.0, "actual": 120.0, "unit": "tests"},
    {"date": "2025-09-22", "direct_report": "Javier Morales", "metric": "Flaky Test Count", "target": 50.0, "actual": 95.0, "unit": "tests"},
    {"date": "2025-10-07", "direct_report": "Javier Morales", "metric": "Flaky Test Count", "target": 50.0, "actual": 78.0, "unit": "tests"},

    {"date": "2025-09-07", "direct_report": "Javier Morales", "metric": "API Test Suite Size", "target": 200.0, "actual": 150.0, "unit": "tests"},
    {"date": "2025-09-22", "direct_report": "Javier Morales", "metric": "API Test Suite Size", "target": 200.0, "actual": 185.0, "unit": "tests"},
    {"date": "2025-10-07", "direct_report": "Javier Morales", "metric": "API Test Suite Size", "target": 200.0, "actual": 210.0, "unit": "tests"},
]

# ===== 5. BLOCKERS / CHALLENGES =====
blockers = [
    # Alex's blockers
    {"first_mentioned": "2025-09-14", "direct_report": "Alex Rodriguez", "blocker": "Feature request overload", "severity": "Medium", "status": "Resolved", "resolved_date": "2025-09-20"},
    {"first_mentioned": "2025-09-14", "direct_report": "Alex Rodriguez", "blocker": "API vendor unresponsive", "severity": "High", "status": "Resolved", "resolved_date": "2025-09-16"},
    {"first_mentioned": "2025-09-14", "direct_report": "Alex Rodriguez", "blocker": "Data science team capacity", "severity": "High", "status": "Resolved", "resolved_date": "2025-09-17"},
    {"first_mentioned": "2025-09-21", "direct_report": "Alex Rodriguez", "blocker": "Search feature plateau", "severity": "High", "status": "Active", "resolved_date": None},
    {"first_mentioned": "2025-10-06", "direct_report": "Alex Rodriguez", "blocker": "Android performance issues", "severity": "Medium", "status": "Active", "resolved_date": None},

    # Javier's blockers
    {"first_mentioned": "2025-09-07", "direct_report": "Javier Morales", "blocker": "Automation timeline unclear", "severity": "High", "status": "Active", "resolved_date": None},
    {"first_mentioned": "2025-09-07", "direct_report": "Javier Morales", "blocker": "Frontend technical debt", "severity": "High", "status": "Active", "resolved_date": None},
    {"first_mentioned": "2025-09-07", "direct_report": "Javier Morales", "blocker": "Checkout bug edge case", "severity": "High", "status": "Resolved", "resolved_date": "2025-09-10"},
    {"first_mentioned": "2025-09-22", "direct_report": "Javier Morales", "blocker": "Flaky tests undermining CI/CD", "severity": "High", "status": "Active", "resolved_date": None},
    {"first_mentioned": "2025-09-22", "direct_report": "Javier Morales", "blocker": "Tooling evaluation paralysis", "severity": "Medium", "status": "Active", "resolved_date": None},
]

# ===== 6. GROWTH AREAS =====
growth_areas = [
    # Alex's growth
    {"direct_report": "Alex Rodriguez", "area": "Strategic Thinking", "progress_level": 2, "activities": "Q4 planning ownership, competitive analysis"},
    {"direct_report": "Alex Rodriguez", "area": "Stakeholder Management", "progress_level": 3, "activities": "Prioritization framework, 'Crucial Conversations' book"},
    {"direct_report": "Alex Rodriguez", "area": "Saying No", "progress_level": 2, "activities": "Coaching from Sarah, scoring model"},
    {"direct_report": "Alex Rodriguez", "area": "Executive Communication", "progress_level": 1, "activities": "Q4 leadership presentation upcoming"},

    # Javier's growth
    {"direct_report": "Javier Morales", "area": "Cloud Security Certification", "progress_level": 1, "activities": "Researching programs"},
    {"direct_report": "Javier Morales", "area": "Performance Engineering", "progress_level": 1, "activities": "K6 evaluation, load testing"},
    {"direct_report": "Javier Morales", "area": "Outcome-focused Communication", "progress_level": 1, "activities": "Sarah coaching on metrics"},
]

# ===== 7. COMMUNICATION PATTERNS =====
communication = [
    {"meeting_date": "2025-09-14", "direct_report": "Alex Rodriguez", "manager_questions": 12, "dr_questions": 5, "dr_hedge_words": 8, "dr_avg_response_length": 45},
    {"meeting_date": "2025-09-21", "direct_report": "Alex Rodriguez", "manager_questions": 10, "dr_questions": 4, "dr_hedge_words": 6, "dr_avg_response_length": 42},
    {"meeting_date": "2025-09-28", "direct_report": "Alex Rodriguez", "manager_questions": 9, "dr_questions": 6, "dr_hedge_words": 5, "dr_avg_response_length": 48},
    {"meeting_date": "2025-10-06", "direct_report": "Alex Rodriguez", "manager_questions": 8, "dr_questions": 7, "dr_hedge_words": 4, "dr_avg_response_length": 50},

    {"meeting_date": "2025-09-07", "direct_report": "Javier Morales", "manager_questions": 15, "dr_questions": 2, "dr_hedge_words": 35, "dr_avg_response_length": 65},
    {"meeting_date": "2025-09-22", "direct_report": "Javier Morales", "manager_questions": 14, "dr_questions": 1, "dr_hedge_words": 32, "dr_avg_response_length": 62},
    {"meeting_date": "2025-10-07", "direct_report": "Javier Morales", "manager_questions": 13, "dr_questions": 3, "dr_hedge_words": 28, "dr_avg_response_length": 58},
]

# Convert to DataFrames and save as CSV
df_meetings = pd.DataFrame(meetings)
df_topics = pd.DataFrame(topics)
df_action_items = pd.DataFrame(action_items)
df_metrics = pd.DataFrame(metrics)
df_blockers = pd.DataFrame(blockers)
df_growth_areas = pd.DataFrame(growth_areas)
df_communication = pd.DataFrame(communication)

# Save to CSV
df_meetings.to_csv('data_meetings.csv', index=False)
df_topics.to_csv('data_topics.csv', index=False)
df_action_items.to_csv('data_action_items.csv', index=False)
df_metrics.to_csv('data_metrics.csv', index=False)
df_blockers.to_csv('data_blockers.csv', index=False)
df_growth_areas.to_csv('data_growth_areas.csv', index=False)
df_communication.to_csv('data_communication.csv', index=False)

print("[SUCCESS] Synthetic dataset generated successfully!")
print("\nDatasets created:")
print(f"  - data_meetings.csv ({len(df_meetings)} rows)")
print(f"  - data_topics.csv ({len(df_topics)} rows)")
print(f"  - data_action_items.csv ({len(df_action_items)} rows)")
print(f"  - data_metrics.csv ({len(df_metrics)} rows)")
print(f"  - data_blockers.csv ({len(df_blockers)} rows)")
print(f"  - data_growth_areas.csv ({len(df_growth_areas)} rows)")
print(f"  - data_communication.csv ({len(df_communication)} rows)")
