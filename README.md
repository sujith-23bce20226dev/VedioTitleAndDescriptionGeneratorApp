# 📺 Video Title & Description Generator App

A Generative AI-powered web application built using Streamlit and FLAN-T5 model that automatically generates creative video titles and engaging descriptions based on a given video topic, idea, or keywords.

Ideal for content creators, marketers, and educators to enhance their video content metadata efficiently.

## 📎 Live Demo  

🔗 https://videotitleanddescriptiongeneratorapp-tbq6pzfyyosfecjcydnduq.streamlit.app/

📌 Features

✍️ Generates 5 creative video titles for the given topic.

📝 Generates a 3–5 line video description in natural language.

⚙️ Simple, clean web-based interface built with Streamlit.

🚀 Powered by Hugging Face’s FLAN-T5 Large model for high-quality text generation.

📊 Displays generation progress using an interactive progress spinner.

📂 Project Structure

VideoTitleAndDescriptionApp/

├── app.py                 # Main Streamlit app

├── requirements.txt       # Python dependencies

├── sample_outputs/

│   ├── screenshot1.png

│   ├── screenshot2.png

│   ├── ...

│   └── screenshot12.png   # Screenshots of app usage & output

└── README.md              # Project documentation (this file)

🚀 How to Run

📦 Install Requirements:

pip install -r requirements.txt

▶️ Run the App:

streamlit run app.py

📸 Sample Screenshots

Screenshots showcasing app input, generated titles, and descriptions are available in the sample_outputs/ folder.

🌱 Future Work

While the current version generates titles and descriptions based on video topics, the following improvements are planned:

Multi-language Content Generation — support titles and descriptions in different languages.

Hashtag Suggestions — generate relevant hashtags for video optimization.

SEO-optimized Description Enhancements — generate search-friendly, keyword-rich descriptions tailored for video platforms.

🛠️ Tech Stack

Python 3.11

Streamlit

Hugging Face Transformers

FLAN-T5 Large model

PyTorch

