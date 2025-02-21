from pydantic import BaseModel, Field
from typing import Optional
from fastapi.requests import Request
from open_webui.apps.webui.models.users import Users
from open_webui.main import webui_app
from open_webui.apps.webui.routers.memories import add_memory, AddMemoryForm


class Action:
    class Valves(BaseModel):
        pass

    class UserValves(BaseModel):
        show_status: bool = Field(
            default=True, description="Show status of the action."
        )
        pass

    def __init__(self):
        self.valves = self.Valves()
        pass

    async def action(
        self,
        body: dict,
        __user__=None,
        __event_emitter__=None,
        __event_call__=None,
    ) -> Optional[dict]:
        print(f"action:{__name__}")

        user_valves = __user__.get("valves")
        if not user_valves:
            user_valves = self.UserValves()

        if __event_emitter__:
            last_assistant_message = body["messages"][-1]
            user = Users.get_user_by_id(__user__["id"])

            if user_valves.show_status:
                await __event_emitter__(
                    {
                        "type": "status",
                        "data": {"description": "Adding to Memories", "done": False},
                    }
                )

            # add the assistant response to memories
            try:
                memory_obj = await add_memory(
                    request=Request(scope={"type": "http", "app": webui_app}),
                    form_data=AddMemoryForm(content=last_assistant_message["content"]),
                    user=user,
                )
                print(f"Memory Added: {memory_obj}")
            except Exception as e:
                print(f"Error adding memory {str(e)}")
                if user_valves.show_status:
                    await __event_emitter__(
                        {
                            "type": "status",
                            "data": {
                                "description": "Error Adding Memory",
                                "done": True,
                            },
                        }
                    )

                    # add a citation to the message with the error
                    await __event_emitter__(
                        {
                            "type": "citation",
                            "data": {
                                "source": {"name": "Error:adding memory"},
                                "document": [str(e)],
                                "metadata": [{"source": "Add to Memory Action Button"}],
                            },
                        }
                    )

            if user_valves.show_status:
                await __event_emitter__(
                    {
                        "type": "status",
                        "data": {"description": "Memory Saved", "done": True},
                    }
                )
