{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Ashika0509/DSPL_ICW/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "! pip install streamlit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "t-6KjUGOWgrh",
        "outputId": "c9955413-b50e-47a0-9961-99f4d4054451"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.12/dist-packages (1.56.0)\n",
            "Requirement already satisfied: altair!=5.4.0,!=5.4.1,<7,>=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.5.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<8,>=5.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.2.6)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.3.2)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.12/dist-packages (from streamlit) (3.1.46)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.0.2)\n",
            "Requirement already satisfied: packaging>=20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (26.0)\n",
            "Requirement already satisfied: pandas<4,>=1.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: pillow<13,>=7.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (11.3.0)\n",
            "Requirement already satisfied: pydeck<1,>=0.8.0b4 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.9.2)\n",
            "Requirement already satisfied: protobuf<8,>=3.20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.29.6)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (18.1.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.32.4)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (9.1.4)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.5.1)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.10.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (4.15.0)\n",
            "Requirement already satisfied: watchdog<7,>=2.1.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.0.0)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.1.6)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (4.26.0)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2.19.0)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.12/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas<4,>=1.4.0->streamlit) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas<4,>=1.4.0->streamlit) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas<4,>=1.4.0->streamlit) (2026.1)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (3.4.7)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (3.11)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2026.2.25)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.12/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.3)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.0.3)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (26.1.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2025.9.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (0.37.0)\n",
            "Requirement already satisfied: rpds-py>=0.25.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (0.30.0)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.8.2->pandas<4,>=1.4.0->streamlit) (1.17.0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#import libraries\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import plotly.express as px\n",
        "import plotly.graph_objects as go\n",
        "from plotly.subplots import make_subplots"
      ],
      "metadata": {
        "id": "x2BlRtjtvi6W"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Page Config\n",
        "st.set_page_config(\n",
        "    page_title=\"Sri Lanka Energy & Sustainability Dashboard\",\n",
        "    page_icon=\"𝙎𝙇\",\n",
        "    layout=\"wide\",\n",
        "    initial_sidebar_state=\"expanded\"\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wlpDQ-9hvl-T",
        "outputId": "bf81764e-9bc2-4427-ddbe-ac3420aea82a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2026-04-17 12:13:59.549 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Load data\n",
        "df = pd.read_csv('/content/drive/MyDrive/W2120559_DSPL_CWK2/Data/Processed Data/cleaned_indicators_lka.csv')"
      ],
      "metadata": {
        "id": "LbLjLVWUwt77"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Sidebar Navigation\n",
        "page = st.sidebar.selectbox(\"Navigation\", [\"About\", \"Home\", \"Advanced Analysis\"])"
      ],
      "metadata": {
        "id": "C-vWTHJDw8fG",
        "outputId": "a7712712-24f0-48e4-9525-4c6a310ac7ab",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2026-04-17 12:14:01.404 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-17 12:14:01.405 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-17 12:14:01.407 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-17 12:14:01.409 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-17 12:14:01.410 WARNING streamlit.runtime.state.session_state_proxy: Session state does not function when running a script without `streamlit run`\n",
            "2026-04-17 12:14:01.412 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-17 12:14:01.668 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.12/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n",
            "2026-04-17 12:14:01.669 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-17 12:14:01.670 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "id": "5CrFBQQBW4hz",
        "outputId": "e3717a25-81ca-4203-845d-2cb476252337",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Sidebar Navigation\n",
        "page = st.sidebar.selectbox(\"📍Navigation\", [\"About\", \"Home\", \"Advanced Analysis\"])\n",
        "\n",
        "# About Page\n",
        "if page == \"About\":\n",
        "    st.title(\"🔎 About this Dashboard\")\n",
        "    st.image(\n",
        "        \"https://crowdsourcingweek.com/wp-content/uploads/2017/11/Energy-Sustainability.jpg.webp\",\n",
        "        use_container_width=True\n",
        "    )\n",
        "\n",
        "    st.markdown(\"\"\"\n",
        "    ## 𝙎𝙇 Sri Lanka Energy & Sustainability Dashboard\n",
        "\n",
        "    This dashboard visualises key energy and sustainability indicators for Sri Lanka from 2000 to 2024 with interactive tools for analysis.\n",
        "\n",
        "    ### 🧩 Key Features:\n",
        "    - ⚡ Electricity access analysis (urban vs rural)\n",
        "    - ♻️ Renewable vs fossil fuel comparison\n",
        "    - 📈 Energy production trends\n",
        "    - 📊 Efficiency and sustainability indicators\n",
        "    - 🔁 Interactive filtering and comparison\n",
        "    - 📉 System loss and performance insights\n",
        "\n",
        "    ### 📊 Dataset:\n",
        "    - Source: [World Bank via HDX] (https://data.humdata.org/dataset/world-bank-energy-and-mining-indicators-for-sri-lanka)\n",
        "    - Indicators include electricity access, renewable energy, fossil fuel usage, energy efficiency, and electricity production sources.\n",
        "    - Timeframe: 2000 to 2024\n",
        "\n",
        "    ### 🛠️ Built With:\n",
        "    - Python, Streamlit, Plotly, Pandas\n",
        "\n",
        "    **Author:** Ashika Samarasinghe\n",
        "    **Student ID:** w2120559 | 20233112\n",
        "    \"\"\")\n",
        "\n",
        "\n",
        "# Home Page\n",
        "elif page == \"Home\":\n",
        "    st.title(\"𝙎𝙇 Sri Lanka Energy & Sustainability Dashboard\")\n",
        "    st.markdown(\"Explore Sri Lanka's key energy and sustainability trends over time.\")\n",
        "\n",
        "    st.sidebar.title(\"🔍 Filters\")\n",
        "    all_indicators = df['Indicator'].unique()\n",
        "\n",
        "    selected_indicators = st.sidebar.multiselect(\n",
        "        \"Select Indicators:\",\n",
        "        options=all_indicators,\n",
        "        default= list(all_indicators)[:5]\n",
        "    )\n",
        "\n",
        "    year_range = st.sidebar.slider(\n",
        "        \"Select Year Range:\",\n",
        "        int(df['Year'].min()), int(df['Year'].max()), (2000, 2024)\n",
        "    )\n",
        "\n",
        "    filtered_df = df[\n",
        "        (df['Indicator'].isin(selected_indicators)) &\n",
        "        (df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])\n",
        "    ]\n",
        "\n",
        "    tab1, tab2, tab3 = st.tabs([\"📈 Line Charts\", \"📊 Comparative Analysis\", \"🔍 Indicators Deep Dive\"])\n",
        "\n",
        "    with tab1:\n",
        "        st.subheader(\"📈 Energy Trend Analysis\")\n",
        "        for indicator in selected_indicators:\n",
        "            chart_df = filtered_df[filtered_df['Indicator'] == indicator]\n",
        "            fig = px.line(chart_df, x='Year',y='Value',title=f\"{indicator} Over Time\",markers=True)\n",
        "            fig.update_layout(hovermode=\"x unified\")\n",
        "            st.plotly_chart(fig, use_container_width=True)\n",
        "\n",
        "    with tab2:\n",
        "        st.subheader(\"📊 Compare Selected Energy Indicators\")\n",
        "        if len(selected_indicators) >= 2:\n",
        "            fig = make_subplots(\n",
        "                rows=len(selected_indicators), cols=1,\n",
        "                shared_xaxes=True,\n",
        "                subplot_titles=selected_indicators,\n",
        "                vertical_spacing=0.05\n",
        "            )\n",
        "            for i, indicator in enumerate(selected_indicators, start=1):\n",
        "                chart_df = filtered_df[filtered_df['Indicator'] == indicator]\n",
        "                fig.add_trace(\n",
        "                    go.Scatter(\n",
        "                        x=chart_df['Year'],\n",
        "                        y=chart_df['Value'],\n",
        "                        mode='lines+markers',\n",
        "                        name=indicator\n",
        "                    ),\n",
        "                    row=i, col=1\n",
        "                )\n",
        "            fig.update_layout(\n",
        "                height=300 * len(selected_indicators),hovermode='x unified',showlegend=False)\n",
        "            st.plotly_chart(fig, use_container_width=True)\n",
        "        else:\n",
        "            st.warning(\"🚨 Please select at least two indicators for comparison.\")\n",
        "\n",
        "    with tab3:\n",
        "        st.subheader(\"🔍 Multiple Energy Indicators Overview\")\n",
        "        if not filtered_df.empty:\n",
        "            fig = px.line(\n",
        "                filtered_df,\n",
        "                x=\"Year\",\n",
        "                y=\"Value\",\n",
        "                color=\"Indicator\",\n",
        "                markers=True,\n",
        "                title=\"Selected Energy Indicators Over Time\"\n",
        "            )\n",
        "            fig.update_layout(hovermode='x unified')\n",
        "            st.plotly_chart(fig, use_container_width=True)\n",
        "        else:\n",
        "            st.warning(\"🚨 No data available for the selected filters.\")\n",
        "\n",
        "    st.markdown(\"---\")\n",
        "    st.subheader(\"📌 Key Metrics\")\n",
        "    if not filtered_df.empty:\n",
        "        latest_year = filtered_df['Year'].max()\n",
        "        latest_data = filtered_df[filtered_df['Year'] == latest_year]\n",
        "        cols = st.columns(min(4, len(latest_data)))\n",
        "        for col, row in zip(cols, latest_data.itertuples()):\n",
        "            col.metric(f\"{row.Indicator} ({int(row.Year)})\", f\"{row.Value:,.2f}\")\n",
        "    else:\n",
        "        st.info(\"No KPI data to display.\")\n",
        "\n",
        "    st.markdown(\"---\")\n",
        "    st.subheader(\"🗂️ Raw Data Table\")\n",
        "    st.dataframe(filtered_df.sort_values([\"Indicator\", \"Year\"]), use_container_width=True)\n",
        "\n",
        "\n",
        "# Advanced Analysis\n",
        "elif page == \"Advanced Analysis\":\n",
        "    st.title(\"📊 Advanced Statistical Analysis\")\n",
        "\n",
        "    st.subheader(\"📌 Univariate Analysis\")\n",
        "    selected_uni = st.multiselect(\n",
        "        \"Select Indicators for Histogram:\",\n",
        "        options=df['Indicator'].unique(),\n",
        "        default=list(df['Indicator'].unique())[:3]\n",
        "    )\n",
        "    for indicator in selected_uni:\n",
        "        chart_df = df[df['Indicator'] == indicator]\n",
        "        fig = px.histogram(chart_df,x='Value',nbins=30,title=f\"Distribution: {indicator}\")\n",
        "        st.plotly_chart(fig, use_container_width=True)\n",
        "\n",
        "    st.markdown(\"---\")\n",
        "\n",
        "    st.subheader(\" 📌 Bivariate Analysis\")\n",
        "    col1, col2 = st.columns(2)\n",
        "    with col1:\n",
        "      x_indicator = st.selectbox(\"X-axis Indicator:\", options=df['Indicator'].unique())\n",
        "    with col2:\n",
        "      y_indicator = st.selectbox(\"Y-axis Indicator:\", options=df['Indicator'].unique())\n",
        "\n",
        "    x_df = df[df['Indicator'] == x_indicator]\n",
        "    y_df = df[df['Indicator'] == y_indicator]\n",
        "    merged_df = pd.merge(x_df, y_df, on='Year', suffixes=('_X', '_Y'))\n",
        "\n",
        "    if not merged_df.empty:\n",
        "        fig = px.scatter(\n",
        "            merged_df,\n",
        "            x='Value_X',\n",
        "            y='Value_Y',\n",
        "            trendline='ols',\n",
        "            labels={'Value_X': x_indicator, 'Value_Y': y_indicator},\n",
        "            title=f\"{x_indicator} vs {y_indicator}\"\n",
        "        )\n",
        "        st.plotly_chart(fig, use_container_width=True)\n",
        "    else:\n",
        "        st.warning(\" 🚨 No matching yearly data available for the selected indicators.\")\n",
        "\n",
        "    st.markdown(\"---\")\n",
        "\n",
        "    st.subheader(\"📊 Correlation Heatmap\")\n",
        "    selected_multi = st.multiselect(\n",
        "        \"Select indicators for correlation matrix:\",\n",
        "        options=df['Indicator'].unique(),\n",
        "        default=list(df['Indicator'].unique())[:5]\n",
        "    )\n",
        "\n",
        "    multi_df = df[df['Indicator'].isin(selected_multi)]\n",
        "    pivot_df = multi_df.pivot(index='Year', columns='Indicator', values='Value')\n",
        "    corr = pivot_df.corr()\n",
        "\n",
        "    if not corr.empty:\n",
        "        fig = px.imshow(\n",
        "            corr,\n",
        "            text_auto=True,\n",
        "            color_continuous_scale=\"RdBu_r\",\n",
        "            title=\"Correlation Matrix (Multivariate)\"\n",
        "        )\n",
        "        st.plotly_chart(fig, use_container_width=True)\n",
        "    else:\n",
        "        st.warning(\" 🚨 Not enough data available to generate the correlation matrix.\")"
      ],
      "metadata": {
        "id": "Ud-TGRqXxv2z",
        "outputId": "b3d6f95c-33c1-4720-f8a2-6c32355fc94a",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2026-04-17 12:14:03.867 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-17 12:14:03.868 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-17 12:14:03.869 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-17 12:14:03.870 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-17 12:14:03.871 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-17 12:14:03.874 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-17 12:14:03.877 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-17 12:14:03.880 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-17 12:14:03.881 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-17 12:14:03.883 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-17 12:14:03.885 Please replace `use_container_width` with `width`.\n",
            "\n",
            "`use_container_width` will be removed after 2025-12-31.\n",
            "\n",
            "For `use_container_width=True`, use `width='stretch'`. For `use_container_width=False`, use `width='content'`.\n",
            "2026-04-17 12:14:03.887 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-17 12:14:03.888 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-17 12:14:03.889 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-17 12:14:03.890 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-17 12:14:03.891 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-17 12:14:03.892 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-17 12:14:03.893 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    }
  ]
}