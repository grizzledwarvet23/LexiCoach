# LexiCoach
 Built for TreeHacks 2023 with love
 
 ## Motivation
 
Learning vocabulary in a new language is hard! Flash-card style apps can help, but they only let you practice you understanding of vocabulary in a very narrow setting. LexiCoach uses a GPT-3 based model to generate in-context exercises that allow you to practice new vocabulary in a target language. LexiCoach allows you to tailor your language practice to your own interests.
 
## Tech Stack

We used JavaScript & HTML for the front-end, Python and the OpenAI API for the back-end, and Python Flask to connect the frontend and backend. For storing and retrieving vocabulary list data, we used SQL Alchemy. Special shoutout to checkbook for making the donation functionality so easy to build :)

## Functionality Summary

Users are able to select from a variety of pre-selected lists, as well as importing their own list, of words that they wish to practice on. The OpenAI model then generates the specified amount of sentences, with a word in the user-provided word list blocked out for user completion. Once the user completes it, the app calculates accuracy of the user's responses. We also incorporate the ability for users to see saved word lists, so they don't have to import the same thing over and over again.
