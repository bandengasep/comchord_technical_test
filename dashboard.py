"""
1:1 Meeting Insights Dashboard for Manager (Sarah Chen)
Visualizes key insights from conversations with direct reports
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="1:1 Insights Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load data
@st.cache_data
def load_data():
    meetings = pd.read_csv('data_meetings.csv')
    topics = pd.read_csv('data_topics.csv')
    action_items = pd.read_csv('data_action_items.csv')
    metrics = pd.read_csv('data_metrics.csv')
    blockers = pd.read_csv('data_blockers.csv')
    growth_areas = pd.read_csv('data_growth_areas.csv')
    communication = pd.read_csv('data_communication.csv')

    # Convert date columns
    meetings['date'] = pd.to_datetime(meetings['date'])
    topics['meeting_date'] = pd.to_datetime(topics['meeting_date'])
    action_items['created_date'] = pd.to_datetime(action_items['created_date'])
    metrics['date'] = pd.to_datetime(metrics['date'])
    communication['meeting_date'] = pd.to_datetime(communication['meeting_date'])

    return meetings, topics, action_items, metrics, blockers, growth_areas, communication

meetings, topics, action_items, metrics, blockers, growth_areas, communication = load_data()

# Sidebar
st.sidebar.title("📊 Dashboard Filters")
st.sidebar.markdown("---")

# Date range filter
min_date = meetings['date'].min()
max_date = meetings['date'].max()
date_range = st.sidebar.date_input(
    "Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Direct report filter
all_reports = ["All"] + sorted(meetings['direct_report'].unique().tolist())
selected_report = st.sidebar.selectbox("Direct Report", all_reports)

# Filter data based on selections
if selected_report != "All":
    meetings_filtered = meetings[meetings['direct_report'] == selected_report]
    topics_filtered = topics[topics['direct_report'] == selected_report]
    action_items_filtered = action_items[action_items['direct_report'] == selected_report]
    metrics_filtered = metrics[metrics['direct_report'] == selected_report]
    blockers_filtered = blockers[blockers['direct_report'] == selected_report]
    growth_filtered = growth_areas[growth_areas['direct_report'] == selected_report]
    communication_filtered = communication[communication['direct_report'] == selected_report]
else:
    meetings_filtered = meetings
    topics_filtered = topics
    action_items_filtered = action_items
    metrics_filtered = metrics
    blockers_filtered = blockers
    growth_filtered = growth_areas
    communication_filtered = communication

# Apply date filter
if len(date_range) == 2:
    start_date, end_date = date_range
    meetings_filtered = meetings_filtered[
        (meetings_filtered['date'] >= pd.Timestamp(start_date)) &
        (meetings_filtered['date'] <= pd.Timestamp(end_date))
    ]

st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.info(
    "This dashboard provides insights from 1:1 meetings with direct reports. "
    "Use the filters above to focus on specific team members or time periods."
)

# Main dashboard
st.title("🎯 1:1 Meeting Insights Dashboard")
st.markdown("**Manager:** Sarah Chen | **Last Updated:** " + datetime.now().strftime("%B %d, %Y"))
st.markdown("---")

# === ROW 1: KEY METRICS ===
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_meetings = len(meetings_filtered)
    st.metric("Total Meetings", total_meetings)

with col2:
    total_actions = len(action_items_filtered)
    completed_actions = len(action_items_filtered[action_items_filtered['status'] == 'Completed'])
    completion_rate = (completed_actions / total_actions * 100) if total_actions > 0 else 0
    st.metric("Action Item Completion", f"{completion_rate:.0f}%",
              f"{completed_actions}/{total_actions} completed")

with col3:
    active_blockers = len(blockers_filtered[blockers_filtered['status'] == 'Active'])
    st.metric("Active Blockers", active_blockers,
              delta=-1 if active_blockers < 3 else 1,
              delta_color="inverse")

with col4:
    avg_sentiment = meetings_filtered['sentiment_score'].mean()
    st.metric("Avg. Meeting Sentiment", f"{avg_sentiment:.2f}",
              delta=f"{(avg_sentiment - 0.5):.2f}",
              delta_color="normal")

st.markdown("---")

# === ROW 2: SENTIMENT & ENGAGEMENT ===
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Meeting Sentiment Trend")
    fig_sentiment = px.line(
        meetings_filtered.sort_values('date'),
        x='date',
        y='sentiment_score',
        color='direct_report',
        markers=True,
        title="Sentiment Score Over Time (0=Negative, 1=Positive)"
    )
    fig_sentiment.add_hline(y=0.5, line_dash="dash", line_color="gray",
                            annotation_text="Neutral")
    fig_sentiment.update_layout(height=350)
    st.plotly_chart(fig_sentiment, use_container_width=True)

with col2:
    st.subheader("💬 Communication Patterns")
    if len(communication_filtered) > 0:
        fig_comm = go.Figure()

        for report in communication_filtered['direct_report'].unique():
            report_data = communication_filtered[communication_filtered['direct_report'] == report].sort_values('meeting_date')
            fig_comm.add_trace(go.Scatter(
                x=report_data['meeting_date'],
                y=report_data['dr_hedge_words'],
                mode='lines+markers',
                name=report,
                hovertemplate='%{y} hedge words<extra></extra>'
            ))

        fig_comm.update_layout(
            title="Hedge Words per Meeting (Lower = More Confident)",
            xaxis_title="Date",
            yaxis_title="Hedge Words Count",
            height=350
        )
        st.plotly_chart(fig_comm, use_container_width=True)
    else:
        st.info("No communication data available for selected filters")

st.markdown("---")

# === ROW 3: OKRS & METRICS ===
st.subheader("🎯 OKR Progress Tracking")

if len(metrics_filtered) > 0:
    unique_metrics = metrics_filtered['metric'].unique()

    # Create tabs for each direct report if "All" is selected
    if selected_report == "All":
        tabs = st.tabs(sorted(metrics_filtered['direct_report'].unique()))

        for i, report in enumerate(sorted(metrics_filtered['direct_report'].unique())):
            with tabs[i]:
                report_metrics = metrics_filtered[metrics_filtered['direct_report'] == report]

                for metric_name in report_metrics['metric'].unique():
                    metric_data = report_metrics[report_metrics['metric'] == metric_name].sort_values('date')

                    fig = go.Figure()
                    fig.add_trace(go.Scatter(
                        x=metric_data['date'],
                        y=metric_data['actual'],
                        mode='lines+markers',
                        name='Actual',
                        line=dict(color='#1f77b4', width=3)
                    ))
                    fig.add_trace(go.Scatter(
                        x=metric_data['date'],
                        y=metric_data['target'],
                        mode='lines',
                        name='Target',
                        line=dict(color='red', dash='dash')
                    ))

                    fig.update_layout(
                        title=f"{metric_name}",
                        xaxis_title="Date",
                        yaxis_title=f"Value ({metric_data.iloc[0]['unit']})",
                        height=300
                    )

                    st.plotly_chart(fig, use_container_width=True)
    else:
        # Show all metrics for selected report
        for metric_name in unique_metrics:
            metric_data = metrics_filtered[metrics_filtered['metric'] == metric_name].sort_values('date')

            col1, col2 = st.columns([3, 1])

            with col1:
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=metric_data['date'],
                    y=metric_data['actual'],
                    mode='lines+markers',
                    name='Actual',
                    line=dict(color='#1f77b4', width=3)
                ))
                fig.add_trace(go.Scatter(
                    x=metric_data['date'],
                    y=metric_data['target'],
                    mode='lines',
                    name='Target',
                    line=dict(color='red', dash='dash')
                ))

                fig.update_layout(
                    title=f"{metric_name}",
                    xaxis_title="Date",
                    yaxis_title=f"Value ({metric_data.iloc[0]['unit']})",
                    height=300
                )

                st.plotly_chart(fig, use_container_width=True)

            with col2:
                latest = metric_data.iloc[-1]
                gap = latest['actual'] - latest['target']
                on_track = "✓ On Track" if gap >= 0 or latest['actual'] / latest['target'] >= 0.9 else "⚠ At Risk"

                st.metric(
                    "Latest",
                    f"{latest['actual']}{latest['unit']}",
                    f"{gap:+.1f} vs target"
                )
                st.markdown(f"**Status:** {on_track}")
else:
    st.info("No metrics data available for selected filters")

st.markdown("---")

# === ROW 4: TOPICS & ACTION ITEMS ===
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Discussion Topics")

    if len(topics_filtered) > 0:
        # Topic frequency
        topic_counts = topics_filtered.groupby('topic').size().reset_index(name='frequency')
        topic_counts = topic_counts.sort_values('frequency', ascending=False)

        fig_topics = px.bar(
            topic_counts,
            x='frequency',
            y='topic',
            orientation='h',
            title="Most Discussed Topics",
            color='frequency',
            color_continuous_scale='blues'
        )
        fig_topics.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_topics, use_container_width=True)

        # Topic priority distribution
        priority_dist = topics_filtered['priority'].value_counts()
        fig_priority = px.pie(
            values=priority_dist.values,
            names=priority_dist.index,
            title="Topic Priority Distribution"
        )
        st.plotly_chart(fig_priority, use_container_width=True)
    else:
        st.info("No topic data available")

with col2:
    st.subheader("✅ Action Items Status")

    if len(action_items_filtered) > 0:
        # Action items by status
        status_counts = action_items_filtered['status'].value_counts()

        fig_actions = px.pie(
            values=status_counts.values,
            names=status_counts.index,
            title="Action Items by Status",
            color=status_counts.index,
            color_discrete_map={
                'Completed': '#28a745',
                'In Progress': '#ffc107',
                'Pending': '#dc3545'
            }
        )
        st.plotly_chart(fig_actions, use_container_width=True)

        # Recent action items
        st.markdown("**Recent Action Items:**")
        recent_actions = action_items_filtered.sort_values('created_date', ascending=False).head(5)

        for _, action in recent_actions.iterrows():
            status_emoji = {"Completed": "✅", "In Progress": "🔄", "Pending": "⏳"}
            st.markdown(
                f"{status_emoji.get(action['status'], '•')} **{action['action']}**  \n"
                f"   Owner: {action['owner']} | Created: {action['created_date'].strftime('%b %d')}"
            )
    else:
        st.info("No action items available")

st.markdown("---")

# === ROW 5: BLOCKERS & GROWTH ===
col1, col2 = st.columns(2)

with col1:
    st.subheader("🚧 Blockers & Challenges")

    if len(blockers_filtered) > 0:
        # Active vs Resolved
        blocker_status = blockers_filtered['status'].value_counts()

        fig_blockers = px.bar(
            x=blocker_status.index,
            y=blocker_status.values,
            title="Blocker Status",
            labels={'x': 'Status', 'y': 'Count'},
            color=blocker_status.index,
            color_discrete_map={'Active': '#dc3545', 'Resolved': '#28a745'}
        )
        st.plotly_chart(fig_blockers, use_container_width=True)

        # List active blockers
        st.markdown("**Active Blockers:**")
        active = blockers_filtered[blockers_filtered['status'] == 'Active'].sort_values('severity', ascending=False)

        if len(active) > 0:
            for _, blocker in active.iterrows():
                severity_color = {'High': '🔴', 'Medium': '🟡', 'Low': '🟢'}
                st.markdown(
                    f"{severity_color.get(blocker['severity'], '•')} **{blocker['blocker']}**  \n"
                    f"   {blocker['direct_report']} | Since: {blocker['first_mentioned']}"
                )
        else:
            st.success("No active blockers!")
    else:
        st.info("No blocker data available")

with col2:
    st.subheader("🌱 Growth & Development")

    if len(growth_filtered) > 0:
        # Growth areas by person
        fig_growth = px.bar(
            growth_filtered,
            x='progress_level',
            y='area',
            color='direct_report',
            orientation='h',
            title="Development Areas Progress (1=Beginning, 5=Advanced)",
            labels={'progress_level': 'Progress Level', 'area': 'Growth Area'}
        )
        fig_growth.update_layout(height=400)
        st.plotly_chart(fig_growth, use_container_width=True)

        # Growth details
        st.markdown("**Development Focus:**")
        for _, growth in growth_filtered.iterrows():
            progress_bar = "▓" * growth['progress_level'] + "░" * (5 - growth['progress_level'])
            st.markdown(
                f"**{growth['area']}** ({growth['direct_report']})  \n"
                f"   {progress_bar} | {growth['activities']}"
            )
    else:
        st.info("No growth data available")

st.markdown("---")

# === FOOTER ===
st.markdown("### 💡 Key Insights")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Strengths:**")
    strengths_found = False

    if avg_sentiment > 0.55:
        st.success("• Positive overall team morale and engagement")
        strengths_found = True
    if completion_rate >= 50:
        st.success(f"• Good action item follow-through ({completion_rate:.0f}%)")
        strengths_found = True
    if active_blockers <= 3:
        st.success("• Manageable number of active blockers")
        strengths_found = True

    # Check for improving trends
    if len(meetings_filtered) >= 2:
        recent_sentiment = meetings_filtered.sort_values('date').tail(2)['sentiment_score'].mean()
        if recent_sentiment > avg_sentiment:
            st.success("• Recent meetings show improving sentiment")
            strengths_found = True

    if not strengths_found:
        st.info("Check individual metrics for specific strengths")

with col2:
    st.markdown("**Areas for Attention:**")
    concerns_found = False

    if avg_sentiment < 0.45:
        st.warning("• Meeting sentiment below neutral - investigate concerns")
        concerns_found = True
    if completion_rate < 50:
        st.warning(f"• Low action item completion rate ({completion_rate:.0f}%)")
        concerns_found = True
    if active_blockers > 5:
        st.warning(f"• High number of active blockers ({active_blockers}) may impact progress")
        concerns_found = True

    # Check for declining trends
    if len(meetings_filtered) >= 2:
        recent_sentiment = meetings_filtered.sort_values('date').tail(2)['sentiment_score'].mean()
        if recent_sentiment < avg_sentiment - 0.1:
            st.warning("• Recent meetings show declining sentiment")
            concerns_found = True

    if not concerns_found:
        st.success("No major concerns detected!")

st.markdown("---")
st.caption("POC Dashboard | ComChord Data Internship Technical Test")
