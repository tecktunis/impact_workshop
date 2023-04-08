# IMPORTS
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from PIL import Image

# FUNCTIONS
# Create a custom color function for the WordCloud
def custom_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    if word in positive_words:
        return "lightblue"
    elif word in neutral_words:
        return "grey"
    else:
        return "red"

# STREAMLIT SIDEBAR FOR NAVIGATION
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "Overall Workshop Quality",
        "Question 1: Understanding Impact",
        "Question 2: Metrics that Matter",
        "Question 3: Instructor Improvement",
    ],
)

# PAGE 1: OVERALL WORKSHOP QUALITY
if page == "Overall Workshop Quality":
    
    # Title
    st.title('Overall Quality of the Workshop')
    
    # Sentiment percentages pie chart
    sentiment_labels = ["Positive", "Neutral", "Negative"]
    sentiment_data = [80, 15, 5]
    cmap = plt.get_cmap("Blues")
    colors = [cmap(i) for i in np.linspace(0.3, 0.8, len(sentiment_labels))]
    plt.pie(sentiment_data, labels=sentiment_labels, autopct="%1.1f%%", startangle=90, colors=colors)
    plt.axis("equal")
    st.pyplot(plt.gcf())
    plt.clf()

    # Agreement data
    session_data = {
        "Learning objectives clear": 85,
        "Interactivity": 70,
        "Pace appropriate": 80,
        "Overall satisfaction": 80,
    }
    instructor_data = {
        "Instructor’s preparedness": 95,
        "Instructor’s expertise": 95,
        "Instructor’s engagement": 90,
        "Overall satisfaction": 90,
    }

    # Custom horizontal bar chart function
    def custom_horizontal_bar_chart(data, title):
        fig, ax = plt.subplots()
        y_labels = list(data.keys())
        y_values = list(range(len(y_labels)))
        x_values = list(data.values())

        ax.barh(y_values, x_values, color=plt.cm.Blues(np.linspace(0.3, 1, len(y_values))))
        ax.set_yticks(y_values)
        ax.set_yticklabels(y_labels)
        ax.set_title(title)

        for i, v in enumerate(x_values):
            ax.text(v / 2, i, str(v) + "%", color="white", fontweight="bold", ha="center", va="center")

        st.pyplot(fig)
        plt.clf()

    # Horizontal bar charts for session and instructor
    st.subheader("Session")
    custom_horizontal_bar_chart(session_data, "Session")
    st.subheader("Instructor")
    custom_horizontal_bar_chart(instructor_data, "Instructor")


    # Recommendation and substitute
    def display_percentage_circle(percentage, title):
        fig, ax = plt.subplots(subplot_kw=dict(aspect="equal"))
        ax.axis("off")
        ax.set_title(title)

        ax.add_artist(plt.Circle((0, 0), 1, color="gray", alpha=0.2))
        ax.add_artist(plt.Circle((0, 0), percentage / 100, color="blue", alpha=0.7))
        ax.text(0, 0, f"{percentage}%", ha="center", va="center", fontsize=20, color="black")

        st.pyplot(fig)
        plt.clf()

    st.subheader("Recommendation to others")
    display_percentage_circle(85, "")
    st.subheader("Substitute for Metrics that Matter")
    display_percentage_circle(75, "")

