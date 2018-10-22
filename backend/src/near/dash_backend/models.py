from schematics import Model
from schematics.types import (
    FloatType,
    ListType,
    ModelType,
    StringType,
)

from near.dash_pylib.models import ObserverData


class NodeStats(Model):
    node_id = StringType(required=True)
    avg_prop_time = FloatType(required=True)


class DashboardData(Model):
    observer_data = ModelType(ObserverData)
    node_stats = ListType(ModelType(NodeStats))