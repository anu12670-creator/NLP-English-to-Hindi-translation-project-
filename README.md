# NLP-English-to-Hindi-translation-project-
NLP-based English to Hindi translation project using Hugging Face Transformers and MarianMT.


# English to Hindi Translation using NLP

## 📌 Project Overview

This project is an English to Hindi language translation system developed using Natural Language Processing (NLP) and Hugging Face Transformers.

The system takes an English sentence as input and generates its corresponding Hindi translation using a MarianMT model. The project can also be deployed as an interactive web application using Streamlit.

## 🎯 Objective

The main objective of this project is to build an automated English-to-Hindi translation system that can:
- Accept English text from the user
- Process the input using an NLP translation model
- Generate Hindi translations
- Provide the translated output through a simple user interface

## 🛠️ Technologies Used

- Python
- Natural Language Processing (NLP)
- Hugging Face Transformers
- MarianMT
- PyTorch
- Pandas
- Streamlit
- Google Colab
- GitHub

## 🤖 Model Used

The project uses the Hugging Face MarianMT model:

`Helsinki-NLP/opus-mt-en-hi`

This model is designed for English → Hindi machine translation.

## 📂 Project Structure

```text
English-to-Hindi-Translation/
│
├── app.py
├── project.py
├── requirements.txt
├── README.md
└── dataset/
    └── project_nlp.csv
```

> The exact files and folders may vary depending on your final project structure.

## 📊 Dataset

The project uses an English-Hindi translation dataset containing pairs of sentences in English and Hindi.

Example:

| English | Hindi |
|---|---|
| What is your name? | आपका नाम क्या है? |
| How are you? | आप कैसे हैं? |
| Good morning | शुभ प्रभात |

## ⚙️ How the Project Works

```text
English Input
      ↓
Text Preprocessing
      ↓
Tokenizer
      ↓
MarianMT Model
      ↓
Translation Generation
      ↓
Hindi Output
```

## 🔧 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/your-repository-name.git
```

Move into the project directory:

```bash
cd English-to-Hindi-Translation
```

Create a virtual environment:

```bash
python -m venv myenv
```

Activate the environment on Windows:

```bash
myenv\Scriptsctivate
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Project

If using the Python project file:

```bash
python project.py
```

If using the Streamlit application:

```bash
streamlit run app.py
```

## 🌐 Streamlit Application

The Streamlit interface allows users to enter an English sentence and obtain its Hindi translation interactively.

### Example

**Input:**
```text
What is your name?
```

**Output:**
```text
आपका नाम क्या है?
```

## 📦 Requirements

The main libraries used in this project include:

```text
transformers
torch
pandas
streamlit
sentencepiece
```

All required dependencies can be installed using:

```bash
pip install -r requirements.txt
```

## 💡 Features

- English-to-Hindi translation
- NLP-based translation
- Hugging Face Transformers
- MarianMT model
- Simple user interface
- Streamlit deployment
- Easy-to-use translation system

## 🚀 Future Improvements

The project can be improved by:
- Supporting more Indian languages
- Improving translation accuracy
- Adding voice input
- Adding text-to-speech output
- Supporting larger datasets
- Deploying the application online
- Adding multilingual translation options

## 👨‍💻 Author

**S. Anurag**

B.Tech – Computer Science and Engineering (Artificial Intelligence & Machine Learning)

GitHub: https://github.com/anu12670-creator

## 📜 License

This project is developed for educational and learning purposes.

