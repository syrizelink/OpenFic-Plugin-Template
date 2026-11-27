"""A native sidebar view with one persisted value."""

STATUS_KEY = "completed"
ACTION_STATUS = {"complete": True, "reset": False}


async def render(context, params):
    completed = await context.storage.get(STATUS_KEY, False)
    return {
        "tree": {
            "type": "Flex",
            "props": {"direction": "column", "gap": "3"},
            "children": [
                {
                    "type": "Text",
                    "children": "试用已完成" if completed else "试用尚未完成",
                },
                {
                    "type": "Button",
                    "props": {"onPress": "reset" if completed else "complete"},
                    "children": "重置试用状态" if completed else "标记试用完成",
                },
            ],
        },
    }


async def action(context, params):
    action_id = params["id"]
    if action_id not in ACTION_STATUS:
        raise ValueError("Unknown example action")
    await context.storage.set(STATUS_KEY, ACTION_STATUS[action_id])
    context.invalidate_ui(params["viewId"])


def register(host):
    host.register_command("example.render", render)
    host.register_command("example.action", action)
