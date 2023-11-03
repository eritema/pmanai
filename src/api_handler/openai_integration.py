import openai

def transcribe_audio(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        transcription = openai.Audio.transcribe("whisper-1", audio_file)
    return transcription['text']

def minutes_extraction(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                #"content": "You are a highly skilled AI trained in language comprehension and summarization. I would like you to read the following transcription of a meeting and summarize it into a meeting minutes report with: discussion points and Action items. The name of the partecipant that spoke the sentence is at the beginning of the line like in the example in ''' deimiter. \
                "content": "The attenders of the meeting are at the beginning of each line (see example in ''' delimiter). Task: Produce a detailed report with the minutes of the meeting. Compose detailed meeting notes for each agenda item discussed during the meeting. Highlight important insights, outcomes, and any unresolved issues for further consideration.\
'''#Input\
Raf: I say something related to the to the meeting.\
Pippo: Contribute to the meeting with something that is written here.\
Output \
#Meeting Minutes\
\
**Date:** [Insert Date]\
**Time:** [Insert Time]\
**Location:** [Insert Location]\
**Attendees:** Raf, Pippo.\
### Discussion Points\
...\
\
### Actions Items\
...\
\
### Next Meeting: TBD\
'''"
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']


def clean_transcription(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a highly skilled AI trained in language comprehension. I would like you to parse the following raw transcription of a meeting and clean it from  greetings and interjections"
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

def reduce_transcription(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a highly skilled AI trained in language comprehension. I would like you to parse the following raw transcription of a meeting, clean it from  greetings and interjections, and remove the redundant information, preserving the answers and the questions."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']



def abstract_summary_extraction(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a highly skilled AI trained in language comprehension and summarization. I would like you to read the following text and summarize it into a concise abstract paragraph. Aim to retain the most important points, providing a coherent and readable summary that could help a person understand the main points of the discussion without needing to read the entire text. Please avoid unnecessary details or tangential."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

def key_points_extraction(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a proficient AI with a specialty in distilling information into key points. Based on the following text, identify and list the main points that were discussed or brought up. These should be the most important ideas, findings, or topics that are crucial to the essence of the discussion. Your goal is to provide a list that someone could read to quickly understand what was talked about."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

def risks_extraction(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a proficient AI with a specialty in distilling information into risks. \
                Based on the following text, identify and list the main risks that can be identified. \
                These should be the most important risks, threats, or issues that are crucial and can \
                harm the businnes. Your goal is to provide a table of risks and risk response that someone \
                could read to quickly understand. \
                \
                | Risk ID | Risk Description | Risk Probability | Risk impact | Risk Reponse|Risk Type|\
                |---|---|---|---|---|\
                |R00|Inability to generate enough bookings to drive growth| Medium | High | Focus on increase bookings by expanding the business development team and implementing new strategies|Financial, Strategic|\
                \
                The `Risk Type` can be: Opportunity, Reputation, Operational, Financial, Strategic, Hazard, Compliance, Uncertainty, Security, Economic, Competition."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

def action_item_extraction(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are an AI expert in analyzing conversations and extracting action items. Please review the text and identify any tasks, assignments, or actions that were agreed upon or mentioned as needing to be done. These could be tasks assigned to specific individuals, or general actions that the group has decided to take. Please list these action items clearly and concisely."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

def sentiment_analysis(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "As an AI with expertise in language and emotion analysis, your task is to analyze the sentiment of the following text. Please consider the overall tone of the discussion, the emotion conveyed by the language used, and the context in which words and phrases are used. Indicate whether the sentiment is generally positive, negative, or neutral, and provide brief explanations for your analysis where possible."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

def diagram_extraction(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "As an AI with expertise in analysing text and extracting actions, states and relations among objext, your task is to represent the following text as a diagram. Consider to review the text and identify any tasks, assignments, actions, state and relation and produce an appropriate diagram in mermaid language."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']
 
