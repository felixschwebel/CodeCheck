# CodeCheck
In this project, I wanted to build a website that helps programmers with their code using AI. 

The idea was that users could provide their code by typing or copying it into the code window, uploading the code file, or selecting a GitHub repository. Then the user has to choose their language and action. Those actions could explain their code, optimise it for better runtime and readability, fix common bugs, provide documentation or convert it to a compatible language. For every action, a new tile pops up in the middle so that it's possible to select multiple actions and scroll through all the results. If the user finds a result especially useful, it can be saved to their profile. 

The code and action are combined in the backend and sent to the OpenAI API. The answer is provided in those tiles. This doesn't work as it is right now because I don't want to connect it to the live API yet. 

It is a fun project which taught me a lot while figuring out how to get those scrollable tiles and coding windows programmed. It's far from finished, but maybe I'll update it occasionally.

Here is the mockup that I created with **Figma**:
<br></br>
<img width="1492" alt="Screenshot 2023-05-25 at 17 40 33" src="https://github.com/felixschwebel/CodeCheck/assets/111788725/2a571a5c-7211-43f5-990c-18a91745525f">
<br></br>
And here is a screenshot of the programmed website (at least the page with all those actions):
<br></br>
<img width="1568" alt="Screenshot 2023-05-25 at 17 57 37" src="https://github.com/felixschwebel/CodeCheck/assets/111788725/b7f6c8ff-88f1-4198-9bff-115b927107ab">


