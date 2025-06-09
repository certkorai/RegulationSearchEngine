import sys
import os
import streamlit as st
import pandas as pd

# Add the 'src' directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from angentic_base.crew import Agent_hub

st.set_page_config(page_title="Compliance Checker", layout="wide")

st.title("🛡️ Compliance Control Extractor")
st.write("Enter a country to extract & validate compliance dimensions using CrewAI agents.")

country = st.text_input("🌍 Country Name")

if st.button("Run Compliance Check"):
    if not country:
        st.warning("Please enter a country name first.")
    else:
        try:
            with st.spinner("⏳ Running agent crews..."):
                crew = Agent_hub()
                crew.run(country)
            st.success("✅ Crew execution complete!")

            # Define file paths and tab names
            tabs_info = {
                "🔐 Security": "output/security.md",
                "🕵️ Privacy": "output/privacy.md",
                "🔍 Transparency": "output/transparency.md",
                "⚖️ Fairness": "output/fairness.md",
                "📦 Final Consolidated": "final.md"
            }

            tab_titles = list(tabs_info.keys())
            tabs = st.tabs(tab_titles)

            for tab, (title, path) in zip(tabs, tabs_info.items()):
                with tab:
                    if os.path.exists(path):
                        with open(path, "r", encoding="utf-8") as f:
                            markdown_table = f.read()
                            try:
                                # Convert markdown table to DataFrame
                                # The separator is '|', but we need to handle potential leading/trailing spaces
                                # and also skip the header separator line.
                                
                                # Split the markdown content into lines
                                lines = markdown_table.splitlines()
                                
                                # Find the line that separates the header from the data (the one with hyphens)
                                separator_index = next((i for i, line in enumerate(lines) if all(c in ['-', ' ', '|'] for c in line)), None)
                                
                                if separator_index is not None:
                                    # Extract the header and data rows
                                    header = [h.strip() for h in lines[0].split('|') if h.strip()]
                                    data_lines = lines[separator_index + 1:]
                                    
                                    # Process data rows
                                    data = []
                                    for line in data_lines:
                                        row = [cell.strip() for cell in line.split('|') if cell.strip()]
                                        if row:  # Only add if the row is not empty
                                            data.append(row)
                                    
                                    # Create DataFrame
                                    df = pd.DataFrame(data, columns=header)
                                    st.dataframe(df)
                                else:
                                    st.markdown(markdown_table)
                                    #st.warning(f"Could not find a valid table format in {title}. Showing raw content.")
                            except Exception as e:
                                st.markdown(markdown_table)
                                #st.error(f"⚠️ Could not parse markdown as table in {title}. Showing raw content:")
                            #st.markdown(markdown_table)
                    else:
                        st.warning(f"{title} output not found: `{path}`")

        except Exception as e:
            st.error(f"❌ Error: {e}")
