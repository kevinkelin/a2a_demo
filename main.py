from adk_starter.agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
import anyio
from dotenv import load_dotenv

load_dotenv("adk_starter/.env")

async def call_agent_async(query: str):
    session_service = InMemorySessionService()

    APP_NAME = "weather_and_time"
    USER_ID = "user_1"
    SESSION_ID = "session_001" 

    # # Create the specific session where the conversation will happen
    session = session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

    runner = Runner(
        agent=root_agent, # The agent we want to run
        app_name=APP_NAME,   # Associates runs with our app
        session_service=session_service # Uses our session manager
    )
    content = types.Content(role='user', parts=[types.Part(text=query)])
    final_response_text = "对不起，agent 不能回答您的问题"
    async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content):
      if event.is_final_response():
          if event.content and event.content.parts:
             final_response_text = event.content.parts[0].text
          elif event.actions and event.actions.escalate: # Handle potential errors/escalations
             final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
          # Add more checks here if needed (e.g., specific error codes)
          break # Stop processing events once the final response is found

    print(f"<<< Agent Response: {final_response_text}")

if __name__ == "__main__":
    anyio.run(call_agent_async, "北京明天的天气")