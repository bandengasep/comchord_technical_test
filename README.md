# 1:1 Meeting Insights Dashboard

An interactive data dashboard that transforms 1:1 conversation transcripts into actionable insights for managers. Built as part of the ComChord Data Internship Technical Test.

![Dashboard Preview](https://img.shields.io/badge/Status-POC-blue) ![Python](https://img.shields.io/badge/Python-3.9+-green) ![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red)

## 🎯 Project Overview

This dashboard is designed for **Sarah Chen**, a Senior Director of Product, to visualize insights from her 1:1 meetings with two direct reports:
- **Alex Rodriguez** (Product Manager)
- **Javier Morales** (QA Lead)

The dashboard extracts and visualizes key metrics including sentiment trends, OKR progress, action item completion, blockers, and communication patterns.

## ✨ Features

- **📈 Sentiment Tracking** - Monitor team morale over time
- **🎯 OKR Progress Visualization** - Track actual vs. target metrics
- **✅ Action Item Management** - View completion rates and status
- **🚧 Blocker Identification** - Identify and track persistent challenges
- **💬 Communication Patterns** - Analyze conversation dynamics (hedge words, question ratios)
- **🌱 Growth & Development** - Track individual development areas
- **🔍 Interactive Filters** - Filter by date range or individual direct report
- **💡 AI-Generated Insights** - Automatic strengths and areas for attention

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip

### Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd comchord_technical_test
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the dashboard:
```bash
streamlit run dashboard.py
```

4. Open your browser to `http://localhost:8501`

## 📊 Data Generation

To regenerate the synthetic dataset:

```bash
python generate_synthetic_data.py
```

This creates 7 CSV files containing:
- Meeting metadata
- Discussion topics
- Action items
- OKR metrics
- Blockers
- Growth areas
- Communication patterns

## 📁 Project Structure

```
.
├── dashboard.py                    # Main Streamlit application
├── generate_synthetic_data.py      # Synthetic data generator
├── requirements.txt                # Python dependencies
├── TECHNICAL_REPORT.md            # Design choices and methodology
├── CLAUDE.md                      # Project context documentation
├── data_meetings.csv              # Meeting metadata
├── data_topics.csv                # Discussion topics
├── data_action_items.csv          # Action items tracking
├── data_metrics.csv               # OKR/metrics data
├── data_blockers.csv              # Blockers and challenges
├── data_growth_areas.csv          # Development focus areas
├── data_communication.csv         # Communication patterns
├── 1-to-1 convos/                 # Original conversation transcripts
│   ├── Alex_R_*.txt
│   └── Javier_M_*.txt
└── bonus materials/               # Team conversation transcripts
    └── Code Review Weekly Workshop - *.txt
```

## 🛠️ Technology Stack

- **Frontend/Visualization**: Streamlit, Plotly
- **Data Processing**: Pandas, NumPy
- **Language**: Python 3.9+

## 📋 Key Visualizations

1. **Sentiment Trend Line** - Tracks emotional tone of meetings over time
2. **OKR Progress Charts** - Compares actual performance against targets
3. **Communication Pattern Metrics** - Visualizes hedge words (confidence indicator)
4. **Action Item Status** - Pie chart breakdown of completion status
5. **Topic Frequency** - Horizontal bar chart of most discussed topics
6. **Blocker Tracking** - Active vs. resolved challenges
7. **Growth Areas Progress** - Development focus and progress levels

## 📝 Documentation

See [TECHNICAL_REPORT.md](TECHNICAL_REPORT.md) for:
- Dashboard design rationale
- Visualization choices
- Difficulties encountered
- Future enhancement roadmap

## 🎓 Project Context

This project was developed for the **ComChord Data Internship Technical Test** with the following objectives:
1. Validate technical skills in data analysis and visualization selection
2. Demonstrate ability to approach and break down ambiguous tasks
3. Design user-centric dashboards for manager-level decision-making

**Time Constraint**: Maximum 4 hours of focused development time

## 🔮 Future Enhancements

- [ ] Parse real conversation transcripts using NLP
- [ ] Implement automated sentiment analysis
- [ ] Add action item extraction from text
- [ ] Integrate team conversation analysis (bonus materials)
- [ ] Develop predictive analytics features
- [ ] Add export capabilities (PDF reports, CSV)
- [ ] LLM-powered conversation summarization

## 👤 Author

**Timothy**
ComChord Data Internship Candidate

## 📄 License

This project is created for educational and evaluation purposes as part of a technical assessment.

---

*Generated with assistance from Claude Code (claude.ai/code)*