# PAGE 2: QUESTION 1 - UNDERSTANDING IMPACT
elif page == "Question 1: Understanding Impact":
    
    # Title
    st.title('Question 1: Has this workshop provided you with a working definition (or at least a better grasp) of what impact is?')

    # Sentiment percentages pie chart
    sentiment_labels = ["Positive", "Neutral", "Negative"]
    sentiment_data = [75, 12.5, 12.5]
    cmap = plt.get_cmap("Blues")
    colors = [cmap(i) for i in np.linspace(0.3, 0.8, len(sentiment_labels))]
    plt.pie(sentiment_data, labels=sentiment_labels, autopct="%1.1f%%", startangle=90, colors=colors)
    plt.axis("equal")
    st.pyplot(plt.gcf())
    plt.clf()

    # Prominent topics word cloud
    # Define the words for each sentiment
    positive_words = ["Working definition or better grasp of impact", "Focus on environmental impact", "Understanding of impact measurement and future changes", "Legislation"]
    neutral_words = []
    negative_words = ["No clear definition provided"]

    # Prominent topics word cloud
    st.subheader("Prominent topics surrounding the question (weighted by frequency):")
    topics = {
        "Working definition or better grasp of impact": 5,
        "Focus on environmental impact": 1,
        "Understanding of impact measurement and future changes": 1,
        "Legislation": 1,
        "No clear definition provided": 1,
    }

    wc = WordCloud(width=800, height=400, background_color="white", color_func=custom_color_func).generate_from_frequencies(topics)
    st.image(wc.to_array())

    # Create a legend for the word cloud
    st.write("*Legend*")
    st.markdown(
    "<div style='display: flex; justify-content: space-between;'>"
    "<span style='color: lightblue'>Positive</span>"
    "<span style='color: grey'>Neutral</span>"
    "<span style='color: red'>Negative</span>"
    "</div>",
    unsafe_allow_html=True,
    )
    
    # Recommendations
    st.subheader("Recommendations")
    recommendations = [
        "Broaden the scope of impact: While some participants appreciated the focus on environmental impact, it would be beneficial to provide a more comprehensive understanding of impact, including social, economic, and governance aspects, to cater to a diverse audience with different interests.",
        "Clarify definitions and concepts: Ensure that the workshop clearly presents a working definition of impact and helps participants understand the concept better. This can be done through examples, case studies, and interactive discussions.",
        "Provide more information on impact measurement: As some participants mentioned gaining insights into current measurement methods and future changes, it would be helpful to dedicate a portion of the workshop to discussing various approaches to impact measurement, along with their strengths and weaknesses.",
        "Balance content: While legislation was seen as relevant and useful, make sure that the workshop balances its content between providing a clear definition of impact, discussing measurement methods, and covering related topics such as legislation.",
        "Encourage interaction and feedback: Facilitate more interaction among participants and offer opportunities for them to provide feedback or ask questions during the workshop. This will help clarify any confusion or misunderstandings regarding the concept of impact and create a more engaging learning environment.",
        "Customize content for different levels of expertise: To accommodate participants with varying levels of experience and knowledge about impact, consider offering separate workshops or breakout sessions tailored to different expertise levels, such as beginner, intermediate, and advanced.",
        "Provide follow-up resources: Share additional resources, such as articles, research papers, or online courses, to help participants deepen their understanding of impact and related topics after the workshop.",
    ]
    for rec in recommendations:
        st.write(f"- {rec}")

# PAGE 3: QUESTION 2 - METRICS THAT MATTER
elif page == "Question 2: Metrics that Matter":
    
    # Title
    st.title('Question 2: What if this Workshop became Metrics that Matter?')

    # Sentiment percentages pie chart
    sentiment_labels = ["Positive", "Neutral", "Negative"]
    sentiment_data = [87.5, 12.5, 0]
    cmap = plt.get_cmap("Blues")
    colors = [cmap(i) for i in np.linspace(0.3, 0.8, len(sentiment_labels))]
    plt.pie(sentiment_data, labels=sentiment_labels, autopct="%1.1f%%", startangle=90, colors=colors)
    plt.axis("equal")
    st.pyplot(plt.gcf())
    plt.clf()

    # Prominent topics word cloud    
    # Define the words for each sentiment
    positive_words = ["Interest in the workshop content", "Instructor's background and engagement", "Connection to the master's overall theme", "Practicality of the workshop"]
    neutral_words = ["Retaining some statistical elements from Metrics that Matter"]
    negative_words = []

    # Prominent topics word cloud
    st.subheader("Prominent topics surrounding the question (weighted by frequency):")
    topics = {
        "Interest in the workshop content": 5,
        "Instructor's background and engagement": 2,
        "Retaining some statistical elements from Metrics that Matter": 3,
        "Connection to the master's overall theme": 2,
        "Practicality of the workshop": 1,
    }

    wc = WordCloud(width=800, height=400, background_color="white", color_func=custom_color_func).generate_from_frequencies(topics)
    st.image(wc.to_array())

    # Create a legend for the word cloud
    st.write("*Legend*")
    st.markdown(
        "<div style='display: flex; justify-content: space-between;'>"
        "<span style='color: lightblue'>Positive</span>"
        "<span style='color: grey'>Neutral</span>"
        "<span style='color: red'>Negative</span>"
        "</div>",
        unsafe_allow_html=True,
    )

    # Recommendations
    st.subheader("Recommendations")
    recommendations = [
        "Maintain the practical focus: Participants appreciated the practicality of the workshop, so ensure that this focus is retained when expanding the course. Use real-world examples and case studies to illustrate the concepts and help students connect the material to their field of study.",
        "Incorporate elements from Metrics that Matter: Some participants mentioned the importance of retaining certain statistical elements from Metrics that Matter, such as learning how to read a scientific paper. Balance the workshop's content by including these elements, while still maintaining a strong focus on impact and innovation.",
        "Leverage the instructor's expertise: Participants showed confidence in the instructor's background and engagement. Encourage the instructor to share their knowledge and experience, and facilitate interactive discussions and activities that allow students to benefit from the instructor's expertise.",
        "Connect to the master's overall theme: Ensure that the expanded course aligns with the master's program's overall theme, helping students understand how the content relates to their broader education.",
        "Consider merging with another course: One participant suggested merging the workshop with the ARM course. Explore the possibility of combining relevant elements from both courses to create a more comprehensive and coherent learning experience.",
    ]
    for rec in recommendations:
        st.write(f"- {rec}")

