"""title: File Handler
author: CypherOxide
author_url: https://angelsantiago.me

"""

import os
import requests
from datetime import datetime
from typing import Callable

from open_webui.apps.webui.models.users import Users


class Tools:
    def __init__(self):
        pass

    async def generate_image(
        self, prompt: str, __user__: dict, __event_emitter__=None
    ) -> str:
        """
        print files
        """
        dir_path = "/app/backend/data/uploads"
        try:
            # Emit the status while reading the directory
            await __event_emitter__(
                {
                    "type": "status",
                    "data": {"description": "Reading directory...", "done": False},
                }
            )

            # List all files in the directory
            if os.path.exists(dir_path):
                files = os.listdir(dir_path)
                all_contents = ""

                # Loop over files to print their contents
                for file_name in files:
                    file_path = os.path.join(dir_path, file_name)

                    # Read the file content
                    with open(file_path, "r") as file:
                        content = file.read()
                        all_contents += f"\n--- {file_name} ---\n{content}\n"

                # Emit message with file contents
                await __event_emitter__(
                    {
                        "type": "message",
                        "data": {"content": all_contents},
                    }
                )

            # Done emitting statuses
            await __event_emitter__(
                {
                    "type": "status",
                    "data": {"description": "Completed task.", "done": True},
                }
            )

        except Exception as e:
            await __event_emitter__(
                {
                    "type": "status",
                    "data": {"description": f"Error: {e}", "done": True},
                }
            )

            return f"Error encountered: {e}"
