# ChatGPT-clone
Build Your own ChatGPT with [revChatGPT](https://github.com/acheong08/ChatGPT) and [Streamlit](https://github.com/streamlit/streamlit)

- Get your access token from - https://chat.openai.com/api/auth/session
- Replace that in the file `chatgpt.py`, inside the config variable
```python
config = {
    "Authorization": "<leave this as whatever - it will get replaced>",
    "access_token": "YOUR_TOKEN_HERE",
}
```
- Install the required libraries `pip install -r requirements.txt`
- Run `python -m streamlit run chatgpt.py`


## Quick Demo: 
https://user-images.githubusercontent.com/5618143/208082095-7e5cadea-4478-4e7d-a96d-e47a52cdce9b.mp4


## Disclaimer

This project is not affiliated with OpenAI in any way. Use at your own risk. I am not responsible for any damage caused by this project. Please read the [OpenAI Terms of Service](https://beta.openai.com/terms) before using this project.
