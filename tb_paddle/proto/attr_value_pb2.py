# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tb_paddle/proto/attr_value.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tb_paddle.proto import tensor_pb2 as tb__paddle_dot_proto_dot_tensor__pb2
from tb_paddle.proto import tensor_shape_pb2 as tb__paddle_dot_proto_dot_tensor__shape__pb2
from tb_paddle.proto import types_pb2 as tb__paddle_dot_proto_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tb_paddle/proto/attr_value.proto',
  package='tb_paddle',
  syntax='proto3',
  serialized_options=_b('\n\030org.tensorflow.frameworkB\017AttrValueProtosP\001\370\001\001'),
  serialized_pb=_b('\n tb_paddle/proto/attr_value.proto\x12\ttb_paddle\x1a\x1ctb_paddle/proto/tensor.proto\x1a\"tb_paddle/proto/tensor_shape.proto\x1a\x1btb_paddle/proto/types.proto\"\x9d\x04\n\tAttrValue\x12\x0b\n\x01s\x18\x02 \x01(\x0cH\x00\x12\x0b\n\x01i\x18\x03 \x01(\x03H\x00\x12\x0b\n\x01\x66\x18\x04 \x01(\x02H\x00\x12\x0b\n\x01\x62\x18\x05 \x01(\x08H\x00\x12#\n\x04type\x18\x06 \x01(\x0e\x32\x13.tb_paddle.DataTypeH\x00\x12,\n\x05shape\x18\x07 \x01(\x0b\x32\x1b.tb_paddle.TensorShapeProtoH\x00\x12(\n\x06tensor\x18\x08 \x01(\x0b\x32\x16.tb_paddle.TensorProtoH\x00\x12.\n\x04list\x18\x01 \x01(\x0b\x32\x1e.tb_paddle.AttrValue.ListValueH\x00\x12\'\n\x04\x66unc\x18\n \x01(\x0b\x32\x17.tb_paddle.NameAttrListH\x00\x12\x15\n\x0bplaceholder\x18\t \x01(\tH\x00\x1a\xe5\x01\n\tListValue\x12\t\n\x01s\x18\x02 \x03(\x0c\x12\r\n\x01i\x18\x03 \x03(\x03\x42\x02\x10\x01\x12\r\n\x01\x66\x18\x04 \x03(\x02\x42\x02\x10\x01\x12\r\n\x01\x62\x18\x05 \x03(\x08\x42\x02\x10\x01\x12%\n\x04type\x18\x06 \x03(\x0e\x32\x13.tb_paddle.DataTypeB\x02\x10\x01\x12*\n\x05shape\x18\x07 \x03(\x0b\x32\x1b.tb_paddle.TensorShapeProto\x12&\n\x06tensor\x18\x08 \x03(\x0b\x32\x16.tb_paddle.TensorProto\x12%\n\x04\x66unc\x18\t \x03(\x0b\x32\x17.tb_paddle.NameAttrListB\x07\n\x05value\"\x90\x01\n\x0cNameAttrList\x12\x0c\n\x04name\x18\x01 \x01(\t\x12/\n\x04\x61ttr\x18\x02 \x03(\x0b\x32!.tb_paddle.NameAttrList.AttrEntry\x1a\x41\n\tAttrEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.tb_paddle.AttrValue:\x02\x38\x01\x42\x30\n\x18org.tensorflow.frameworkB\x0f\x41ttrValueProtosP\x01\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[tb__paddle_dot_proto_dot_tensor__pb2.DESCRIPTOR,tb__paddle_dot_proto_dot_tensor__shape__pb2.DESCRIPTOR,tb__paddle_dot_proto_dot_types__pb2.DESCRIPTOR,])




_ATTRVALUE_LISTVALUE = _descriptor.Descriptor(
  name='ListValue',
  full_name='tb_paddle.AttrValue.ListValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s', full_name='tb_paddle.AttrValue.ListValue.s', index=0,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='i', full_name='tb_paddle.AttrValue.ListValue.i', index=1,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='f', full_name='tb_paddle.AttrValue.ListValue.f', index=2,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='tb_paddle.AttrValue.ListValue.b', index=3,
      number=5, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='tb_paddle.AttrValue.ListValue.type', index=4,
      number=6, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape', full_name='tb_paddle.AttrValue.ListValue.shape', index=5,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensor', full_name='tb_paddle.AttrValue.ListValue.tensor', index=6,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='func', full_name='tb_paddle.AttrValue.ListValue.func', index=7,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=446,
  serialized_end=675,
)

_ATTRVALUE = _descriptor.Descriptor(
  name='AttrValue',
  full_name='tb_paddle.AttrValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s', full_name='tb_paddle.AttrValue.s', index=0,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='i', full_name='tb_paddle.AttrValue.i', index=1,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='f', full_name='tb_paddle.AttrValue.f', index=2,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='tb_paddle.AttrValue.b', index=3,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='tb_paddle.AttrValue.type', index=4,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape', full_name='tb_paddle.AttrValue.shape', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensor', full_name='tb_paddle.AttrValue.tensor', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='tb_paddle.AttrValue.list', index=7,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='func', full_name='tb_paddle.AttrValue.func', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='placeholder', full_name='tb_paddle.AttrValue.placeholder', index=9,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ATTRVALUE_LISTVALUE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='tb_paddle.AttrValue.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=143,
  serialized_end=684,
)


_NAMEATTRLIST_ATTRENTRY = _descriptor.Descriptor(
  name='AttrEntry',
  full_name='tb_paddle.NameAttrList.AttrEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tb_paddle.NameAttrList.AttrEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tb_paddle.NameAttrList.AttrEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=766,
  serialized_end=831,
)

_NAMEATTRLIST = _descriptor.Descriptor(
  name='NameAttrList',
  full_name='tb_paddle.NameAttrList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tb_paddle.NameAttrList.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attr', full_name='tb_paddle.NameAttrList.attr', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_NAMEATTRLIST_ATTRENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=687,
  serialized_end=831,
)

_ATTRVALUE_LISTVALUE.fields_by_name['type'].enum_type = tb__paddle_dot_proto_dot_types__pb2._DATATYPE
_ATTRVALUE_LISTVALUE.fields_by_name['shape'].message_type = tb__paddle_dot_proto_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_ATTRVALUE_LISTVALUE.fields_by_name['tensor'].message_type = tb__paddle_dot_proto_dot_tensor__pb2._TENSORPROTO
_ATTRVALUE_LISTVALUE.fields_by_name['func'].message_type = _NAMEATTRLIST
_ATTRVALUE_LISTVALUE.containing_type = _ATTRVALUE
_ATTRVALUE.fields_by_name['type'].enum_type = tb__paddle_dot_proto_dot_types__pb2._DATATYPE
_ATTRVALUE.fields_by_name['shape'].message_type = tb__paddle_dot_proto_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_ATTRVALUE.fields_by_name['tensor'].message_type = tb__paddle_dot_proto_dot_tensor__pb2._TENSORPROTO
_ATTRVALUE.fields_by_name['list'].message_type = _ATTRVALUE_LISTVALUE
_ATTRVALUE.fields_by_name['func'].message_type = _NAMEATTRLIST
_ATTRVALUE.oneofs_by_name['value'].fields.append(
  _ATTRVALUE.fields_by_name['s'])
_ATTRVALUE.fields_by_name['s'].containing_oneof = _ATTRVALUE.oneofs_by_name['value']
_ATTRVALUE.oneofs_by_name['value'].fields.append(
  _ATTRVALUE.fields_by_name['i'])
_ATTRVALUE.fields_by_name['i'].containing_oneof = _ATTRVALUE.oneofs_by_name['value']
_ATTRVALUE.oneofs_by_name['value'].fields.append(
  _ATTRVALUE.fields_by_name['f'])
_ATTRVALUE.fields_by_name['f'].containing_oneof = _ATTRVALUE.oneofs_by_name['value']
_ATTRVALUE.oneofs_by_name['value'].fields.append(
  _ATTRVALUE.fields_by_name['b'])
_ATTRVALUE.fields_by_name['b'].containing_oneof = _ATTRVALUE.oneofs_by_name['value']
_ATTRVALUE.oneofs_by_name['value'].fields.append(
  _ATTRVALUE.fields_by_name['type'])
_ATTRVALUE.fields_by_name['type'].containing_oneof = _ATTRVALUE.oneofs_by_name['value']
_ATTRVALUE.oneofs_by_name['value'].fields.append(
  _ATTRVALUE.fields_by_name['shape'])
_ATTRVALUE.fields_by_name['shape'].containing_oneof = _ATTRVALUE.oneofs_by_name['value']
_ATTRVALUE.oneofs_by_name['value'].fields.append(
  _ATTRVALUE.fields_by_name['tensor'])
_ATTRVALUE.fields_by_name['tensor'].containing_oneof = _ATTRVALUE.oneofs_by_name['value']
_ATTRVALUE.oneofs_by_name['value'].fields.append(
  _ATTRVALUE.fields_by_name['list'])
_ATTRVALUE.fields_by_name['list'].containing_oneof = _ATTRVALUE.oneofs_by_name['value']
_ATTRVALUE.oneofs_by_name['value'].fields.append(
  _ATTRVALUE.fields_by_name['func'])
_ATTRVALUE.fields_by_name['func'].containing_oneof = _ATTRVALUE.oneofs_by_name['value']
_ATTRVALUE.oneofs_by_name['value'].fields.append(
  _ATTRVALUE.fields_by_name['placeholder'])
_ATTRVALUE.fields_by_name['placeholder'].containing_oneof = _ATTRVALUE.oneofs_by_name['value']
_NAMEATTRLIST_ATTRENTRY.fields_by_name['value'].message_type = _ATTRVALUE
_NAMEATTRLIST_ATTRENTRY.containing_type = _NAMEATTRLIST
_NAMEATTRLIST.fields_by_name['attr'].message_type = _NAMEATTRLIST_ATTRENTRY
DESCRIPTOR.message_types_by_name['AttrValue'] = _ATTRVALUE
DESCRIPTOR.message_types_by_name['NameAttrList'] = _NAMEATTRLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AttrValue = _reflection.GeneratedProtocolMessageType('AttrValue', (_message.Message,), {

  'ListValue' : _reflection.GeneratedProtocolMessageType('ListValue', (_message.Message,), {
    'DESCRIPTOR' : _ATTRVALUE_LISTVALUE,
    '__module__' : 'tb_paddle.proto.attr_value_pb2'
    # @@protoc_insertion_point(class_scope:tb_paddle.AttrValue.ListValue)
    })
  ,
  'DESCRIPTOR' : _ATTRVALUE,
  '__module__' : 'tb_paddle.proto.attr_value_pb2'
  # @@protoc_insertion_point(class_scope:tb_paddle.AttrValue)
  })
_sym_db.RegisterMessage(AttrValue)
_sym_db.RegisterMessage(AttrValue.ListValue)

NameAttrList = _reflection.GeneratedProtocolMessageType('NameAttrList', (_message.Message,), {

  'AttrEntry' : _reflection.GeneratedProtocolMessageType('AttrEntry', (_message.Message,), {
    'DESCRIPTOR' : _NAMEATTRLIST_ATTRENTRY,
    '__module__' : 'tb_paddle.proto.attr_value_pb2'
    # @@protoc_insertion_point(class_scope:tb_paddle.NameAttrList.AttrEntry)
    })
  ,
  'DESCRIPTOR' : _NAMEATTRLIST,
  '__module__' : 'tb_paddle.proto.attr_value_pb2'
  # @@protoc_insertion_point(class_scope:tb_paddle.NameAttrList)
  })
_sym_db.RegisterMessage(NameAttrList)
_sym_db.RegisterMessage(NameAttrList.AttrEntry)


DESCRIPTOR._options = None
_ATTRVALUE_LISTVALUE.fields_by_name['i']._options = None
_ATTRVALUE_LISTVALUE.fields_by_name['f']._options = None
_ATTRVALUE_LISTVALUE.fields_by_name['b']._options = None
_ATTRVALUE_LISTVALUE.fields_by_name['type']._options = None
_NAMEATTRLIST_ATTRENTRY._options = None
# @@protoc_insertion_point(module_scope)
