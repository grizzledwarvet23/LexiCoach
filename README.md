# LexiCoach
 Built for TreeHacks 2023 with love
 
 ## Motivation
 
 Language is complex -- extremely complex. When learning a new language, simply google translating words or phrases and stringing them together results in a significant loss of context and nuance. Even in your native language, it can be a steep learning curve to familiarize yourself with technical vocabulary words in without a proper understanding of them. Through LexiCoach, we hope to automate the process for language users of all fluency levels to develop their language skills in the way they need the most.
 
## Tech Stack

We used JavaScript & HTML for the front-end, Python and the OpenAI API for the back-end, and Python Flask to connect the frontend and backend. For storing and retrieving vocabulary list data, we used SQL Alchemy. Special shoutout to checkbook for making the donation functionality so easy to build :)

## Functionality Summary

Users are able to select from a variety of pre-selected lists, as well as importing their own list, of words that they wish to practice on. The OpenAI model then generates the specified amount of sentences, with a word in the user-provided word list blocked out for user completion. Once the user completes it, the app calculates accuracy of the user's responses. We also incorporate the ability for users to see saved word lists, so they don't have to import the same thing over and over again.
