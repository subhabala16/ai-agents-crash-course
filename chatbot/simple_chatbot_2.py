import dotenv
import chainlit as cl
from nutrition_agent import nutrition_agent
from agents import Runner
dotenv.load_dotenv()

@cl.on_message
async def on_message(message: cl.Message):
    result = await Runner.run(nutrition_agent,message.content)
    
    await cl.Message(content=result.final_output).send()