# PAGE 4: QUESTION 3 - INSTRUCTOR IMPROVEMENT
elif page == "Question 3: Instructor Improvement":
    
    # Title
    st.title('Question 3: What would you recommend the instructor to improve for the next workshop?')

    # Sentiment percentages pie chart
    sentiment_labels = ["Positive", "Constructive criticism"]
    sentiment_data = [20, 80]
    cmap = plt.get_cmap("Blues")
    colors = [cmap(i) for i in np.linspace(0.3, 0.8, len(sentiment_labels))]
    plt.pie(sentiment_data, labels=sentiment_labels, autopct="%1.1f%%", startangle=90, colors=colors)
    plt.axis("equal")
    st.pyplot(plt.gcf())
    plt.clf()

    # Prominent topics word cloud
    # Define the words for each sentiment
    positive_words = ["No need for improvement"]
    neutral_words = []
    negative_words = ["Expanding the focus", "Deep diving into reporting tools", "More interactivity", "More time for the topic"]

    # Prominent topics word cloud
    st.subheader("Prominent topics surrounding the question (weighted by frequency):")
    topics = {
        "Expanding the focus": 1,
        "No need for improvement": 1,
        "Deep diving into reporting tools": 1,
        "More interactivity": 1,
        "More time for the topic": 1,
    }

    wc = WordCloud(width=800, height=400, background_color="white", color_func=custom_color_func).generate_from_frequencies(topics)
    st.image(wc.to_array())

    # Create a legend for the word cloud
    st.write("*Legend*")
    st.markdown(
        "<div style='display: flex; justify-content: space-between;'>"
        "<span style='color: lightblue'>Positive</span>"
        "<span style='color: grey'>Neutral</span>"
        "<span style='color: red'>Constructive Criticism</span>"
        "</div>",
        unsafe_allow_html=True,
    )

    # Recommendations
    st.subheader("Recommendations")
    recommendations = [
        "Wider Focus: Expand the scope of the workshop to include social impact in addition to environmental impact, providing a more comprehensive understanding of impact assessment.",
        "In-depth Exploration: Deep dive into relevant reporting tools, such as the EU taxonomy, to help students gain practical knowledge and better understand the application of these tools in real-life scenarios.",
        "Interactive Learning: Incorporate more group work and gamification elements to make the workshop more engaging and facilitate active learning. For example, participants could assess the impact of a company using a suggested framework in small groups.",
        "Time Management: Allocate more time to the workshop to ensure that all topics are adequately covered and participants have enough time to fully grasp the concepts and engage in meaningful discussions.",
        "Continuous Improvement: The instructor should consider incorporating regular feedback sessions, either during or after the workshop, to identify areas for improvement and adapt the content and delivery accordingly.",
    ]
    for rec in recommendations:
        st.write(f"- {rec}")