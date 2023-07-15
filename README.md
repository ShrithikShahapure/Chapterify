# Chapterify
This is a Streamlit Applicaion that generates chapters and sumaries for youtube videos using Streamlit and ChatGPT.
It runs on a docker container in and AWS EC2 instance that had Continuous Deployment by Github Actions.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`MY_OPENAI_KEY`

## Run Locally

Clone the project

```bash
  git clone https://github.com/ShrithikShahapure/Chapterify.git
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Go to the project directory

```bash
  cd Chapterify
```

Execute the program

```bash
 streamlit run main.py
```

