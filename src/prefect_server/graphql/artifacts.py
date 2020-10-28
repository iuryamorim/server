from typing import Any


from graphql import GraphQLResolveInfo

from prefect_server import api
from prefect_server.utilities.graphql import mutation


@mutation.field("create_task_run_artifact")
async def resolve_create_task_run_artifact(
    obj: Any, info: GraphQLResolveInfo, input: dict
) -> dict:
    task_run_artifact_id = await api.artifacts.create_task_run_artifact(
        task_run_id=input.get("task_run_id"),
        kind=input.get("kind"),
        data=input.get("data"),
        tenant_id=input.get("tenant_id"),
    )
    return {"id": task_run_artifact_id}


@mutation.field("update_task_run_artifact")
async def resolve_update_task_run_artifact(
    obj: Any, info: GraphQLResolveInfo, input: dict
) -> dict:
    success = await api.artifacts.update_task_run_artifact(
        task_run_artifact_id=input.get("task_run_artifact_id"),
        data=input.get("data"),
    )
    return {"success": success}


@mutation.field("delete_task_run_artifact")
async def resolve_delete_task_run_artifact(
    obj: Any, info: GraphQLResolveInfo, input: dict
) -> dict:
    success = await api.artifacts.delete_task_run_artifact(
        task_run_artifact_id=input.get("task_run_artifact_id"),
    )
    return {"success": success}
