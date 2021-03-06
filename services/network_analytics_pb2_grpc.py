# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import network_analytics_pb2 as network__analytics__pb2


class NetowrkAnalyticsStub(object):
  """/// End Bipartite graph

  /// Network Analytics Services

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.BipartiteGraph = channel.unary_unary(
        '/NetowrkAnalytics/BipartiteGraph',
        request_serializer=network__analytics__pb2.BipartiteGraphRequest.SerializeToString,
        response_deserializer=network__analytics__pb2.BipartiteGraphResponse.FromString,
        )
    self.ProjectedGraph = channel.unary_unary(
        '/NetowrkAnalytics/ProjectedGraph',
        request_serializer=network__analytics__pb2.ProjecetedGraphRequest.SerializeToString,
        response_deserializer=network__analytics__pb2.ProjecetedGraphResponse.FromString,
        )


class NetowrkAnalyticsServicer(object):
  """/// End Bipartite graph

  /// Network Analytics Services

  """

  def BipartiteGraph(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ProjectedGraph(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NetowrkAnalyticsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'BipartiteGraph': grpc.unary_unary_rpc_method_handler(
          servicer.BipartiteGraph,
          request_deserializer=network__analytics__pb2.BipartiteGraphRequest.FromString,
          response_serializer=network__analytics__pb2.BipartiteGraphResponse.SerializeToString,
      ),
      'ProjectedGraph': grpc.unary_unary_rpc_method_handler(
          servicer.ProjectedGraph,
          request_deserializer=network__analytics__pb2.ProjecetedGraphRequest.FromString,
          response_serializer=network__analytics__pb2.ProjecetedGraphResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'NetowrkAnalytics', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
