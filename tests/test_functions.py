from bioage_framework import functions
from bioage_framework import classes
import config

# Test for local machine only, since API keys can't be transferred to github safely
# Possible workaround -- self-hosted test runner
def test_query():
    chatbot = classes.ChatModel(url=config.URL_CB, api_key=config.API_KEY_CB, chatbot_id=config.ID_CB)
    res = chatbot.query('What does an increased level of albumin mean?')
    assert res[0] == True