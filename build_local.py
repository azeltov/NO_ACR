from azureml.core import Workspace
from azureml.core import Environment
from azureml.core.runconfig import DockerConfiguration
from azureml.core.conda_dependencies import CondaDependencies

ws = Workspace.from_config()
print(ws.name, ws.resource_group, ws.location, ws.subscription_id, sep = '\n')

myenv = Environment.get(workspace=ws, name="myenv")

myenv.build_local(workspace=ws, useDocker=True) 